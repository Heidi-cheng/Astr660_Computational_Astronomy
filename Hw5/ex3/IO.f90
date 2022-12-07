module IO
    implicit none
    contains
        subroutine output(n,time)
            use Simulation_data
            implicit none
            integer, intent(in) :: n
            real, intent(in)    :: time

            integer      :: i, j
            character(7) :: cycstr
            character(58)      :: filename

            real         :: ua ! analytical solution
            real         :: pax, pix, pex
            real         :: pay, piy, pey
            
            write(cycstr,10) n,'.d'
10  format(i5,a2)

            ! fill remaing zeros
            do i=1,5
                if(cycstr(i:i).eq.' ') cycstr(i:i)='0'
            enddo

            filename = 'advection2d_'//cycstr
            open(100,file=filename,status='unknown')

            ! write header
            write(100,29) "# i", "j", "x", "y", "U(x, y)", "UA(x, y)"

            pax = 0.15 + cx * time
            pix = pax-0.05
            pex = pax+0.05
            pay = 0.15 + cy * time
            piy = pay-0.05
            pey = pay+0.05

            do i=1,iend
                if ((x(i) .ge. pix) .and. (x(i) .le. pex)) then
                    if ((y(i) .ge. piy) .and. (y(i) .le. pey)) then
                        ua = 1.0
                    else 
                        ua = 0.01
                    endif
                else
                    ua = 0.01
                endif

                do j = 1, jend
                    write(100,30) i, j, x(i), y(j), u(i ,j), ua
                enddo
            enddo
            



29 format(2a6,4a24)
30 format(2i6,4e24.12E4)

            close(100)
            return
        end subroutine output

end module IO
