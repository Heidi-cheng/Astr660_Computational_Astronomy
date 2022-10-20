!
! National Tsing Hua University
!
! ASTR 660 Computational Astrophysics
!
! Created:  Kuo-Chuan Pan 2020
! Modified: Karen Yang 2022.10.15
!
! Problem:
!
!        Solving non-linear equations
!
program linear
    use linalg
    implicit none
    integer, parameter  :: N = 3
    real,dimension(N,N) :: lower, upper, A, P, Ainv
    real,dimension(N) :: bl
    real,dimension(N) :: bu
    real,dimension(N) :: xl
    real,dimension(N) :: xu
    real,dimension(4,4) :: aa,ll,uu,pp
    integer :: i,j

    ! lower triangle
    lower(1,1) = -1.0
    lower(1,2) =  0.0
    lower(1,3) =  0.0

    lower(2,1) = -6.0
    lower(2,2) = -4.0
    lower(2,3) =  0.0

    lower(3,1) =  1.0
    lower(3,2) =  2.0
    lower(3,3) =  2.0
        
    ! upper triangle
    upper(1,1) =  1.0
    upper(1,2) =  2.0
    upper(1,3) =  2.0

    upper(2,1) =  0.0
    upper(2,2) = -4.0
    upper(2,3) = -6.0

    upper(3,1) =  0.0
    upper(3,2) =  0.0
    upper(3,3) = -1.0

    ! the vectore b for solving the lower matrix
    bl(1) =  1.0
    bl(2) = -6.0
    bl(3) =  3.0

    ! the vector b for solving the upper matrix
    bu(1) =  3.0
    bu(2) = -6.0
    bu(3) =  1.0

    call solve_lower_triangular_matrix(N,lower,bl,xl)
    call solve_upper_triangular_matrix(N, upper, bu, xu)
    call mat_print("L",lower)
    call mat_print("U",upper)
    print *, "vector   b_lower = ",bl
    print *, "solution x_lower = ",xl
    print *, "vector   b_upper = ",bu
    print *, "solution x_upper = ",xu
    
end program linear 


