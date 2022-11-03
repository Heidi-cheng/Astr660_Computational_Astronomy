module Solver 

    implicit none
    contains

    subroutine rk2(n, yin, ynext, t, h, func)
        implicit none
        integer, intent(in) :: n      ! number of ODEs
        real, intent(in)    :: t, h
        real, dimension(n), intent(in)  :: yin
        real, dimension(n), intent(out)  :: ynext
        external      :: func
        integer            :: i
        real, dimension(n) :: k, k1, k2
        real,dimension(n)  :: y2

        

        do i = 1, n
        call func(n, t, yin, k)
        !compute k1 = func(t, yin)
        k1(i) = k(i)
        ! compute y2 = yin + h*k1
        y2 = yin + h*k1
        ! compute k2 = func(t+h, y2)
        call func(n, t+h, y2, k)
        k2(i) = k(i)
        ! compute ynext
        ynext(i) = yin(i) + 0.5*h*(k1(i) + k2(i))
        enddo


        return
    end subroutine rk2

end module Solver
