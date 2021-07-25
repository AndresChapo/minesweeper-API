const jsonx = document.getElementById('jsonx');
const superboard = document.getElementById('superboard');
const boxes = Array.from(document.getElementsByClassName('box'));
const statusText = document.getElementById('statusText');

// Grid content:
var full_grid;
var id_game = 0;
var sizes = 0;
var mines_cuantities = 0;
var grid = [];
var flags = [];
var swept = [];
var game_status = 0;

const spaces = [null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null];

// OK - grid variables 
// func contruya visible grid
// func que resete el grid
// css decorar boxes basico
// func que actualiza
// func nuevo juego
// func retomar juego
// func que informa status del juego

const drawEmptyBoard = (sizes) => {
    //boxes.forEach((box, index) =>{
    for (var i = 0; i < (sizes*sizes); i++) {
        //let styleString = '';
        //if (index > 5){
        //    styleString += 'border-top: 3px solid red;';
        //}
        //box.style = styleString;
       // box.addEventListener('click',boxClicked);
       //1,1 = 6 (size * x) + y
       //SIZE 5x5 = 25

        boxes[i] = document.createElement("div");
        boxes[i].id = i;
        boxes[i].className = "box";
        superboard.insertAdjacentElement("beforeend", boxes[i]);
    }
    if (sizes == 500){// 5
    superboard.style = 'width: 125px;'
    }

    superboard.style = 'width: '+(sizes*25)+'px;'

};

const getGrid = (id) => {
    fetch('/grids/'+id, { method: 'GET'})
    .then(response => response.json())
    .then(data => full_grid = showData(data))
    .catch(function (error) {
        console.error("Error with JSON");
        console.error(error);
    }) 

};

const showData = (data) => {
    console.log(data);

    id_game = data[0].id_game;
    sizes = data[0].sizes;
    mines_cuantities = data[0].mines_cuantities;
    grid = JSON.parse(data[0].grid);
    flags = JSON.parse(data[0].flags);
    swept = JSON.parse(data[0].swept);
    game_status = data[0].game_status;
    

    console.log("id_game: "+id_game);
    console.log("sizes: "+sizes);
    console.log("mines_cuantities: "+mines_cuantities);
    console.log("grid: ",grid);
    console.log("flags: ",flags);
    console.log("swept: ",swept);
    console.log("game_status: "+game_status);

    swept.forEach((sweptx, index) =>{
        pos = coordenates_to_id(sizes, sweptx[0],sweptx[1]);
        score = grid[sweptx[0]][sweptx[1]];
        boxes[pos].style = 'background-color: var(--emptyColor);';
        if (score != 0){
            boxes[pos].innerText = score;
        }
    });
    //jsonx.innerText = grid;
    return data;
};

const coordenates_to_id = (size, x, y) => {
    //1,1 = 6 = (size * x) + y
    return (size * x) + y;
};

getGrid(12);
drawEmptyBoard(10);


console.log('full_grid: ',full_grid);
