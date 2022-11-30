!---------------------------------------------------
! The physics module
!
module physics
    use Simulation_data
    implicit none
    contains
        
        subroutine initial()
            !
            ! setup initial conditions of each stars
            ! in this example we only have two stars
            !
            use constants, only : au, msun, pi, G
            implicit none
            integer :: i
            real :: m1, m2, force, angle
            angle = 0.0

            m1 = 1.0 * msun
            m2 = 2.0 * msun

            !
            ! Use Kepler's law to evaluate the orbital period
            ! and use Newton's law to evaluate the force between
            ! two stars
            !

            separation = 3.0*au 
            period     = sqrt((4.0*(pi**2.0)*(separation**3.0))/(G*(m1+m2))) 
            force      = (G*m1*m2)/(separation**2.0) 

            !
            ! setup initial conditions of star M1
            stars(1)%mass = m1
            stars(1)%x    = -2.0*au 
            stars(1)%y    = 0.0 
            stars(1)%vx   = 0.0 
            stars(1)%vy   = -(2.0 * pi * (stars(1)%x))/period 
            stars(1)%ax   = force/stars(1)%mass 
            stars(1)%ay   = 0.0 

            !
            ! setup initial conditions of star M2
            stars(2)%mass = m2
            stars(2)%x    = 1.0*au 
            stars(2)%y    = 0.0 
            stars(2)%vx   = 0.0 
            stars(2)%vy   = -(2.0 * pi * (stars(2)%x))/period 
            stars(2)%ax   = force/stars(2)%mass 
            stars(2)%ay   = 0.0 


        end subroutine initial

        subroutine update(dt)
            use constants, only: G
            implicit none
            real, intent(in)  :: dt
            integer :: i,j
            real    :: x, y, rsq, fx1, fy1, fx2, fy2
            real    :: radius, force, angle1, angle2

            !
            ! In this example we use a first order scheme (Euler method)
            ! we approximate dx/dt = v  --> x^(n+1) - x^n = v * dt
            ! therefore, x at step n+1 = x^(n+1) = x^n + v * dt
            !
            ! the same approximation can be applied to dv/dt = a
            !
        
            stars(1)%x = stars(1)%x + stars(1)%vx*dt
            stars(1)%vx = stars(1)%vx + stars(1)%ax*dt

            stars(1)%y = stars(1)%y + stars(1)%vy*dt
            stars(1)%vy = stars(1)%vy + stars(1)%ay*dt

            stars(2)%x = stars(2)%x + stars(2)%vx*dt
            stars(2)%vx = stars(2)%vx + stars(2)%ax*dt

            stars(2)%y = stars(2)%y + stars(2)%vy*dt
            stars(2)%vy = stars(2)%vy + stars(2)%ay*dt

            !rsq = ((stars(1)%x)**2+(stars(1)%y)**2) + ((stars(2)%x)**2+(stars(2)%y)**2)
            !angle = angle + ((2.0*pi)/period) * dt
            rsq = (stars(2)%x-stars(1)%x)**2.0 + (stars(1)%y-stars(2)%y)**2.0
            !angle1 = atan(stars(1)%y/stars(1)%x)
            !print *, "angle=", angle
            force = (G*stars(1)%mass*stars(2)%mass)/rsq
            !fx1 = abs(force * cos(angle1))
            !fy1 = abs(force * sin(angle1))

            !stars(1)%ax = fx1/stars(1)%mass
            !stars(1)%ay = -fy1/stars(1)%mass
            
            stars(1)%ax = (force/stars(1)%mass)*(stars(2)%x-stars(1)%x)/(rsq**0.5)
            stars(1)%ay = (force/stars(1)%mass)*(stars(2)%y-stars(1)%y)/(rsq**0.5)

            !angle2 = atan(stars(2)%y/stars(2)%x)
            !print *, "angle=", angle
            !force = (G*stars(1)%mass*stars(2)%mass)/rsq
            !fx2 = abs(force * cos(angle2))
            !fy2 = abs(force * sin(angle2))

            !stars(2)%ax = -fx2/stars(2)%mass
            !stars(2)%ay = fy2/stars(2)%mass

            !stars(2)%ax = -1.0 * (stars(1)%ax * stars(1)%mass)/stars(2)%mass
            !stars(2)%ay = -1.0 * (stars(1)%ay * stars(1)%mass)/stars(2)%mass

            stars(2)%ax =(force/stars(2)%mass)*(stars(1)%x-stars(2)%x)/(rsq**0.5)
            stars(2)%ay =(force/stars(2)%mass)*(stars(1)%y-stars(2)%y)/(rsq**0.5)

            !if (180 > angle*180/pi .and. angle*180/pi> 90) then
            !    stars(2)%ax =  fx/stars(2)%mass
            !    stars(1)%ax = -fx/stars(1)%mass
            !else if (180 > angle*180/pi .and. angle*180/pi > 270) then
            !    stars(1)%ax = -fx/stars(1)%mass
            !    stars(1)%ay =  fy/stars(1)%mass
            !    stars(2)%ax =  fx/stars(2)%mass
            !    stars(2)%ay = -fy/stars(2)%mass
            !else if (270 > angle*180/pi .and. angle*180/pi > 360) then
            !    stars(1)%ax =  fx/stars(1)%mass
            !    stars(1)%ay =  fy/stars(1)%mass
            !    stars(2)%ax = -fx/stars(2)%mass
            !    stars(2)%ay = -fy/stars(2)%mass
            !end if
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
            
            !call euler(n, yin1, ynext1, t, dt, func)
            !call euler(n, yin2, ynext2, t, dt, func)

            ! update position to t = t + dt
            
            !TODO

            ! update velocity to t = t + dt
            !TODO

            ! update accelerations to t = t + dt
            !TODO

            return
        end subroutine update
        
        subroutine update_rk4(dt)
            implicit none
            real, intent(in)  :: dt
            integer :: n
            real    :: x, y, rsq, force, dt2
            real, dimension(4) :: yin1, yin2, ynext1, ynext2

            real,dimension(4) :: k1_1,k2_1,k3_1,k4_1
            real,dimension(4) :: k1_2,k2_2,k3_2,k4_2
            real,dimension(4) :: y2_1,y3_1,y4_1
            real,dimension(4) :: y2_2,y3_2,y4_2
            
            n = 4
            dt2 = dt/2.0

            yin1(1) = stars(1)%x
            yin1(2) = stars(1)%y
            yin1(3) = stars(1)%vx
            yin1(4) = stars(1)%vy

            yin2(1) = stars(2)%x
            yin2(2) = stars(2)%y
            yin2(3) = stars(2)%vx
            yin2(4) = stars(2)%vy

            call myfunc(n, yin1, yin2, k1_1, k1_2)
            y2_1 = yin1 + (dt2*k1_1)
            y2_2 = yin2 + (dt2*k1_2)
            
            call myfunc(n, y2_1, y2_2, k2_1, k2_2)
            y3_1 = yin1 + (dt2*k2_1)
            y3_2 = yin2 + (dt2*k2_2)

            call myfunc(n, y3_1, y3_2, k3_1, k3_2)
            y4_1 = yin1 + (dt*k3_1)
            y4_2 = yin2 + (dt*k3_2)

            call myfunc(n, y4_1, y4_2, k4_1, k4_2)
            
            ynext1 = yin1 + (dt/6.0)*(k1_1 + 2.0*k2_1 + 2.0*k3_1 + k4_1)
            ynext2 = yin2 + (dt/6.0)*(k1_2 + 2.0*k2_2 + 2.0*k3_2 + k4_2)

            stars(1)%x  = ynext1(1)
            stars(1)%y  = ynext1(2)
            stars(1)%vx = ynext1(3)
            stars(1)%vy = ynext1(4)
        
            stars(2)%x  = ynext2(1)
            stars(2)%y  = ynext2(2)
            stars(2)%vx = ynext2(3)
            stars(2)%vy = ynext2(4)

        end subroutine update_rk4        

        subroutine myfunc(n, yin1, yin2, k1, k2)
            use constants, only: G 
            implicit none
            integer, intent(in) :: n
            real, dimension(n), intent(in) :: yin1, yin2 
            real, dimension(n), intent(out):: k1, k2
            real :: rsq, force

            
            rsq = (yin1(1)-yin2(1))**2.0 + (yin1(2)-yin2(2))**2.0
            force = (G*stars(1)%mass*stars(2)%mass)/rsq            
            
            k1(1) = yin1(3) ! vx1
            k1(2) = yin1(4) ! vy1
            k2(1) = yin2(3) ! vx2
            k2(2) = yin2(4) ! vy2

            k1(3) = (force/stars(1)%mass) * (yin2(1)-yin1(1))/(rsq**0.5) ! ax1
            k1(4) = (force/stars(1)%mass) * (yin2(2)-yin1(2))/(rsq**0.5) ! ay1
            k2(3) = (force/stars(2)%mass) * (yin1(1)-yin2(1))/(rsq**0.5) ! ax2
            k2(4) = (force/stars(2)%mass) * (yin1(2)-yin2(2))/(rsq**0.5) ! ay2

        end subroutine myfunc

end module physics

