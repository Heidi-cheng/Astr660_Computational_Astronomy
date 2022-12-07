subroutine boundary(v)
    !
    ! apply BC on array v
    !
    use Simulation_data
    implicit none
    real, dimension(istart-ibuf:iend+ibuf), intent(inout) :: v
    integer :: i

    ! apply boundary condition

    ! TODO: implement periodic BC for left boundary 
    

    v(istart-ibuf) = v(iend)
    v(iend+ibuf) = v(istart)



    ! TODO: implement periodic BC for right boundary 


end subroutine boundary
