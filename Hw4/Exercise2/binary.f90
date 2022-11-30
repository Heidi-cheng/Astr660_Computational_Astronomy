!---------------------------------------------------
!
! National Tsing Hua University
!
! ASTR 660 Computational Astrophysics
!
! Created:  Kuo-Chuan Pan 2020
! Modified: Karen Yang 2022.10.21
!
! Problem:
!
!        Simulating binary orbits
!
program binary

    use constants
    use Simulation_data
    use physics, only : initial, update, update_rk4
    use output, only : record

    implicit none

    integer :: i, interval, noutput, step
    real :: dt, time, tmax
    !real, dimension(6) :: yin1, yin2

    ! initial setup
    step     = 0             ! start from 0th step
    dt       = 0.01 * yr  ! sec, time step
    time     = 0.0           ! sec, start from t=0
    tmax     = 10.0 * yr     ! sec, max simulation time

    ! output intervals to record trajectory
    noutput  = 500
    interval = (tmax/dt)/noutput

    ! initialize the stars
    call initial()
    !yin1(1) = stars(1)%x
    !yin1(2) = stars(1)%y
    !yin1(3) = stars(1)%vx
    !yin1(4) = stars(1)%vy
    !yin1(5) = fx1/stars(1)%mass
    !yin1(6) = fy1/stars(1)%mass

    !yin2(1) = stars(2)%x
    !yin2(2) = stars(2)%y
    !yin2(3) = stars(2)%vx
    !yin2(4) = stars(2)%vy
    !yin2(5) = fx2/stars(2)%mass
    !yin2(6) = fy2/stars(2)%mass

    ! the main time loop
    do while (time .le. tmax)

        ! update stars
        !call update(dt)
        call update_rk4(dt)

        ! update time
        time = time + dt

        ! output data
        if (mod(step,interval) .eq. 0) then
            call record(time)
        endif

        ! update step
        step = step + 1
    end do
    
    print *, "DONE!"

end program binary

