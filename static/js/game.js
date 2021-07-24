const jsonx = document.getElementById('jsonx');

const boxes = Array.from(document.getElementsByClassName('box'));
const statusText = document.getElementById('statusText');

// Grid content:
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


const getGrid = (id) => {
    fetch('/grids/'+id, { method: 'GET'})
    .then(response => response.json())
    .then(data => {
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

        jsonx.innerText = grid;
    }).catch(function (error) {
        console.error("Error with JSON");
        console.error(error);
    }) 

};



getGrid(1);


