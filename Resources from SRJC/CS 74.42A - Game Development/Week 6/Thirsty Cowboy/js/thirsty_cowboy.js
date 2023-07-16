
var game = new Phaser.Game(
  800, 600, Phaser.CANVAS, 'phaser-example',
  { preload: preload, create: create, update: update, render: render }
);

function preload() {

    game.load.tilemap('level1', 'assets/json/level1.json', null, Phaser.Tilemap.TILED_JSON );
    game.load.image('tiles-1', 'assets/images/tiles-1.png' );

    game.load.spritesheet( 'cowboy', 'assets/images/Cowboy-sprite.png', 30, 42 );

    game.load.image( 'beer', 'assets/images/beerBottle-verticle_sprite_small.png' );
    game.load.image( 'whiskey', 'assets/images/whiskey-sprite_small.png' );
    game.load.image( 'background', 'assets/images/desert-background.png' );

    game.load.audio( 'music', 'assets/audio/spagetti_western.ogg' );
    game.load.audio( 'slurp', 'assets/audio/slurping.wav' );

}

var map;
var tileset;
var layer;
var cowboy;
var cursors;
var bg;
var score = 0;

function create() {

    game.physics.startSystem(Phaser.Physics.ARCADE);

    game.stage.backgroundColor = '#000000';

    bg = game.add.tileSprite(0, 0, 800, 600, 'background');
    bg.fixedToCamera = true;

    map = game.add.tilemap('level1');

    map.addTilesetImage('tiles-1');

    map.setCollisionByExclusion( [ 13, 14, 15, 16, 46, 47, 48, 49, 50, 51 ] );

    layer = map.createLayer('Tile Layer 1');

    //  Un-comment this on to see the collision tiles
    // layer.debug = true;

    layer.resizeWorld();

    game.physics.arcade.gravity.y = 250;

    cowboy = game.add.sprite( 42, 30, 'cowboy' );
    game.physics.enable( cowboy, Phaser.Physics.ARCADE );

    cowboy.body.bounce.y = 0.2;
    cowboy.body.collideWorldBounds = true;

    cowboy.animations.add( 'standing', [ 4 ], 10, true );
    cowboy.animations.add( 'walking_left', [ 0, 1, 2, 3 ], 10, true );
    cowboy.animations.add( 'walking_right', [ 5, 6, 7, 8 ], 10, true );
    cowboy.animations.add( 'jump', [ 9 ], 10, true );

    game.camera.follow(cowboy);

    cursors = game.input.keyboard.createCursorKeys();

    // Game Music
    music = game.add.audio( 'music' );
    music.play();

    beers = game.add.group();
    beers.enableBody = true;
    whiskeys = game.add.group();
    whiskeys.enableBody = true;
    slurp = game.add.audio( 'slurp' );

    // Create collectables across the map with slight variance each time.
    var index = Math.floor( Math.random() * 10 ) + 5;
    for( var i = 0; i < index; i++ )
    {
        var beer = beers.create( game.world.randomX, game.world.randomY, 'beer' );
        var whiskey = whiskeys.create( game.world.randomX, game.world.randomY, 'whiskey' );
    }

}

function update() {

    game.physics.arcade.collide( cowboy, layer );
    game.physics.arcade.collide( beers, layer );
    game.physics.arcade.collide( whiskeys, layer );

    game.physics.arcade.overlap( cowboy, beers, collectBeer, null, this);
    game.physics.arcade.overlap( cowboy, whiskeys, collectWhiskey, null, this);

    cowboy.body.velocity.x = 0;

    if( cursors.left.isDown )
    {
        cowboy.body.velocity.x = -150;
        cowboy.animations.play( "walking_left" );
        //cowboy.scale.x = -1;
    }
    else if( cursors.right.isDown )
    {
        cowboy.body.velocity.x = 150;
        cowboy.animations.play( "walking_right" );
        //cowboy.scale.x = 1;
    }
    else {
      cowboy.animations.play( "standing" );
    }

    if ( cursors.up.isDown && cowboy.body.onFloor() )
    {
        cowboy.body.velocity.y = -250;
        cowboy.animations.play( "jump" );

        if( cowboy.body.onFloor() )
        {
          cowboy.animations.play( "jump" );
        }
    }

    function collectBeer( cowboy_Object, beer_Object )
    {
      beer_Object.kill();
      slurp.play();
      score = score + 1;
    }

    function collectWhiskey( cowboy_Object, whiskey_Object )
    {
      whiskey_Object.kill();
      slurp.play();
      score = score + 5;
    }

}

function render () {

  game.debug.text('Score: ' + score, 32, 32);

}
