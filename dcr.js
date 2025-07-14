import { data } from "./dcrdata.js";

const layout = [

  {
    "name": "",
    "grid": [0,0,0,0],
    "link": ""
  },
  {
    "name": "unknown",
    "grid": [0,0,39,0],
    "link": ""
  },
  {
    "name": "jalapenos",
    "grid": [0,1,2,1],
    "link": "https://www.burpee.com/pepper-hot-jalapeno-early-prod099710.html?srsltid=AfmBOopFVYjX9S6dVgljv6wQd-z3L4Fy48KItz9h4ud87dpZoNHdWyxn"
  },
  {
    "name": "tomatoes",
    "grid": [3,1,39,1],
    "link": ""
  },
  {
    "name": "bellPeppers",
    "grid": [0,2,7,2],
    "link": ""
  },
  {
    "name": "beets",
    "grid": [8,2,11,2],
    "link": ""
  },
  {
    "name": "onions",
    "grid": [12,2,39,2],
    "link": ""
  },
  {
    "name": "zucchini",
    "grid": [0,3,11,3],
    "link": ""
  },
  {
    "name": "carrots",
    "grid": [12,3,39,3],
    "link": ""
  },
  {
    "name": "squash",
    "grid": [0,4,14,4],
    "link": ""
  },
  {
    "name": "peas",
    "grid": [15,4,39,4],
    "link": ""
  }

]

let page = 0;
generateDCR(page);

//LAYOUT finish, can't seem to get that first table to play nice, maybe put activities next to it, MAN HOURS, PURCHASES, PHOTO CORRECT

function generateDCR(pageNumber) {

  addPrev();
  addTitle(pageNumber);
  addNext();
  addPictures(pageNumber);
  addWeather(pageNumber);
  addLayout(40, 10, layout);
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
  weatherTableBody.setAttribute("id", "weather");
  weatherTable.appendChild(weatherTableBody);
  weatherTable.setAttribute("id", "weather");

  // add the weather table to the weather div
  weatherDiv.appendChild(weatherTable);

}


//I: rows, columns, A JSON type variable with an array of ingredient objects.  Each object has
//name string, grid occupancy on a rowxcolumn matrix in [R1,C1,R2,C2] format, and link.
//O: An HTML table with each cell containing information from the JSON.
//C: Limited to a 40x50 table to correspond with actual grow area
//E:

//strategy: Iterate through JSON and create a matrix with all the data.  Pass the matrix to the table creator function.  Iterate through matrix, creating rows as necessary.

//Create empty matrix.  Iterate through JSON and put data into matrix.  Pass matrix to table creator function.

//data[pageNumber].highTemp
// const data = [
//   {
//     "date": "Saturday, June 7th, 2025",
//     "highTemp": 51.0,
//     "lowTemp": 65.0,
//     "precip": 0.35,
//     "watering": "N/A",
//     "visitors": "None",
//     "dayActivities": "Weld tiller, measure and stake out area. Remove weeds, mow, till soil to break up thatch, hand sift thatch from soil and dispose",
//     "eveningActivities": "None",
//     "manHours": ["Paul", 7.5, "Derek", 7.5],
//     "purchases": ["Seeds, Stakes, Twine", 90.00],
//     "image_url": ["https://picsum.photos/200", "https://picsum.photos/300", "https://picsum.photos/400"],
//   }]



function addLayout(noRow, noColumn, layout) {

    //Create empty matrix
    let layoutMatrix = [];

    for ( let y = 0; y < noRow; y++ ) {
      layoutMatrix[ y ] = [];
      for ( let x = 0; x < noColumn; x++ ) {
        layoutMatrix[ y ][ x ] = "";
      }
    }

    //Fill matrix with data
    for ( let n = 0; n < layout.length; n++) {

      let rowStart = layout[n].grid[0];
      let colStart = layout[n].grid[1];
      let rowEnd = layout[n].grid[2];
      let colEnd = layout[n].grid[3];

      for ( let x = rowStart; x <= rowEnd; x++ ) {
        layoutMatrix[x][colStart] = {name: layout[n].name, link: layout[n].link}
      }
    }

    //Check to see:
    //console.log("this is layoutMatrix: ", layoutMatrix);

    //Create layout HTML table
    const tbl = document.createElement("table");
    tbl.setAttribute("id", "gardenlayout");
    const tblBody = document.createElement("tbody");

    for (let i = 0; i < noRow; i++) {
      const row = document.createElement("tr");

      for (let j = 0; j < noColumn; j++) {
        const cell = document.createElement("td");
        cell.setAttribute("class", layoutMatrix[i][j].name);
        row.appendChild(cell);
      }

      tblBody.appendChild(row);
    }

    tbl.appendChild(tblBody);

    //Get div for table
    const layoutDiv = document.getElementById("gardenlayout");
    layoutDiv.appendChild(tbl);

    //Create legend
    const legendDiv = document.getElementById("legend");
    const legend = document.createElement("table");
    legend.setAttribute("id", "legend");
    const legendBody = document.createElement("tbody");

    for (let i = 1; i < layout.length; i++) {
      const legendrow = document.createElement("tr");
      // const cell1 = document.createElement("td");
      // cell1.setAttribute("class", layout[i].name);
      // legendrow.appendChild(cell1);
      const cell2 = document.createElement("td");
      let a = document.createElement('a');
      a.title = layout[i].name;
      a.href = layout[i].link;
      let linkText = document.createTextNode(layout[i].name);
      a.appendChild(linkText);
      cell2.appendChild(a);
      cell2.setAttribute("class", layout[i].name);
      cell2.addEventListener("mouseenter", hightlight);
      cell2.addEventListener("mouseleave", reverse);
      legendrow.appendChild(cell2);
      legendBody.appendChild(legendrow);
    }

    legend.appendChild(legendBody);
    legendDiv.appendChild(legend);

     //helper functions
     function hightlight(evt) {
       let oldClassName = evt.target.className;
       let targets = document.getElementsByClassName(evt.target.className);
       let targetsArray = Array.from(targets);
       for (let i = 0; i < targetsArray.length; i++) {
        targetsArray[i].className = "legendHighlight";
       }
     }

     function reverse(evt) {
      let newClassName = evt.target.innerText;
      let targets = document.getElementsByClassName("legendHighlight");
      let targetsArray = Array.from(targets);
      for (let i = 0; i < targetsArray.length; i++) {
        targetsArray[i].className = newClassName;
      }
     }

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