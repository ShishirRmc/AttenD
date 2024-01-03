"use strict";

var attendContainer = document.querySelector(".attend");
var allCards = document.querySelectorAll(".attend--card");
var nope = document.getElementById("nope");
var like = document.getElementById("like");

function initCards(card, index) {
  var newCards = document.querySelectorAll(".attend--card:not(.removed)");

  newCards.forEach(function (card, index) {
    card.style.zIndex = allCards.length - index;
    card.style.transform =
      "scale(" + (20 - index) / 20 + ") translateY(-" + 30 * index + "px)";
    card.style.opacity = (10 - index) / 10;
  });

  attendContainer.classList.add("loaded");

  if (document.querySelectorAll(".attend--card:not(.removed)").length === 0) {
    handleAllCardsSwiped();
  }
}

initCards();
allCards.forEach(function (el) {
  var hammertime = new Hammer(el);

  hammertime.on("pan", function (event) {
    el.classList.add("moving");
  });

  hammertime.on("pan", function (event) {
    if (event.deltaX === 0) return;
    if (event.center.x === 0 && event.center.y === 0) return;

    attendContainer.classList.toggle("attend_like", event.deltaX > 0);
    attendContainer.classList.toggle("attend_nope", event.deltaX < 0);

    var xMulti = event.deltaX * 0.03;
    var yMulti = event.deltaY / 80;
    var rotate = xMulti * yMulti;

    event.target.style.transform =
      "translate(" +
      event.deltaX +
      "px, " +
      event.deltaY +
      "px) rotate(" +
      rotate +
      "deg)";
  });

  hammertime.on("panend", function (event) {
    el.classList.remove("moving");
    attendContainer.classList.remove("attend_like");
    attendContainer.classList.remove("attend_nope");

    var moveOutWidth = document.body.clientWidth;
    var keep = Math.abs(event.deltaX) < 80 || Math.abs(event.velocityX) < 0.5;

    event.target.classList.toggle("removed", !keep);

    if (keep) {
      event.target.style.transform = "";
    } else {
      var endX = Math.max(
        Math.abs(event.velocityX) * moveOutWidth,
        moveOutWidth
      );
      var toX = event.deltaX > 0 ? endX : -endX;
      var endY = Math.abs(event.velocityY) * moveOutWidth;
      var toY = event.deltaY > 0 ? endY : -endY;
      var xMulti = event.deltaX * 0.03;
      var yMulti = event.deltaY / 80;
      var rotate = xMulti * yMulti;

      event.target.style.transform =
        "translate(" +
        toX +
        "px, " +
        (toY + event.deltaY) +
        "px) rotate(" +
        rotate +
        "deg)";
      initCards();
    }
  });
});

function createButtonListener(like) {
  return function (event) {
    var cards = document.querySelectorAll(".attend--card:not(.removed)");
    var moveOutWidth = document.body.clientWidth * 1.5;

    if (!cards.length) return false;

    var card = cards[0];

    card.classList.add("removed");

    if (like) {
      card.style.transform =
        "translate(" + moveOutWidth + "px, -100px) rotate(-30deg)";
    } else {
      card.style.transform =
        "translate(-" + moveOutWidth + "px, -100px) rotate(30deg)";
    }

    initCards();

    event.preventDefault();
  };
}

var nopeListener = createButtonListener(false);
var likeListener = createButtonListener(true);

nope.addEventListener("click", nopeListener);
like.addEventListener("click", likeListener);

//

var undo = document.getElementById("undo");
var removedCardsStack = [];

undo.addEventListener("click", function (event) {
  var removedCards = document.querySelectorAll(".attend--card.removed");
  if (removedCards.length > 0) {
    for (var i = removedCards.length - 1; i >= 0; i--) {
      // var removedCard = removedCards[i];
      var removedCard = removedCards[removedCards.length - 1];
      removedCard.classList.remove("removed");
      removedCard.style.transform = "";
      removedCardsStack.pop();
    }
    initCards();
  }
});

function handleAllCardsSwiped() {
  // Remove all cards
  var cardsContainer = document.querySelector(".attend--cards");
  cardsContainer.innerHTML = ""; // Remove all cards

  // Remove the buttons
  var buttonsContainer = document.querySelector(".attend--buttons");
  buttonsContainer.innerHTML = ""; // Remove all buttons

  // Display the thank-you message
  var attendContainer = document.querySelector(".attend");

  var thankYouMessage = document.createElement("div");
  thankYouMessage.classList.add("thank-you");
  thankYouMessage.textContent = "Thank you for attending the expo! 😊";

  // Append the thank-you message to the .attend container
  attendContainer.appendChild(thankYouMessage);

  var logo = document.getElementById("logo");
  logo.classList.add("increased-size");
}
