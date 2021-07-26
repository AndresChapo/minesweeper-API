const div_id_game = document.getElementById('id_game');
const superboard = document.getElementById('superboard');
var boxes = Array.from(document.getElementsByClassName('box'));
const statusText = document.getElementById('statusText');
const flag_onBtn = document.getElementById('flag_onBtn');
const txtSize = document.getElementById('txtSize');
const txtMines = document.getElementById('txtMines');
const txtGame_id = document.getElementById('txtGame_id');
const resume_gameBtn = document.getElementById('resume_gameBtn');
const new_gameBtn = document.getElementById('new_gameBtn');


// OK - documented RESTful API
// OK - validar func retomar juego
// - CSS mas lindo
// - Mensajes de error
// - Time tracking


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

const getGridAPI = (id) => {
    fetch('/grids/'+id, { method: 'GET'})
    .then(response => response.json())
    .then(data =>     showData(data[0]))
    .catch(function (error) {
        console.error("Error with JSON");
        console.error(error);
    });
};

const updateGameAPI = (grid_id,row,column,flag) => {
    fetch('/game/play/'+grid_id+'/'+row+'/'+column+'/'+flag, { method: 'PUT'})
    .then(response => response.json())
    .then(data => showData(data[0]))
    .catch(function (error) {
        console.error("Error with JSON");
        console.error(error);
    });
};

const newGameAPI = (sizes,mines) => {
    fetch('/game/new/'+sizes+'/'+mines, { method: 'GET'})
    .then(response => response.json())
    .then(data => showData(data[0]))
    .catch(function (error) {
        console.error("Error with JSON");
        console.error(error);
    });
};

const showData = (data) => {
//    console.log(data);
    currentGame.importGrid(data);

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
    check_if_player_won(currentGame.game_status);
};

const print_swepts = (sizes, swept, grid) => {
    swept.forEach((sweptx, index) =>{
        pos = coordenates_to_id(sizes, sweptx[0],sweptx[1]);
        score = grid[sweptx[0]][sweptx[1]];
        boxes[pos].style = 'background-color: var(--emptyColor);';
        if (score == 0){
            boxes[pos].innerText = '';
        }else if(score == 9){
            boxes[pos].innerText = 'x';
        }else{
            boxes[pos].innerText = score;
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

const coordenates_to_id = (size, row, column) => {
    //1,1 = 6 = (size * x) + y
    return (size * row) + column;
};

const id_box_to_coordinates = (size, id) => {
    var click_on = [];
    click_on.push(parseInt(id/size));
    click_on.push(id%size);
    return click_on;
};

const boxClicked = (e) => {
    console.log(e.target.id);
    if(currentGame.game_status==1){
        var click_on = id_box_to_coordinates(currentGame.sizes,e.target.id);

        if(flag_onBtn.innerText == "Flag OFF"){
            updateGameAPI(currentGame.id_game,click_on[0],click_on[1],0);
        }else{
            updateGameAPI(currentGame.id_game,click_on[0],click_on[1],1);
        }
    }
};

const deleteBoard = () => {
    boxes.forEach((box, index) =>{
        box.remove();
    });
    boxes = Array.from(document.getElementsByClassName('box'));
};

const new_gameClick = () => {
    var max_mines_allowed = (txtSize.value * txtSize.value)/2;
    if(txtSize.value > 4 && txtSize.value < 26){
        if(txtMines.value > 0 && txtMines.value <= max_mines_allowed){
    //    new_game_flag = true;
            deleteBoard();
            newGameAPI(txtSize.value,txtMines.value);
            txtSize.value = '';
            txtMines.value = '';
        }else{
            console.log("The minimum of mines is 1, the maximum for this size is:"+ parseInt(max_mines_allowed));
        }
    }else{
        console.log("The minimun size is 5, the maximum is 100")
    }
};

const flagClick = () => {
    if(flag_onBtn.innerText == "Flag OFF"){
        flag_onBtn.innerText = "Flag ON";
    }else{
        flag_onBtn.innerText = "Flag OFF";
    }
};
const resume_gameClick = () => {
    if(txtGame_id.value  > 0){
        deleteBoard();
        getGridAPI(txtGame_id.value);
    }else{
        console.log("The minimun has to be 1")
    }
};
const check_if_player_won = (status) => {
    if(status == 0){
        statusText.innerText = "You lose!";
    }else if(status == 1){
        statusText.innerText = "Game ON!";
    }else if(status == 2){
        statusText.innerText = "You Win!";
    }
};

new_gameBtn.addEventListener('click', new_gameClick);
flag_onBtn.addEventListener('click', flagClick);
resume_gameBtn.addEventListener('click', resume_gameClick);


