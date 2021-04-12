 function addorremove(id) {
    if (id){
      var wishlist= $('#jobwl'+id).data('wl');
      if(wishlist == 0){
      $.ajax({
        url:"users/wishlist-add/" +id,
        method:"GET",
        success:function () {
          $('#jobwl'+ id).removeClass('btn-primary').addClass('btn-danger')
              const Toast = Swal.mixin({
              toast: true,
              position: 'top',
              showConfirmButton: true,
              timer: 3000,
              timerProgressBar: true,
              didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
              }
            })

            Toast.fire({
              icon: 'success',
              title: 'Job added to wish list!'
            })
            $('#jobwl'+id).data('wl',1);
        }
      })
    }else{
     $.ajax({
        url:"users/wishlist-remove/" +id,
        method:"GET",
        success:function () {
          $('#jobwl'+ id).removeClass('btn-danger').addClass('btn-primary')
              const Toast = Swal.mixin({
              toast: true,
              position: 'top',
              showConfirmButton: true,
              timer: 3000,
              timerProgressBar: true,
              didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
              }
            })

            Toast.fire({
              icon: 'error',
              title: 'Job removed from list!'
            })
            $('#jobwl'+id).data('wl',0);
        }
      })
    }
    }
  }