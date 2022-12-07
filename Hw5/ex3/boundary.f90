subroutine boundary(v)
    !
    ! apply BC on array v
    !
    use Simulation_data
    implicit none
    real, dimension(istart-ibuf:iend+ibuf, istart-ibuf:iend+ibuf), intent(inout) :: v
    integer :: i, j


    ! apply boundary condition

    ! left boundary (period)



    do j = 1, iend
        do i = 1, ibuf
            v(istart-i, j) = v(iend, j)
        enddo
    enddo
    ! right boundary (period)
    do j = 1, iend
        do i = 1, ibuf
            v(iend+i, j) = v(istart, j)
        enddo
    enddo

    do i = 1, iend
        do j = 1, ibuf
            v(i, jstart-j) = v(i, jend)
        enddo
    enddo
    ! right boundary (period)
    do i = 1, iend
        do j = 1, ibuf
            v(i, jend+j) = v(i, jstart)
        enddo
    enddo

end subroutine boundary
