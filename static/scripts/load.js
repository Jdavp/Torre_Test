$(document).ready(function () {
    $('button').on('click', function () {
      $('#userinfo').html("")
      $('#listofmatches').html("")
      $('#same_utc').html("")
        $.ajax({
            type: 'GET',
            url: '/main_user/' + $('input').val(),
            dataType:"json",
            success: function (data) {
              console.log(data)
              let content = ''
                content += '<img src="' + data.photo + '" style=width:auto;>'
                content += '<h2>' + data.name + '</h2>'
                content += '<p id="user_tz">' + data.timezone +'</p>'
                $('#userinfo').html(content)
              data_table(data.timezone)
            }
        });
        // $.ajax({
        //     type: 'GET',
        //     url: '/same_utc/',
        //     dataType:"json",
        //     success: function (data) {
        //       var content = ''
        //       // for (let i = 0; i < data.length; i++) {
        //       //   content += '<div class="card col-4">'
        //       //   content += '<div class="card-body" >'
        //       //   content += '<img src="' + data[i].photo + '" style="height:14%" width="100%" max-width="600px" >'
        //       //   content += '<h4 class="card-title">' + data[i].name + '</h4>'
        //       //   content += '<h6 class="text-muted card-subtitle mb-2">' +data[i].id + '</h6>'
        //       //   content += '<p class="card-text">' +data[i].strengths + '</p>'
        //       //   content += '</div>'
        //       //   content += '</div>'
        //       // }
        //       $('#same_utc').html(content)
        //     }
        //   });

      console.log('Done!!!!');
    });
  });

  function data_table(timezone) {
    $.ajax({
            type: 'GET',
            url: '/same_utc/?timezone=' + timezone,
            dataType:"html",
            success: function (data) {
              $('#same_utc').html(data)
            }
          });
  }
