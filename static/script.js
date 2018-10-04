function startDining(actions){

    $("#start").hide()

    let container = $(".container-fluid")

    container.append(`

        <div class="philosopher0">
            <div id="0" class="d-flex p0">
                <img class="img-food" src="../static/css/food.png" />
                <h1 >platao</h1>
            </div>
        </div>

        <div class="philosopher1-2">

            <div id="1" class="d-flex p1">
                <h1>socrates</h1>
                <img class="img-food" src="../static/css/food.png" />
            </div>

            <div id="2" class="d-flex p2">
                <img class="img-food" src="../static/css/food.png" />
                <h1>aristoteles</h1>
            </div>

        </div>

        <div class="philosopher3-4">

            <div id="3" class="d-flex p3">
                <h1>nietzsche</h1>
                <img class="img-food" src="../static/css/food.png" />
            </div>

            <div id="4" class="d-flex p4">
                <img class="img-food" src="../static/css/food.png" />
                <h1>kant</h1>
            </div>

        </div>

    `)

    var i = 0

    console.log(actions)

    while(i < actions.length){
        (function(i) {
          setTimeout(function() {
            action = actions[i]

            philosopher_id = action.split("-")[0]
            philosopher_action = action.split("-")[1]
            philosopher_food = action.split("-")[2]

            switch(philosopher_food){
                case '2':
                    philosopher_food = "food"
                    break
                case '1':
                    philosopher_food = "half-food"
                    break
                case '0':
                    philosopher_food = "no-food"
                    break
            }

            switch(philosopher_action){
                case 'eating':
                    philosopher_action = "eating"
                    break
                case 'hungry':
                    philosopher_action = "hungry"
                    break
                default:
                    philosopher_action = philosopher_action
                    break
            }

            switch(philosopher_id){
                case '0':
                    $("#0").html(`<img class="img-food" src="../static/css/${philosopher_food}.png" /><h1 class="${philosopher_action}">platao ${philosopher_action}</h1>`)
                    break
                case '1':
                    $("#1").html(`<h1 class="${philosopher_action}">socrates ${philosopher_action}</h1><img class="img-food" src="../static/css/${philosopher_food}.png" />`)
                    break
                case '2':
                    $("#2").html(`<img class="img-food" src="../static/css/${philosopher_food}.png" /><h1 class="${philosopher_action}">aristoteles ${philosopher_action}</h1>`)
                    break
                case '3':
                    $("#3").html(`<h1 class="${philosopher_action}">nietzsche ${philosopher_action}</h1><img class="img-food" src="../static/css/${philosopher_food}.png" />`)
                    break
                case '4':
                    $("#4").html(`<img class="img-food" src="../static/css/${philosopher_food}.png" /><h1 class="${philosopher_action}">kant ${philosopher_action}</h1>`)
                    break

            }
          }, 1000 * i )
       })(i++)
    }

}

