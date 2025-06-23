import { data } from "./dcrdata.js";


console.log("I am the DCR");
console.log("Now here is some data: ", data);

let page = 0;
generateDCR(page);

//Clear child data FIRST!!!!!

function generateDCR(pageNumber) {

  if (pageNumber < 0 || pageNumber > data.length) {
    pageNumber = 0;
  }
  //create title block
  addTitle(pageNumber);
  addWeather(pageNumber);
  addActivities(pageNumber);

}

  //Add a simple button
  var button = document.createElement("button");
  button.innerHTML = "Click for Next";
  button.onclick = function () {
    generateDCR(page++);
};
  document.body.appendChild(button);

  //Add simple image
  var img = document.createElement("img");
  img.src = data[0].image_url[0];
  document.body.appendChild(img);

  function addTitle(pageNumber) {

    // get the title div
    const titleDiv = document.getElementById("title");

    // title content
    const titleContent = document.createTextNode(data[pageNumber].date);

    // add the title content to the title div
    titleDiv.appendChild(titleContent);
  }

  function addWeather(pageNumber) {

    // get the weather div
    const weatherDiv = document.getElementById("weather");

    // weather content
    const weatherHighTemp = document.createTextNode("High Temperature: " + data[pageNumber].highTemp);
    const weatherLowTemp = document.createTextNode("Low Temperature: " + data[pageNumber].lowTemp);
    const weatherPrecip = document.createTextNode("Precipitation (in): " + data[pageNumber].precip);

    // add the weather contents to the weather div
    weatherDiv.appendChild(weatherHighTemp);
    weatherDiv.appendChild(weatherLowTemp);
    weatherDiv.appendChild(weatherPrecip);
  }

  function addActivities(pageNumber) {

    // get the activities div
    const activitiesDiv = document.getElementById("activities");

    // activities content
    const activitiesWatering = document.createTextNode("Watering: " + data[pageNumber].watering);
    const activitiesVisitors = document.createTextNode("Visitors: " + data[pageNumber].visitors);
    const activitiesDay = document.createTextNode("Day Activities: " + data[pageNumber].dayActivities);
    const activitiesEvening = document.createTextNode("Evening Activities: " + data[pageNumber].eveningActivities);


    // add the activity contents to the activity div
    activitiesDiv.appendChild(activitiesWatering);
    activitiesDiv.appendChild(activitiesVisitors);
    activitiesDiv.appendChild(activitiesDay);
    activitiesDiv.appendChild(activitiesEvening);
  }