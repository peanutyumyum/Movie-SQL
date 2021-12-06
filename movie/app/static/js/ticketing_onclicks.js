let is_requested = false;
let context = new Object();

function movie_onClick() {
    console.log("movie click");
    if(!is_requested || !context.movie_name) {
        context.movie_name = event.target.value;
        is_requested = context.movie_name ? true : false;
        let theater_list = document.getElementById("theater_list");
        while(theater_list.hasChildNodes()) {
            theater_list.removeChild(theater_list.firstChild);
        }
        let pk = event.target.id;
        $.ajax({
            method: "GET",
            url: './ticketing',
            data: { 
                'movie_id': pk,
                // 'csrfmiddlewaretoken': '{{ csrf_token }}',
            },
            dataType: "json",
        })
        .done(res => {
            console.log(context);
            console.log(JSON.stringify(context));
            let theaters = res.theaters;
            console.log("theaters:"+theaters);
            theaters.forEach(theater => {
                let new_input = document.createElement('input');
                new_input.setAttribute("id", theater);
                new_input.setAttribute("type", 'radio');
                new_input.setAttribute("value", theater);
                new_input.setAttribute("class", 'theater_city');
                new_input.setAttribute("name", 'theater_city');
                new_input.onclick = theaterCity_onClick();

                let new_label = document.createElement('label');
                new_label.setAttribute("for", theater);
                new_label.appendChild(document.createTextNode(theater));

                document.getElementById("theater_list").appendChild(new_input);
                document.getElementById("theater_list").appendChild(new_label);
                // $('#theater_list').append(new_radio);
            });   
        })
        .fail((xhr, status, errorThrown) => {
            alert("오류가 발생했습니다: " + errorThrown);
        })
    }
}

function theaterCity_onClick() {
    if(is_requested && !context.movie_city) {
        console.log("is_requested false");
        is_requested = false;
    }
    if(!is_requested || !context.movie_city) {
        let movie_city = event.target.value;
        // let movie_city = $(this).val();
        console.log("movie_city: "+movie_city);
        context.movie_city = movie_city;
        is_requested = context.movie_city ? true : false;
        let branch_list = document.getElementById("branch_list");
        while(branch_list.hasChildNodes()) {
            branch_list.removeChild(branch_list.firstChild);
        }
        // $('#branch_list').empty();
        $.ajax({
            method: "GET",
            url: './ticketing',
            data: { 
                'movie_city': movie_city,
                // 'csrfmiddlewaretoken': '{{ csrf_token }}',
            },
            dataType: "json",
        })
        .done(res => {
            let branch_names = res.branch_names;
            branch_names.forEach(branch_name => {
                let new_input = document.createElement('input');
                new_input.setAttribute("id", branch_name);
                new_input.setAttribute("type", 'radio');
                new_input.setAttribute("value", branch_name);
                new_input.setAttribute("class", 'theater_branch');
                new_input.setAttribute("name", 'theater_branch');
                

                let new_label = document.createElement('label');
                new_label.setAttribute("for", branch_name);
                new_label.appendChild(document.createTextNode(branch_name));

                document.getElementById("branch_list").appendChild(new_input);
                document.getElementById("branch_list").appendChild(new_label);
                // $('#branch_list').append(new_radio);
            });
        })
        .fail((xhr, status, errorThrown) => {
            alert("오류가 발생했습니다: " + errorThrown);
        });
    }
}