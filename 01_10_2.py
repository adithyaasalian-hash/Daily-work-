<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CV Builder</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      padding: 20px;
    }
    .container {
      max-width: 800px;
      margin: auto;
      background: #fff;
      padding: 20px;
      border: 1px solid #ddd;
    }
    h1 {
      text-align: center;
    }
    .resume {
      margin-top: 30px;
      padding: 20px;
      border: 1px solid #ccc;
      background: #fafafa;
    }
    img {
      max-width: 150px;
      border-radius: 50%;
      margin-bottom: 20px;
    }
    .section {
      margin-bottom: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>CV Builder</h1>
    <form id="cvForm">
      <label>Name: <input type="text" id="name"></label><br><br>
      <label>Email: <input type="email" id="email"></label><br><br>
      <label>Phone: <input type="text" id="phone"></label><br><br>
      <label>Location: <input type="text" id="location"></label><br><br>
      <label>Summary: <textarea id="summary"></textarea></label><br><br>
      <label>Education: <textarea id="education"></textarea></label><br><br>
      <label>Skills: <textarea id="skills"></textarea></label><br><br>
      <label>Experience: <textarea id="experience"></textarea></label><br><br>
      <label>Projects: <textarea id="projects"></textarea></label><br><br>
      <label>Upload Photo: <input type="file" id="photo" accept="image/*"></label><br><br>
      <button type="button" onclick="generateCV()">Generate CV</button>
    </form>

    <div id="resume" class="resume" style="display:none;">
      <img id="resumePhoto" src="" alt="Profile Photo">
      <h2 id="resumeName"></h2>
      <p id="resumeContact"></p>

      <div class="section">
        <h3>Summary</h3>
        <p id="resumeSummary"></p>
      </div>

      <div class="section">
        <h3>Education</h3>
        <p id="resumeEducation"></p>
      </div>

      <div class="section">
        <h3>Skills</h3>
        <p id="resumeSkills"></p>
      </div>

      <div class="section">
        <h3>Experience</h3>
        <p id="resumeExperience"></p>
      </div>

      <div class="section">
        <h3>Projects</h3>
        <p id="resumeProjects"></p>
      </div>
    </div>
  </div>

  <script>
    function generateCV() {
      document.getElementById("resumeName").innerText = document.getElementById("name").value;
      document.getElementById("resumeContact").innerText =
        "Email: " + document.getElementById("email").value +
        " | Phone: " + document.getElementById("phone").value +
        " | Location: " + document.getElementById("location").value;

      document.getElementById("resumeSummary").innerText = document.getElementById("summary").value;
      document.getElementById("resumeEducation").innerText = document.getElementById("education").value;
      document.getElementById("resumeSkills").innerText = document.getElementById("skills").value;
      document.getElementById("resumeExperience").innerText = document.getElementById("experience").value;
      document.getElementById("resumeProjects").innerText = document.getElementById("projects").value;

      // Handle photo upload
      const photoInput = document.getElementById("photo");
      const resumePhoto = document.getElementById("resumePhoto");
      if (photoInput.files && photoInput.files[0]) {
        resumePhoto.src = URL.createObjectURL(photoInput.files[0]);
      }

      document.getElementById("resume").style.display = "block";
    }
  </script>
</body>
</html>
