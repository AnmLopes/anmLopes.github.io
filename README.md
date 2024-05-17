<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Name - Resume</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    header {
      background-color: #333;
      color: #fff;
      padding: 2em 0;
      text-align: center;
    }

    section {
      margin: 2em;
    }

    h1, h2 {
      color: #333;
    }

    ul {
      list-style-type: none;
      padding: 0;
    }

    ul li {
      margin-bottom: 1em;
    }

    .section-title {
      font-size: 1.5em;
      border-bottom: 2px solid #333;
      padding-bottom: 0.5em;
      margin-bottom: 1em;
    }

    .date {
      font-style: italic;
    }

    .education, .experience {
      margin-bottom: 2em;
    }

    .skills {
      display: flex;
      flex-wrap: wrap;
    }

    .skill {
      background-color: #333;
      color: #fff;
      padding: 0.5em 1em;
      margin: 0.5em;
      border-radius: 5px;
    }
  </style>
</head>
<body>

  <header>
    <h1>Your Name</h1>
    <p>Web Developer | Business Analyst | </p>
  </header>

  <section>
    <div class="education">
      <h2 class="section-title">Education</h2>
      <ul>
        <li>
          <h3>University Name</h3>
          <p class="date">Graduated: May 20XX</p>
          <p>Bachelor of Science in Computer Science</p>
        </li>
      </ul>
    </div>

    <div class="experience">
      <h2 class="section-title">Work Experience</h2>
      <ul>
        <li>
          <h3>Company Name</h3>
          <p class="date">June 20XX - Present</p>
          <p>Position: Web Developer</p>
          <p>Description of responsibilities and achievements in this role.</p>
        </li>
      </ul>
    </div>

    <div class="skills">
      <h2 class="section-title">Skills</h2>
      <div class="skill">HTML</div>
      <div class="skill">CSS</div>
      <div class="skill">JavaScript</div>
      <div class="skill">React.js</div>
      <div class="skill">Business Analysis</div>
      <!-- Add more skills as needed -->
    </div>
  </section>

</body>
</html>
