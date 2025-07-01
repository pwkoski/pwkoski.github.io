import { data } from "./dcrdata.js";

let page = 0;
generateDCR(page);

//LAYOUT, MAN HOURS, PURCHASES, PHOTO CORRECT

function generateDCR(pageNumber) {

  addPrev();
  addTitle(pageNumber);
  addNext();
  addPictures(pageNumber);
  addWeather(pageNumber);
  addLayout();
  addActivities(pageNumber);
  addManHours(pageNumber);
  addPurchases(pageNumber);
}

function addPrev() {

  // get the prev div
  const prevDiv = document.getElementById("prev");

  //clear content in prev div
  prevDiv.innerHTML = "";

  let buttonPrev = document.createElement("button");
  buttonPrev.innerHTML = "Previous";
  buttonPrev.onclick = function () {
    page--;
    if (page < 0) {
      page = 0;
    }
    generateDCR(page);
  };
  prevDiv.appendChild(buttonPrev);
}

function addTitle(pageNumber) {

  // get the title div
  const titleDiv = document.getElementById("title");

  //clear content in title div
  titleDiv.innerHTML = "";

  // title content
  const heading = document. createElement("h2");
  heading.innerHTML = data[pageNumber].date;

  // add the title content to the title div
  titleDiv.appendChild(heading);
}

function addNext() {

  // get the next div
  const nextDiv = document.getElementById("next");

  //clear content in next div
  nextDiv.innerHTML = "";

  let buttonNext = document.createElement("button");
  buttonNext.innerHTML = "Next";
  buttonNext.onclick = function () {
    page++;
    if (page < 0 || page >= data.length) {
      page = 0;
    }
    generateDCR(page);
  };
  nextDiv.appendChild(buttonNext);

}

function addPictures(pageNumber) {

  // get the next div
  const picturesDiv = document.getElementById("pictures");

  //clear content in next div
  picturesDiv.innerHTML = "";

  //Add images from data
  for (let i = 0; i < data[pageNumber].image_url.length; i++) {
    let img = document.createElement("img");
    img.src = data[pageNumber].image_url[i];
    picturesDiv.appendChild(img);
  }

}

function addWeather(pageNumber) {

  // get the weather div
  const weatherDiv = document.getElementById("weather");

  // clear weather content
  weatherDiv.innerHTML = "";

  // weather content
  const weatherHighTempText = document.createTextNode("High Temperature (F): ");
  const weatherHighTempNum = document.createTextNode(data[pageNumber].highTemp);
  const weatherLowTempText = document.createTextNode("Low Temperature (F): ");
  const weatherLowTempNum = document.createTextNode(data[pageNumber].lowTemp);
  const weatherPrecipText = document.createTextNode("Precipitation (in): ");
  const weatherPrecipNum = document.createTextNode(data[pageNumber].precip);
  const wateringText = document.createTextNode("Watering: ");
  const wateringNum = document.createTextNode(data[pageNumber].watering);

  //Create table
  let weatherTable = document.createElement('table');

  //Create table body
  let weatherTableBody = document.createElement('tbody');

  //Create rows
  const row1 = document.createElement("tr");
  const row2 = document.createElement("tr");
  const row3 = document.createElement("tr");
  const row4 = document.createElement("tr");

  //Create data cells
  const cell11 = document.createElement("td");
  const cell12 = document.createElement("td");
  const cell21 = document.createElement("td");
  const cell22 = document.createElement("td");
  const cell31 = document.createElement("td");
  const cell32 = document.createElement("td");
  const cell41 = document.createElement("td");
  const cell42 = document.createElement("td");

  //Append data to data cells
  cell11.appendChild(weatherHighTempText);
  cell12.appendChild(weatherHighTempNum);
  cell21.appendChild(weatherLowTempText);
  cell22.appendChild(weatherLowTempNum);
  cell31.appendChild(weatherPrecipText);
  cell32.appendChild(weatherPrecipNum);
  cell41.appendChild(wateringText);
  cell42.appendChild(wateringNum);

  //Append cells to rows
  row1.appendChild(cell11);
  row1.appendChild(cell12);
  row2.appendChild(cell21);
  row2.appendChild(cell22);
  row3.appendChild(cell31);
  row3.appendChild(cell32);
  row4.appendChild(cell41);
  row4.appendChild(cell42);

  //Append rows to body
  weatherTableBody.appendChild(row1);
  weatherTableBody.appendChild(row2);
  weatherTableBody.appendChild(row3);
  weatherTableBody.appendChild(row4);

  //Append table body to table
  weatherTable.appendChild(weatherTableBody);

  // add the weather table to the weather div
  weatherDiv.appendChild(weatherTable);

}

function addLayout() {

}

function addActivities(pageNumber) {

  // get the activities and visitors divs
  const activitiesDiv = document.getElementById("activities");
  const visitorsDiv = document.getElementById("visitorsDiv");
  const visitorsText = document.getElementById("visitorsText");
  const dayActivitiesDiv = document.getElementById("dayActivitiesDiv");
  const dayActivitiesText = document.getElementById("dayActivitiesText");
  const eveningActivitiesDiv = document.getElementById("eveningActivitiesDiv");
  const eveningActivitiesText = document.getElementById("eveningActivitiesText");

  // clear data in divs
  activitiesDiv.innerHTML = "";
  visitorsDiv.innerHTML = "";
  visitorsText.innerHTML = "";
  dayActivitiesDiv.innerHTML = "";
  dayActivitiesText.innerHTML = "";
  eveningActivitiesDiv.innerHTML = "";
  eveningActivitiesText.innerHTML = "";

  // Create visistors content
  const visitors = document.createTextNode(data[pageNumber].visitors);
  const visitorsHeading = document.createElement("h3");
  visitorsHeading.innerText = "Visitors:  ";

  //Add visitor content to divs
  visitorsDiv.appendChild(visitorsHeading);

  visitorsText.appendChild(visitors);
  visitorsDiv.appendChild(visitorsText);

  activitiesDiv.appendChild(visitorsDiv);

  // Create activities content
  const activitiesDay = document.createTextNode(data[pageNumber].dayActivities);
  const dayActivitiesHeading = document.createElement("h3");
  dayActivitiesHeading.innerText = "Day Activities:  ";
  const activitiesEvening = document.createTextNode(data[pageNumber].eveningActivities);
  const eveningActivitiesHeading = document.createElement("h3");
  eveningActivitiesHeading.innerText = "Evening Activities:  ";

  //Add activity content to divs
  dayActivitiesDiv.appendChild(dayActivitiesHeading);
  eveningActivitiesDiv.appendChild(eveningActivitiesHeading);

  dayActivitiesText.appendChild(activitiesDay);
  eveningActivitiesText.appendChild(activitiesEvening);
  dayActivitiesDiv.appendChild(dayActivitiesText);
  eveningActivitiesDiv.appendChild(eveningActivitiesText)

  activitiesDiv.appendChild(dayActivitiesDiv);
  activitiesDiv.appendChild(eveningActivitiesDiv);
}

function addManHours(pageNumber) {

}

function addPurchases(pageNumber) {

}