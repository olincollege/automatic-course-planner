# automatic-course-planner

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/olincollege/automatic-course-planner">
    <img src="olincollege_logo.jpeg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Automatic Course Planner</h3>

  <p align="center">
    <br />
    <a href="https://olincollege.github.io/automatic-course-planner"><strong>Explore the website »</strong></a>
    <br />
    <br />
    <a href="https://olincollege.github.io/automatic-course-planner">View Demo</a>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The project aims to help college students plan out their 4-year course schedule based on their major and any other constraints they have such as studying abroad, leave of absence, or early graduation. The project predicts what courses will be offered for the next four years based on the past 10 years of course offering data. The prediction model we used was the SARIMAX model which does time series forecasting. The prediction model built for this project is in `course_offering_prediction.ipynb` file.    

From the predicted course offering and the likelihood of the courses' offering for each semester, we filled in the requirements for graduation starting with the major requirement and general requirement along with the credit requirement. Since the credit requirements do not have to be a specific course, they are picked out randomly from the courses that are more than 50% likely to be offered, weighted by the likelihood of their offering. 

The user's constraints are received and the generated 4-year course schedule for the user is shown in a user-friendly way through the Tkinter library.  



<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install the requirements
   ```sh
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage

1. Run the `course_planner_main.py` file
2. Choose your major
3. Choose if you are doing LOA and the according semester 
4. Choose if you are studying abroad and the according semester
5. Choose if you are graduating early and the according semester
6. Press on the `View 4 Year Course Plan` button
7. Your 4-year course schedule has been generated!!


<!-- ROADMAP -->
## Roadmap

- [ ] Course offering prediction
- [ ] Get user constraints(major, LOA, study abroad, graduating early)
- [ ] Fill major requirements
- [ ] Fill general requirements
- [ ] Fill credit requirements
- [ ] Show personalized 4-year course schedule

<!-- WEBSITE -->
## Website
Our website can be found at <a>https://olincollege.github.io/automatic-course-planner/</a>.

<!-- CREDITS -->
## Credits
Contributors on this project include Aditi Bharadwaj, Dongim Lee, Sally Lee, and Vivian Mak. Information about course offerings was taken from Olin College's website and catalogs. Information about the predictive model we used, the SARIMAX model, was taken from <a href="[https://olincollege.github.io/automatic-course-planner](https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html)">this link</a>.

<!-- LICENSE -->
## License
Distributed under the MIT License.
