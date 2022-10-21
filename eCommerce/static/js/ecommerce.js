
      $(document).ready(function(){

        //Contact Form Handler
        var contactForm = $('.contact_form')
        var contactFormMethod = contactForm.attr('method')
        var contactFormEndPoint =contactForm.attr('action')


        function displayingSubmit(submitBtn, defaultText, doSubmit){
          if (doSubmit){
            submitBtn.addClass('disabled')
            submitBtn.html('<i class="fa-solid fa-spinner"></i> Sending...')
            }
          else {
            submitBtn.removeClass('disabled')
            submitBtn.html(defaultText)

          }
        }

        contactForm.submit(function(event){
          event.preventDefault()
          var  contactFormData = contactForm.serialize()

          var contactFormSubmitBtn = contactForm.find("[type='submit']")
          var contactFormSubmitBtnText = contactFormSubmitBtn.text()

          displayingSubmit(contactFormSubmitBtn,'',true)

          $.ajax({
            method: contactFormMethod,
            url: contactFormEndPoint,
            data: contactFormData,


            success: function(data){
              contactForm[0].reset()
              $.alert({
                    title: 'Success',
                    content: data.message,
                    theme: 'modern',
                    })
              setTimeout(displayingSubmit(contactFormSubmitBtn,contactFormSubmitBtnText,false),500)
            },
            error: function(error){
                console.log(error.responseJSON)
                var jsonData = error.responseJSON
                var msg=""
                console.log(jsonData)

                $.each(jsonData, function(key,value){
                  msg += key + ":" + value[0].message + '</br>'
                })

                $.alert({
                    title: 'Oops!',
                    content: msg,
                    theme: 'modern',
                    })
                setTimeout(displayingSubmit(contactFormSubmitBtn,contactFormSubmitBtnText,false),500)

            }



          })
        })



        //Auto  Search

        var searchForm = $('.search-form')
        var searchInput = searchForm.find("[name='q']")
        var typingTimer
        var typingInterval = 500
        var searchBtn = searchForm.find("[type='submit']")

        searchInput.keyup(function(event){
          clearTimeout(typingTimer)
          typingTimer = setTimeout(performSearch, typingInterval)

        })

        searchInput.keydown(function(event){
          clearTimeout(typingTimer)
        })

        function displaySearching(){
          searchBtn.addClass('disabled')
          searchBtn.html('<i class="fa-solid fa-spinner"></i> Search...')
        }
        function performSearch(){
          displaySearching()
          query = searchInput.val()
          setTimeout(window.location.href='/search/?q=' + query,2000)


        }



        //cart + add product
        var productForm  = $('.form-product-ajax')
        productForm.submit(function(event){
            event.preventDefault();
            // console.log('form is not sending')
            var thisForm = $(this)
            var actionEndpoint = thisForm.attr('action');
            var httpMethod = thisForm.attr('method');
            var formData = thisForm.serialize();



            $.ajax({
              url: actionEndpoint,
              method: httpMethod,
              data: formData,
              success: function(data){

                var submitSpan = thisForm.find('.submit-span')
                if (  data.added){

                 submitSpan.html('<button class="btn btn-success" type="submit">Add to cart</button>')
                }

                var navbarCount = $(".Navbar-cart-count")
                navbarCount.text(data.cartItemCount)
                var currentPath = window.location.href
                if (currentPath.indexOf('cart')!=-1) {
                  refreshCart()
                }

              },


              error: function(errorData){

                $.alert({
                    title: 'Oops!',
                    content: 'An error occurred',
                    theme: 'modern',
                });
                console.log('error')
                console.log(errorData)
              }



            })

        })

        function refreshCart(){
          console.log('in current cart')
          var cartTable = $('.cart-table')
          var cartBody = cartTable.find('.cart-body')
          // cartBody.html('<h1>Changed</h1>')
          var productRows = $('.cart-products')
          var currentUrl = window.location.href

          var cartSubtotal = cartBody.find('.cart-subtotal')
          var cartTotal = cartBody.find('.cart-total')


          var refreshCartUrl = '/api/cart/'
          var refreshCartMethod = 'GET';
          var data;
          $.ajax({
            url: refreshCartUrl,
            method: refreshCartMethod,
            data: data,
            productRows:productRows,


            success: function(data){
              console.log('success')
              console.log(data)

              var hiddenCartItemRemoveForm =$(".cart-item-remove-form")

              if (data.products.length>0) {
                productRows.html('')
                i = data.products.length
                $.each(data.products, function(index,value){

                     var newCartItemRemove = hiddenCartItemRemoveForm.clone()
                     newCartItemRemove.css('display','block')
                     newCartItemRemove.find('.cart-item-product-id').val(value.id)

                      cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + value.name + "</a>" + newCartItemRemove.html() + "</td><td>" + value.price + "</td></tr>")
                      i--


                })



                cartSubtotal.text(data.subtotal)
                cartTotal.text(data.total)
                }
               else{
                window.location.href = currentUrl
               }

            },
            error: function(errorData){
               $.alert({
                    title: 'Oops!',
                    content: 'An error occurred',
                    theme: 'modern',
                    })

              console.log(errorData)
            }
          })

        }


      })
