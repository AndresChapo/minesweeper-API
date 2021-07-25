const div_id_game = document.getElementById('id_game');
const superboard = document.getElementById('superboard');
const boxes = Array.from(document.getElementsByClassName('box'));
const statusText = document.getElementById('statusText');

// otra opcion era haccer full_grid.push() 
// Grid content:

class GridGame {
    id_game = 0;
    sizes = 0;
    mines_cuantities = 0;
    grid = [];
    flags = [];
    swept = [];
    game_status = 0;

    constructor() {}
    async importGrid(data){
        this.id_game = data.id_game;
        this.sizes = data.sizes;
        this.mines_cuantities = data.mines_cuantities;
        this.grid = JSON.parse(data.grid);
        this.flags = JSON.parse(data.flags);
        this.swept = JSON.parse(data.swept);
        this.game_status = data.game_status;
    }
    insertData(id_game, sizes,mines_cuantities,grid, flags, swept,game_status) {
        this.id_game = id_game;
        this.sizes = sizes;
        this.mines_cuantities = mines_cuantities;
        this.grid = grid;
        this.flags = flags;
        this.swept = swept;
        this.game_status = game_status;
    }
    get id_game(){
        return this.id_game;
    }
};
let currentGame = new GridGame();


// OK - grid variables 
// OK - func contruya visible grid
// func que resete el grid
// css decorar boxes basico
// func que actualiza
// func nuevo juego
// func retomar juego
// func que informa status del juego

const drawEmptyBoard = (sizes) => {
    if(boxes.length > 0){
        console.log("boxes.length: ",boxes.length);
        boxes.forEach((box, index) =>{
            box.style = 'background-color: var(--backColor);';
            box.innerText = '';
        });
    }else{
        for (var i = 0; i < (sizes*sizes); i++) {
        
            boxes[i] = document.createElement("div");
            boxes[i].id = i;
            boxes[i].className = "box";
            superboard.insertAdjacentElement("beforeend", boxes[i]);
            boxes[i].addEventListener('click',boxClicked);
        }
        superboard.style = 'width: '+(sizes*25)+'px;';
    }

};

const getGrid = (id) => {
    fetch('/grids/'+id, { method: 'GET'})
    .then(response => response.json())
    .then(data =>     showData(data[0]))
    .catch(function (error) {
        console.error("Error with JSON");
        console.error(error);
    });
};

const updateGame = (grid_id,row,column,flag) => {
    fetch('/game/play/'+grid_id+'/'+row+'/'+column+'/'+flag, { method: 'PUT'})
    .then(response => response.json())
    .then(data => showData(data))
    .catch(function (error) {
        console.error("Error with JSON");
        console.error(error);
    });
};

const showData = (data) => {
//    console.log(data);
    currentGame.importGrid(data)
/*
    id_game = data[0].id_game;
    sizes = data[0].sizes;
    mines_cuantities = data[0].mines_cuantities;
    grid = JSON.parse(data[0].grid);
    flags = JSON.parse(data[0].flags);
    swept = JSON.parse(data[0].swept);
    game_status = data[0].game_status;
*/  

    console.log("id_game: "+currentGame.id_game);
    console.log("sizes: "+currentGame.sizes);
    console.log("mines_cuantities: "+currentGame.mines_cuantities);
    console.log("grid: ",currentGame.grid);
    console.log("flags: ",currentGame.flags);
    console.log("swept: ",currentGame.swept);
    console.log("game_status: "+currentGame.game_status);

    div_id_game.innerText = 'Game N#: ' + currentGame.id_game;
    drawEmptyBoard(currentGame.sizes);
    print_flags(currentGame.sizes, currentGame.flags);
    print_swepts(currentGame.sizes,currentGame.swept, currentGame.grid);


};

const print_swepts = (sizes, swept, grid) => {
    swept.forEach((sweptx, index) =>{
        pos = coordenates_to_id(sizes, sweptx[0],sweptx[1]);
        score = grid[sweptx[0]][sweptx[1]];
        boxes[pos].style = 'background-color: var(--emptyColor);';
        if (score != 0){
            boxes[pos].innerText = score;
        }else{
            boxes[pos].innerText = '';
        }
    })
};

const print_flags = (sizes, flags) => {
    flags.forEach((flagx, index) =>{
        pos = coordenates_to_id(sizes, flagx[0],flagx[1]);
        boxes[pos].style = 'background-color: var(--emptyColor);';
        boxes[pos].innerText = '?';
    })
};

const coordenates_to_id = (size, x, y) => {
    //1,1 = 6 = (size * x) + y
    return (size * x) + y;
};

const id_box_to_coordinates = (size, id) => {
    var x = (id%size);
    var y = parseInt(id/size);
    console.log("id_box_to_coordinates- X: ",x);
    console.log("id_box_to_coordinates- Y: ",y);
    return x, y;
};

const boxClicked = (x) => {
    console.log(x.target.id);
    id_box_to_coordinates(10,x.target.id);
//    updateGame(div_id_game.innerText,1,9,1);

};

const restart = () => {
    console.log("currentGame.id_game: ", currentGame.id_game);
    console.log("currentGame.grid: ", currentGame.grid);
};

restartBtn.addEventListener('click', restart);


getGrid(12);
//showData(currentGame);

