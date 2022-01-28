// change navbar color when navbar scroll

function scrollValue() {
  var navbar = document.getElementById('navbar');
  var scroll = window.scrollY;
  if (scroll < 600) {
    navbar.classList.remove('BgColour');
  } else {
    navbar.classList.add('BgColour');
  }
}
// ############## popup #############

function popup() {
  document.getElementById("panel").style.display = "none";
}

// Posts overflow hide
function scrollupper() {
  var posts = document.getElementById('bookposts');
  var scroll = window.scrollY;

  if (scroll < 900) {
    posts.classList.remove('scrollupper');
  } else {
    posts.classList.add('scrollupper');
  }
}

window.addEventListener('scroll', scrollValue);
window.addEventListener('scroll', scrollupper);

// navbar onclick to display dropdown list

function myFunction() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";

  }
  else {
    x.style.display = "none";
  }
}

function BookCatBtn() {
  var x = document.getElementById("myDIVBtn");
  if (x.style.display === "none") {
    x.style.display = "block";

  }
  else {
    x.style.display = "none";
  }
}


// media quarry for navbar dropdown list of category

function daFunction(x) {

  if (x.matches) { // If media query matches

    y.style.position = "relative"
  } else {
    y.style.position = "absolute"
  }
}
var y = document.getElementById("myDIV");
var x = window.matchMedia("(max-width:1190px)")
daFunction(x) // Call listener function at run time
x.addListener(daFunction)


// ################# post slider #############

var slides = document.getElementsByClassName("booksitems");

for (let i = 0; i < slides.length; i++) {
  let rightBtn = document.getElementById("right-button" + i);
  let leftBtn = document.getElementById("left-button" + i);


  rightBtn.addEventListener("click", function (event) {
    let conent = document.querySelector('#content' + i);
    conent.scrollLeft += 550;
    event.preventDefault();
  });

  leftBtn.addEventListener("click", function (event) {
    let conent = document.querySelector('#content' + i);
    conent.scrollLeft -= 550;
    event.preventDefault();
  });

}


// ################# slider button hide ##################


function ppu() {
  document.getElementById("uppv").style.display = "none";
  document.getElementById("uppu").style.display = "flex";

}

function ppuc() {
  document.getElementById("uppv").style.display = "flex";
  document.getElementById("uppu").style.display = "none";

}


// ############## profile photo upload ############

const inFile = document.getElementById("inpFile");
const previewContainer = document.getElementById("imagePreview");
const previewImage = previewContainer.querySelector(".image-preview__image");

inpFile.addEventListener("change", function () {
  const file = this.files[0];

  if (file) {
    const reader = new FileReader();

    previewImage.style.display = "block"

    reader.addEventListener("load", function () {

      previewImage.setAttribute("src", this.result);
    });

    reader.readAsDataURL(file);
  }
});

// ############# hide or show password ##########

function ShowPass() {
  var x = document.getElementById("loginpassword");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function ShowPassR() {
  var x = document.getElementById("id_new_password1");
  var y = document.getElementById("id_new_password2")
  if (x.type === "password", y.type === "password") {
    x.type = "text";
    y.type = "text";

  } else {
    x.type = "password";
    y.type = "password";
  }
}

// ################# hide Book Options ##################


var slides = document.getElementsByClassName("bookinfo");

for (let i = 1; i < slides.length + 1; i++) {
  let OptionBtn = document.getElementById("BookOptionNo" + i);


  OptionBtn.addEventListener("click", function (event) {
    let conent = document.querySelector('#DeleteBook' + i);


    if (conent.style.display === "none") {
      conent.style.display = "block";
      event.preventDefault();

    }
    else {
      conent.style.display = "none";
      event.preventDefault();
    }

  });
}

// ################################### for delete button

var slides = document.getElementsByClassName("bookinfo");

for (let i = 1; i < slides.length + 1; i++) {
  let OptionBtn = document.getElementById("Delete1" + i);


  OptionBtn.addEventListener("click", function (event) {
    let conent = document.querySelector('#DeleteBookConfirm' + i);
    let bookimg = document.querySelector('#bookimg' + i);
    let Booktext = document.querySelector('#Booktext' + i);
    let Option = document.querySelector('#DeleteBook' + i);


    if (conent.style.display === "none") {
      bookimg.style.display = "none";
      Booktext.style.display = "none"
      Option.style.display = "none"
      conent.style.display = "block";
      event.preventDefault();

    }
    else {
      conent.style.display = "none";
      event.preventDefault();
    }

  });
}


// ############################### for cancle button

var slides = document.getElementsByClassName("bookinfo");


for (let i = 1; i < slides.length + 1; i++) {
  let OptionBtn = document.getElementById("DeleteBookCancle" + i);

  OptionBtn.addEventListener("click", function (event) {
    let conent = document.querySelector('#DeleteBookConfirm' + i);
    let bookimg = document.querySelector('#bookimg' + i);
    let Booktext = document.querySelector('#Booktext' + i);


    if (conent.style.display === "block") {
      bookimg.style.display = "block";
      Booktext.style.display = "block"
      conent.style.display = "none";
      event.preventDefault();

    }
    else {
      conent.style.display = "block";
      event.preventDefault();
    }

  });
}



// Show Books in profile

function ShowBooks() {
  var Books = document.getElementById("ShowBooks");
  var Following = document.getElementById("ShowFollowings");
  var Follower = document.getElementById("ShowFollowers");
  Books.style.display = "flex";
  Following.style.display = "none";
  Follower.style.display = "none";
}

// Show Followings in profile

function ShowFollowings() {
  var Books = document.getElementById("ShowBooks");
  var Following = document.getElementById("ShowFollowings");
  var Follower = document.getElementById("ShowFollowers");
  Books.style.display = "none";
  Following.style.display = "flex";
  Follower.style.display = "none";
}

// Show FOllowers in profile

function ShowFollowers() {
  var Books = document.getElementById("ShowBooks");
  var Following = document.getElementById("ShowFollowings");
  var Follower = document.getElementById("ShowFollowers");
  Books.style.display = "none";
  Following.style.display = "none";
  Follower.style.display = "flex";
}