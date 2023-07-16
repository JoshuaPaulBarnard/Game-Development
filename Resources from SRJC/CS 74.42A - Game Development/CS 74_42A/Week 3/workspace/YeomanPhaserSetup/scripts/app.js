(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
/* global Phaser */
"use strict";

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

var _statesBootJs = require("./states/Boot.js");

var _statesBootJs2 = _interopRequireDefault(_statesBootJs);

var _statesPreloadJs = require("./states/Preload.js");

var _statesPreloadJs2 = _interopRequireDefault(_statesPreloadJs);

var _statesGameJs = require("./states/Game.js");

var _statesGameJs2 = _interopRequireDefault(_statesGameJs);

var game;

window.onload = function () {
  game = new Phaser.Game(800, 600, Phaser.AUTO, 'game');
  game.state.add('boot', _statesBootJs2["default"]);
  game.state.add('preload', _statesPreloadJs2["default"]);
  game.state.add('game', _statesGameJs2["default"]);
  game.state.start('boot');
};

},{"./states/Boot.js":2,"./states/Game.js":3,"./states/Preload.js":4}],2:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, '__esModule', {
  value: true
});

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ('value' in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError('Cannot call a class as a function'); } }

var Boot = (function () {
  function Boot() {
    _classCallCheck(this, Boot);
  }

  _createClass(Boot, [{
    key: 'preload',
    value: function preload() {
      // the preload method
      this.load.image('preloader', 'assets/images/loading_bar.png');
    }
  }, {
    key: 'create',
    value: function create() {
      this.game.input.maxPointers = 1;
      this.game.state.start('preload');
    }
  }]);

  return Boot;
})();

exports['default'] = Boot;
module.exports = exports['default'];

},{}],3:[function(require,module,exports){
//require other components

"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

var _get = function get(_x, _x2, _x3) { var _again = true; _function: while (_again) { var object = _x, property = _x2, receiver = _x3; _again = false; if (object === null) object = Function.prototype; var desc = Object.getOwnPropertyDescriptor(object, property); if (desc === undefined) { var parent = Object.getPrototypeOf(object); if (parent === null) { return undefined; } else { _x = parent; _x2 = property; _x3 = receiver; _again = true; desc = parent = undefined; continue _function; } } else if ("value" in desc) { return desc.value; } else { var getter = desc.get; if (getter === undefined) { return undefined; } return getter.call(receiver); } } };

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Game = (function (_Phaser$State) {
  _inherits(Game, _Phaser$State);

  function Game() {
    _classCallCheck(this, Game);

    //object level properties
    _get(Object.getPrototypeOf(Game.prototype), "constructor", this).call(this);
  }

  _createClass(Game, [{
    key: "create",
    value: function create() {}
  }, {
    key: "update",
    value: function update() {}
  }]);

  return Game;
})(Phaser.State);

exports["default"] = Game;
module.exports = exports["default"];

},{}],4:[function(require,module,exports){
'use strict';

Object.defineProperty(exports, '__esModule', {
  value: true
});

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ('value' in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError('Cannot call a class as a function'); } }

var Preload = (function () {
  function Preload() {
    _classCallCheck(this, Preload);

    this.asset = null;
    this.ready = false;
  }

  _createClass(Preload, [{
    key: 'preload',
    value: function preload() {
      this.load.image('loading_bg', 'assets/images/loading_bg.jpg');
    }
  }, {
    key: 'create',
    value: function create() {

      //background for game
      this.add.sprite(0, 0, "loading_bg");

      this.asset = this.add.sprite(this.game.width / 2, this.game.height / 2, 'preloader');
      this.asset.anchor.setTo(0.5, 0.5);

      this.load.onLoadComplete.addOnce(this.onLoadComplete, this);
      this.load.setPreloadSprite(this.asset);

      //do all your loading here
      //this.load.image('player', 'assets/images/player.png'); //width and height of sprite

      //staaaart load
      this.load.start();
    }
  }, {
    key: 'update',
    value: function update() {

      if (this.ready) {
        this.game.state.start('game');
      }
    }
  }, {
    key: 'onLoadComplete',
    value: function onLoadComplete() {
      this.ready = true;
    }
  }]);

  return Preload;
})();

exports['default'] = Preload;
module.exports = exports['default'];

},{}]},{},[1])
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIm5vZGVfbW9kdWxlcy9icm93c2VyLXBhY2svX3ByZWx1ZGUuanMiLCIvaG9tZS91YnVudHUvd29ya3NwYWNlL1llb21hblBoYXNlclNldHVwL3NyYy9hcHAuanMiLCIvaG9tZS91YnVudHUvd29ya3NwYWNlL1llb21hblBoYXNlclNldHVwL3NyYy9zdGF0ZXMvQm9vdC5qcyIsIi9ob21lL3VidW50dS93b3Jrc3BhY2UvWWVvbWFuUGhhc2VyU2V0dXAvc3JjL3N0YXRlcy9HYW1lLmpzIiwiL2hvbWUvdWJ1bnR1L3dvcmtzcGFjZS9ZZW9tYW5QaGFzZXJTZXR1cC9zcmMvc3RhdGVzL1ByZWxvYWQuanMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7Ozs7Ozs0QkNHaUIsa0JBQWtCOzs7OytCQUNmLHFCQUFxQjs7Ozs0QkFDeEIsa0JBQWtCOzs7O0FBSm5DLElBQUksSUFBSSxDQUFDOztBQU9ULE1BQU0sQ0FBQyxNQUFNLEdBQUcsWUFBWTtBQUMxQixNQUFJLEdBQUcsSUFBSSxNQUFNLENBQUMsSUFBSSxDQUFDLEdBQUcsRUFBRSxHQUFHLEVBQUUsTUFBTSxDQUFDLElBQUksRUFBRSxNQUFNLENBQUMsQ0FBQztBQUN0RCxNQUFJLENBQUMsS0FBSyxDQUFDLEdBQUcsQ0FBQyxNQUFNLDRCQUFPLENBQUM7QUFDN0IsTUFBSSxDQUFDLEtBQUssQ0FBQyxHQUFHLENBQUMsU0FBUywrQkFBVSxDQUFDO0FBQ25DLE1BQUksQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLE1BQU0sNEJBQU8sQ0FBQztBQUM3QixNQUFJLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQyxNQUFNLENBQUMsQ0FBQztDQUMxQixDQUFDOzs7Ozs7Ozs7Ozs7O0lDZG1CLElBQUk7V0FBSixJQUFJOzBCQUFKLElBQUk7OztlQUFKLElBQUk7O1dBRWhCLG1CQUFHOztBQUVSLFVBQUksQ0FBQyxJQUFJLENBQUMsS0FBSyxDQUFDLFdBQVcsRUFBRSwrQkFBK0IsQ0FBQyxDQUFDO0tBQy9EOzs7V0FFSyxrQkFBRztBQUNQLFVBQUksQ0FBQyxJQUFJLENBQUMsS0FBSyxDQUFDLFdBQVcsR0FBRyxDQUFDLENBQUM7QUFDaEMsVUFBSSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsS0FBSyxDQUFDLFNBQVMsQ0FBQyxDQUFDO0tBQ2xDOzs7U0FWa0IsSUFBSTs7O3FCQUFKLElBQUk7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0lDRUosSUFBSTtZQUFKLElBQUk7O0FBRVosV0FGUSxJQUFJLEdBRVQ7MEJBRkssSUFBSTs7O0FBSXJCLCtCQUppQixJQUFJLDZDQUliO0dBQ1Q7O2VBTGtCLElBQUk7O1dBT2pCLGtCQUFHLEVBQ1I7OztXQUdLLGtCQUFHLEVBQ1I7OztTQVprQixJQUFJO0dBQVMsTUFBTSxDQUFDLEtBQUs7O3FCQUF6QixJQUFJOzs7Ozs7Ozs7Ozs7OztJQ0ZKLE9BQU87QUFFZixXQUZRLE9BQU8sR0FFWjswQkFGSyxPQUFPOztBQUd4QixRQUFJLENBQUMsS0FBSyxHQUFHLElBQUksQ0FBQztBQUNsQixRQUFJLENBQUMsS0FBSyxHQUFHLEtBQUssQ0FBQztHQUNwQjs7ZUFMa0IsT0FBTzs7V0FPbkIsbUJBQUc7QUFDUixVQUFJLENBQUMsSUFBSSxDQUFDLEtBQUssQ0FBQyxZQUFZLEVBQUUsOEJBQThCLENBQUMsQ0FBQztLQUMvRDs7O1dBRUssa0JBQUc7OztBQUdQLFVBQUksQ0FBQyxHQUFHLENBQUMsTUFBTSxDQUFDLENBQUMsRUFBQyxDQUFDLEVBQUUsWUFBWSxDQUFDLENBQUM7O0FBRW5DLFVBQUksQ0FBQyxLQUFLLEdBQUcsSUFBSSxDQUFDLEdBQUcsQ0FBQyxNQUFNLENBQUMsSUFBSSxDQUFDLElBQUksQ0FBQyxLQUFLLEdBQUMsQ0FBQyxFQUFDLElBQUksQ0FBQyxJQUFJLENBQUMsTUFBTSxHQUFDLENBQUMsRUFBRSxXQUFXLENBQUMsQ0FBQztBQUNoRixVQUFJLENBQUMsS0FBSyxDQUFDLE1BQU0sQ0FBQyxLQUFLLENBQUMsR0FBRyxFQUFFLEdBQUcsQ0FBQyxDQUFDOztBQUVsQyxVQUFJLENBQUMsSUFBSSxDQUFDLGNBQWMsQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLGNBQWMsRUFBRSxJQUFJLENBQUMsQ0FBQztBQUM1RCxVQUFJLENBQUMsSUFBSSxDQUFDLGdCQUFnQixDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsQ0FBQzs7Ozs7O0FBT3ZDLFVBQUksQ0FBQyxJQUFJLENBQUMsS0FBSyxFQUFFLENBQUM7S0FDbkI7OztXQUVLLGtCQUFHOztBQUVQLFVBQUcsSUFBSSxDQUFDLEtBQUssRUFBRTtBQUNiLFlBQUksQ0FBQyxJQUFJLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQyxNQUFNLENBQUMsQ0FBQztPQUMvQjtLQUVGOzs7V0FFYSwwQkFBRztBQUNmLFVBQUksQ0FBQyxLQUFLLEdBQUcsSUFBSSxDQUFDO0tBQ25COzs7U0F4Q2tCLE9BQU87OztxQkFBUCxPQUFPIiwiZmlsZSI6ImdlbmVyYXRlZC5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzQ29udGVudCI6WyIoZnVuY3Rpb24gZSh0LG4scil7ZnVuY3Rpb24gcyhvLHUpe2lmKCFuW29dKXtpZighdFtvXSl7dmFyIGE9dHlwZW9mIHJlcXVpcmU9PVwiZnVuY3Rpb25cIiYmcmVxdWlyZTtpZighdSYmYSlyZXR1cm4gYShvLCEwKTtpZihpKXJldHVybiBpKG8sITApO3ZhciBmPW5ldyBFcnJvcihcIkNhbm5vdCBmaW5kIG1vZHVsZSAnXCIrbytcIidcIik7dGhyb3cgZi5jb2RlPVwiTU9EVUxFX05PVF9GT1VORFwiLGZ9dmFyIGw9bltvXT17ZXhwb3J0czp7fX07dFtvXVswXS5jYWxsKGwuZXhwb3J0cyxmdW5jdGlvbihlKXt2YXIgbj10W29dWzFdW2VdO3JldHVybiBzKG4/bjplKX0sbCxsLmV4cG9ydHMsZSx0LG4scil9cmV0dXJuIG5bb10uZXhwb3J0c312YXIgaT10eXBlb2YgcmVxdWlyZT09XCJmdW5jdGlvblwiJiZyZXF1aXJlO2Zvcih2YXIgbz0wO288ci5sZW5ndGg7bysrKXMocltvXSk7cmV0dXJuIHN9KSIsIi8qIGdsb2JhbCBQaGFzZXIgKi9cclxudmFyIGdhbWU7XHJcblxyXG5pbXBvcnQgQm9vdCBmcm9tIFwiLi9zdGF0ZXMvQm9vdC5qc1wiO1xyXG5pbXBvcnQgUHJlbG9hZCBmcm9tIFwiLi9zdGF0ZXMvUHJlbG9hZC5qc1wiO1xyXG5pbXBvcnQgR2FtZSBmcm9tIFwiLi9zdGF0ZXMvR2FtZS5qc1wiO1xyXG5cclxuXHJcbndpbmRvdy5vbmxvYWQgPSBmdW5jdGlvbiAoKSB7XHJcbiAgZ2FtZSA9IG5ldyBQaGFzZXIuR2FtZSg4MDAsIDYwMCwgUGhhc2VyLkFVVE8sICdnYW1lJyk7XHJcbiAgZ2FtZS5zdGF0ZS5hZGQoJ2Jvb3QnLCBCb290KTtcclxuICBnYW1lLnN0YXRlLmFkZCgncHJlbG9hZCcsIFByZWxvYWQpO1xyXG4gIGdhbWUuc3RhdGUuYWRkKCdnYW1lJywgR2FtZSk7XHJcbiAgZ2FtZS5zdGF0ZS5zdGFydCgnYm9vdCcpO1xyXG59OyIsImV4cG9ydCBkZWZhdWx0IGNsYXNzIEJvb3Qge1xyXG5cclxuICBwcmVsb2FkKCkge1xyXG4gICAgLy8gdGhlIHByZWxvYWQgbWV0aG9kXHJcbiAgICB0aGlzLmxvYWQuaW1hZ2UoJ3ByZWxvYWRlcicsICdhc3NldHMvaW1hZ2VzL2xvYWRpbmdfYmFyLnBuZycpO1xyXG4gIH1cclxuXHJcbiAgY3JlYXRlKCkge1xyXG4gICAgdGhpcy5nYW1lLmlucHV0Lm1heFBvaW50ZXJzID0gMTtcclxuICAgIHRoaXMuZ2FtZS5zdGF0ZS5zdGFydCgncHJlbG9hZCcpO1xyXG4gIH1cclxuXHJcbn0iLCIvL3JlcXVpcmUgb3RoZXIgY29tcG9uZW50c1xyXG5cclxuZXhwb3J0IGRlZmF1bHQgY2xhc3MgR2FtZSBleHRlbmRzIFBoYXNlci5TdGF0ZSB7XHJcblxyXG4gIGNvbnN0cnVjdG9yKCkge1xyXG4gICAgLy9vYmplY3QgbGV2ZWwgcHJvcGVydGllc1xyXG4gICAgc3VwZXIoKTtcclxuICB9XHJcblxyXG4gIGNyZWF0ZSgpIHtcclxuICB9XHJcblxyXG5cclxuICB1cGRhdGUoKSB7XHJcbiAgfVxyXG5cclxuXHJcbn0iLCJleHBvcnQgZGVmYXVsdCBjbGFzcyBQcmVsb2FkIHtcclxuXHJcbiAgY29uc3RydWN0b3IoKSB7XHJcbiAgICB0aGlzLmFzc2V0ID0gbnVsbDtcclxuICAgIHRoaXMucmVhZHkgPSBmYWxzZTtcclxuICB9XHJcblxyXG4gIHByZWxvYWQoKSB7XHJcbiAgICB0aGlzLmxvYWQuaW1hZ2UoJ2xvYWRpbmdfYmcnLCAnYXNzZXRzL2ltYWdlcy9sb2FkaW5nX2JnLmpwZycpO1xyXG4gIH1cclxuXHJcbiAgY3JlYXRlKCkge1xyXG5cclxuICAgIC8vYmFja2dyb3VuZCBmb3IgZ2FtZVxyXG4gICAgdGhpcy5hZGQuc3ByaXRlKDAsMCwgXCJsb2FkaW5nX2JnXCIpO1xyXG5cclxuICAgIHRoaXMuYXNzZXQgPSB0aGlzLmFkZC5zcHJpdGUodGhpcy5nYW1lLndpZHRoLzIsdGhpcy5nYW1lLmhlaWdodC8yLCAncHJlbG9hZGVyJyk7XHJcbiAgICB0aGlzLmFzc2V0LmFuY2hvci5zZXRUbygwLjUsIDAuNSk7XHJcblxyXG4gICAgdGhpcy5sb2FkLm9uTG9hZENvbXBsZXRlLmFkZE9uY2UodGhpcy5vbkxvYWRDb21wbGV0ZSwgdGhpcyk7XHJcbiAgICB0aGlzLmxvYWQuc2V0UHJlbG9hZFNwcml0ZSh0aGlzLmFzc2V0KTtcclxuXHJcbiAgICAvL2RvIGFsbCB5b3VyIGxvYWRpbmcgaGVyZVxyXG4gICAgLy90aGlzLmxvYWQuaW1hZ2UoJ3BsYXllcicsICdhc3NldHMvaW1hZ2VzL3BsYXllci5wbmcnKTsgLy93aWR0aCBhbmQgaGVpZ2h0IG9mIHNwcml0ZVxyXG5cclxuXHJcbiAgICAvL3N0YWFhYXJ0IGxvYWRcclxuICAgIHRoaXMubG9hZC5zdGFydCgpO1xyXG4gIH1cclxuXHJcbiAgdXBkYXRlKCkge1xyXG5cclxuICAgIGlmKHRoaXMucmVhZHkpIHtcclxuICAgICAgdGhpcy5nYW1lLnN0YXRlLnN0YXJ0KCdnYW1lJyk7XHJcbiAgICB9XHJcblxyXG4gIH1cclxuXHJcbiAgb25Mb2FkQ29tcGxldGUoKSB7XHJcbiAgICB0aGlzLnJlYWR5ID0gdHJ1ZTtcclxuICB9XHJcblxyXG59Il19
