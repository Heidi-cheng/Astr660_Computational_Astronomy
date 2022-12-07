subroutine evolution()
    use Simulation_data
    use IO, only : output
    implicit none

    integer :: n
    real    :: dt, time

    n        = 0
    time     = 0.0

    dt = abs(dx/cx)*cfl

    do while(time .le. tend)
        
        if (mod(n,io_interval) .eq. 0) then
            print *, "n =", n ," Time =", time
            call output(n,time)
        endif
        call update(time, dt)
        
        n    = n + 1
        time = time + dt
    enddo

end subroutine evolution


!!
!! 
!!
subroutine update(time, dt)
    use Simulation_data
    implicit none
    real, intent(in) :: time ,dt
    integer :: i, j
    real    :: FL, FR, FLy, FRy

    ! x direction
    call boundary(u)
    uold = u
    do j = jstart, jend
        do i = istart, iend
            call flux(i,j,dt,FL,FR)
            u(i, j) = uold(i, j) - dt/dx*(FR-FL)
        enddo
    enddo

    ! y direction
    !call boundary(u)
    uold = u
    do i = istart, iend
        do j = jstart, jend
            call yflux(i,j,dt,FLy,FRy)
            u(i, j) = uold(i, j) - dt/dy*(FRy-FLy)
        enddo
    enddo

end subroutine update

!
! Routine to evalue flux the cell edge
!
subroutine flux(i,j,dt,FL, FR)
    use Simulation_data
    implicit none
    integer, intent(in) :: i, j
    real, intent(in)    :: dt
    real, intent(out)   :: FL, FR
    real :: sig, a, b, qL, qR

    !! Use piecewise linear and slope limiter
    !! left state
    call get_slope(dx,uold(i-2, j),uold(i-1, j),uold(i, j),sig) ! compute sig(i-1)
    FL = cx*uold(i-1, j) + 0.5*cx*(dx-cx*dt)*sig
    !! right state
    call get_slope(dx,uold(i-1, j),uold(i, j),uold(i+1, j),sig) ! compute sig(i)
    FR = cx*uold(i, j) + 0.5*cx*(dx-cx*dt)*sig

    return

end subroutine flux

subroutine yflux(i,j,dt,FLy, FRy)
    use Simulation_data
    implicit none
    integer, intent(in) :: i,j
    real, intent(in)    :: dt
    real, intent(out)   :: FLy, FRy
    real :: sig, a, b, qL, qR

    call get_slope(dy,uold(i, j-2),uold(i, j-1),uold(i, j),sig) ! compute sig(i-1)
    FLy = cy*uold(i, j-1) + 0.5*cy*(dy-cy*dt)*sig

    call get_slope(dy,uold(i, j-1),uold(i, j),uold(i, j+1),sig) ! compute sig(i)
    FRy = cy*uold(i, j) + 0.5*cy*(dy-cy*dt)*sig

    return

end subroutine yflux


subroutine get_slope(ddx,l,m,r,sig)
    use Simulation_data
    implicit none
    real, intent(in)  :: ddx
    real, intent(in)  :: l   ! left 
    real, intent(in)  :: m   ! middle
    real, intent(in)  :: r   ! right
    real, intent(out) :: sig ! the slope
    real :: a, b

    ! compute a and b as the left/right slopes 
    a = (m-l)/ddx
    b = (r-m)/ddx

    ! TODO: implement the minmod limiter

    if (abs(a)<abs(b) .and. a*b>0) then
        sig = a
    else if (abs(b)<abs(a) .and. a*b>0) then
        sig = b        
    else if (a*b<0) then
        sig = 0
    end if

    return
end subroutine get_slope
