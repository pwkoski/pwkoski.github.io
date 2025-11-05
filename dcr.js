import { data } from "./dcrdata.js";
import { layout } from "./dcrlayoutdata.js";

let page = 0;
generateDCR(page);

function generateDCR(pageNumber) {

  addPrev();
  addTitle(pageNumber);
  addNext();
  addPictures(pageNumber);
  addLayout(40, 10, layout);
  addActivities(pageNumber);
  addManHours(pageNumber);
  addPurchases(pageNumber);
  addHarvest(pageNumber);
  addPreserve(pageNumber);
}

//addPrev: Function that adds the "Previous" button to the page
//@param: none
//@return: none, adds the button to the page
function addPrev() {

  // get the prev div
  const prevDiv = document.getElementById("prev");

  //clear content in prev div
  prevDiv.innerHTML = "";

  //create button
  let buttonPrev = document.createElement("button");
  buttonPrev.innerHTML = "Previous";
  //set functionality
  buttonPrev.onclick = function () {
    page--;
    if (page < 0) {
      page = data.length - 1;
    }
    generateDCR(page);
  };
  prevDiv.appendChild(buttonPrev);
}

//addTitle: Function that adds the page title to the page
//@param: none
//@return: none, adds the title to the page
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

//addNext: Function that adds the "Next" button to the page
//@param: none
//@return: none, adds the button to the page
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

//addPictures: Function that adds pictures to the page
//@param: int pageNumber, the number corresponding to the entry
//@return: none, adds pictures to the page
function addPictures(pageNumber) {

  // get the picture div
  const picturesDiv = document.getElementById("pictures");

  //clear content in picture div
  picturesDiv.innerHTML = "";

  //Add images from data
  for (let i = 0; i < data[pageNumber].image_url.length; i++) {
    let img = document.createElement("img");
    img.src = data[pageNumber].image_url[i];
    picturesDiv.appendChild(img);
  }

}

//addLayout: creates the layout and legend and appends to the weather and layout container
//@param: noRow, number of rows in the layout
//@param: noColumn, number of columns in the layout
//@param: layout, array of ingredient objects with ingredient name and occupancy in a matrix in [Row Start,Column Start,Row End,Column End] format.
//@return: none, modifies DOM
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

  //Create layout HTML table
  const tbl = document.createElement("table");
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


  //Create div for garden
  const gardenDiv = document.createElement('div');
  gardenDiv.setAttribute("id", "gardenlayout");
  //add table to layoutdiv
  gardenDiv.appendChild(tbl);

  //Create div for legend
  const legendDiv = document.createElement('div');
  legendDiv.setAttribute("id", "legend");

  //Create legend table
  const legend = document.createElement("table");
  const legendBody = document.createElement("tbody");

  //Create flag for "unknown" so multiple entries aren't made
  let foundUnknown = false;
  for (let i = 1; i < layout.length; i++) {
    if (layout[i].name == "none" && foundUnknown == true) {
      continue;
    }
    else {
      if (layout[i].name == "none") foundUnknown = true;
      const legendrow = document.createElement("tr");
      const cell = document.createElement("td");
      let linkText = document.createTextNode(layout[i].name);
      cell.appendChild(linkText);
      cell.setAttribute("class", layout[i].name);
      cell.addEventListener("mouseenter", hightlight);
      cell.addEventListener("mouseleave", reverse);
      legendrow.appendChild(cell);
      legendBody.appendChild(legendrow);
    }

  }

  //Append body to table
  legend.appendChild(legendBody);
  //Append table to div
  legendDiv.appendChild(legend);

  //Append layout div and legend div to layout div
  //get the layout container div
  const layoutDiv = document.getElementById("layout");
  //Clear content
  layoutDiv.innerHTML = "";

  //Add heading
  const layoutHeading = document.createElement("h3");
  layoutHeading.innerText = "Garden Layout:  ";
  layoutDiv.appendChild(layoutHeading);
  //Create flex container for layout and legend
  const layoutFlexContainer = document.createElement("div");
  layoutFlexContainer.setAttribute("id", "layoutFlexContainer");
  layoutDiv.appendChild(layoutFlexContainer);
  //append legendDiv to layoutDiv
  layoutFlexContainer.appendChild(legendDiv);
  //append  gardenDiv to layoutDiv
  layoutFlexContainer.appendChild(gardenDiv);


  //helper functions
  function hightlight(evt) {
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

//addActivities: Function that adds the days activities to the page
//@param: int pageNumber, the number corresponding to the entry
//@return: none, adds activities to the page
function addActivities(pageNumber) {

  // get the activities divs
  const activitiesDiv = document.getElementById("activities");
  const dayActivitiesDiv = document.getElementById("dayActivitiesDiv");
  const dayActivitiesText = document.getElementById("dayActivitiesText");

  // clear data in divs
  activitiesDiv.innerHTML = "";
  dayActivitiesDiv.innerHTML = "";
  dayActivitiesText.innerHTML = "";

  // Create activities content
  const activitiesDay = document.createTextNode(data[pageNumber].dayActivities);
  const dayActivitiesHeading = document.createElement("h3");
  dayActivitiesHeading.innerText = "Activities:  ";

  //Add activity content to divs
  dayActivitiesDiv.appendChild(dayActivitiesHeading);
  dayActivitiesText.appendChild(activitiesDay);
  dayActivitiesDiv.appendChild(dayActivitiesText);

  activitiesDiv.appendChild(dayActivitiesDiv);

}

//addActivities: Function that adds currrent day's activities and man hours to page, displays the previous total,
//and displays the new total.
//@param: int pageNumber, the number corresponding to the entry
//@return: none, adds man hours to the page
function addManHours(pageNumber) {
  let previousTotal = 0.0;
  let newTotal = 0.0;
  let currentActivity = data[pageNumber].manHours[0];
  let currentHours = data[pageNumber].manHours[1];

  //get divs
  const manhoursDiv = document.getElementById("manhours");
  //clear existing content
  manhoursDiv.innerHTML = "";

  // Create manhours content
  const manhoursHeading = document.createElement("h3");
  manhoursHeading.innerText = "Manhours:  ";

  //Add content to divs
  manhoursDiv.appendChild(manhoursHeading);

  //Create div for text
  const manhoursText = document.createElement('div');
  manhoursText.setAttribute("id", "manhoursText");
  manhoursDiv.appendChild(manhoursText);

  //Sum previous man hours
  for (let i = 0; i < pageNumber; i++) {
    previousTotal = previousTotal + data[i].manHours[1];
  }

  //Create man hours table
  const manhoursTable = document.createElement("table");
  const manhoursBody = document.createElement("tbody");
  const row1 = document.createElement("tr");
  const row2 = document.createElement("tr");
  const row3 = document.createElement("tr");
  const cell11 = document.createElement("td");
  const cell12 = document.createElement("td");
  const cell21 = document.createElement("td");
  const cell22 = document.createElement("td");
  const cell31 = document.createElement("td");
  const cell32 = document.createElement("td");
  let cell11Text = document.createTextNode("Previous Total: ");
  let cell12Text = document.createTextNode(previousTotal);
  let cell21Text = document.createTextNode(currentActivity);
  let cell22Text = document.createTextNode(currentHours);
  let cell31Text = document.createTextNode("New Total: ");
  let cell32Text = document.createTextNode(previousTotal + currentHours);

  cell11.appendChild(cell11Text);
  cell12.appendChild(cell12Text);
  cell21.appendChild(cell21Text);
  cell22.appendChild(cell22Text);
  cell31.appendChild(cell31Text);
  cell32.appendChild(cell32Text);

  row1.appendChild(cell11);
  row1.appendChild(cell12);
  row2.appendChild(cell21);
  row2.appendChild(cell22);
  row3.appendChild(cell31);
  row3.appendChild(cell32);

  manhoursBody.appendChild(row1);
  manhoursBody.appendChild(row2);
  manhoursBody.appendChild(row3);

  manhoursTable.appendChild(manhoursBody);

  manhoursText.appendChild(manhoursTable);

}

//addPurchases: Function that adds currrent day's purchases to the page, displays the total.
//@param: int pageNumber, the number corresponding to the entry
//@return: none, adds purchases to the page
function addPurchases(pageNumber) {

  let total = 0.0;

  //get divs
  const purchasesDiv = document.getElementById("purchases");
  //clear existing content
  purchasesDiv.innerHTML = "";

  // Create purchases content
  const purchasesHeading = document.createElement("h3");
  purchasesHeading.innerText = "Purchases:  ";

  //Add content to divs
  purchasesDiv.appendChild(purchasesHeading);

  //Create div for text
  const purchasesText = document.createElement('div');
  purchasesText.setAttribute("id", "purchasesText");
  purchasesDiv.appendChild(purchasesText);

  //Create table
  const purchasesTable = document.createElement("table");
  const purchasesBody = document.createElement("tbody");

  for (let i = 0; i <= pageNumber; i++) {
    if (data[i].purchases[0] == "") {
      continue;
    }
    total = total + data[i].purchases[1];
    let row = document.createElement("tr");
    let date = document.createElement("td");
    let type = document.createElement("td");
    let amount = document.createElement("td");
    let dateText = document.createTextNode(data[i].date);
    let typeText = document.createTextNode(data[i].purchases[0]);
    let amountText = document.createTextNode(data[i].purchases[1]);
    date.appendChild(dateText);
    type.appendChild(typeText);
    amount.appendChild(amountText);
    row.appendChild(date);
    row.appendChild(type);
    row.appendChild(amount);
    purchasesBody.appendChild(row);

  }

  let totalRow = document.createElement("tr");
  let totalHeading = document.createElement("td");
  let totalBlank = document.createElement("td");
  let totalAmount = document.createElement("td");
  let totalHeadingText = document.createTextNode("Total:  ");
  let totalBlankText = document.createTextNode("     ");
  let totalAmountText = document.createTextNode(total);
  totalHeading.appendChild(totalHeadingText);
  totalBlank.appendChild(totalBlankText);
  totalAmount.appendChild(totalAmountText);
  totalRow.appendChild(totalHeading);
  totalRow.appendChild(totalBlank);
  totalRow.appendChild(totalAmount);
  purchasesBody.appendChild(totalRow);
  purchasesTable.appendChild(purchasesBody);
  purchasesText.appendChild(purchasesTable);

}

//addHarvest: Function that adds the current harvest up the the day to the page.
//@param: int pageNumber, the number corresponding to the entry
//@return: none, adds harvest to the page
function addHarvest(pageNumber) {

  let harvestObject = {};

  //get div
  const harvestDiv = document.getElementById("harvest");
  //clear existing content
  harvestDiv.innerHTML = "";

  // Create purchases content
  const harvestHeading = document.createElement("h3");
  harvestHeading.innerText = "Harvest:  ";

  //Add content to divs
  harvestDiv.appendChild(harvestHeading);

  //Create div for text
  const harvestText = document.createElement('div');
  harvestText.setAttribute("id", "harvestText");
  harvestDiv.appendChild(harvestText);

  //Create table
  const harvestTable = document.createElement("table");
  const harvestBody = document.createElement("tbody");

  //Create harvestObject
  for (let i = 0; i <= pageNumber; i++) {

    if (data[i].harvest[0] == "") {
      continue;
    }
    for (let j = 0; j < data[i].harvest.length; j += 2) {
      if (data[i].harvest[j] in harvestObject) {
        harvestObject[data[i].harvest[j]] = harvestObject[data[i].harvest[j]] + data[i].harvest[j+1];
      }
      else {
        harvestObject[data[i].harvest[j]] = data[i].harvest[j+1];
      }
      }
  }

  //Create table
  for (var key in harvestObject) {
    if (!harvestObject.hasOwnProperty(key)) {
        //The current property is not a direct property of harvestObject
        continue;
    }
    let row = document.createElement("tr");
    let type = document.createElement("td");
    let amount = document.createElement("td");
    let typeText = document.createTextNode(key);
    let amountText = document.createTextNode(harvestObject[key]);
    type.appendChild(typeText);
    amount.appendChild(amountText);
    row.appendChild(type);
    row.appendChild(amount);
    harvestBody.appendChild(row);
  }

  harvestTable.appendChild(harvestBody);
  harvestText.appendChild(harvestTable);

}

//addPreserve: Function that adds the current preserved items up the the day to the page.
//@param: int pageNumber, the number corresponding to the entry
//@return: none, adds preserved items to the page
function addPreserve(pageNumber) {

  let preserveObject = {};

  //get div
  const preserveDiv = document.getElementById("preserve");
  //clear existing content
  preserveDiv.innerHTML = "";

  // Create preserve content
  const preserveHeading = document.createElement("h3");
  preserveHeading.innerText = "Preserved:  ";

  //Add content to divs
  preserveDiv.appendChild(preserveHeading);

  //Create div for text
  const preserveText = document.createElement('div');
  preserveText.setAttribute("id", "preserveText");
  preserveDiv.appendChild(preserveText);

  //Create table
  const preserveTable = document.createElement("table");
  const preserveBody = document.createElement("tbody");

  //Create preserveObject
  for (let i = 0; i <= pageNumber; i++) {

    if (data[i].preserve[0] == "") {
      continue;
    }
    for (let j = 0; j < data[i].preserve.length; j += 2) {
      preserveObject[data[i].preserve[j]] = data[i].preserve[j+1];
    }
  }

  //Create table
  for (var key in preserveObject) {
    if (!preserveObject.hasOwnProperty(key)) {
        //The current property is not a direct property of p
        continue;
    }
    let row = document.createElement("tr");
    let type = document.createElement("td");
    let amount = document.createElement("td");
    let typeText = document.createTextNode(key);
    let amountText = document.createTextNode(preserveObject[key]);
    type.appendChild(typeText);
    amount.appendChild(amountText);
    row.appendChild(type);
    row.appendChild(amount);
    preserveBody.appendChild(row);
  }

  preserveTable.appendChild(preserveBody);
  preserveText.appendChild(preserveTable);

}
