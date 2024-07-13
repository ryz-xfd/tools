<!DOCTYPE html>
<!-- Github : ryz-xfd
	Youtube : ryz. 
-->
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Gemini</title>
	<!-- Github : ryz-xfd
	Youtube : ryz. 
-->
	<style>
		body {
			font-family: Arial, sans-serif;
			line-height: 1.6;
			margin: 20px;
			padding: 0;
			box-sizing: border-box;
		}
		.form {
			margin-bottom: 20px;
		}
		.form label {
			font-weight: bold;
		}
		.form input[type="text"] {
			padding: 8px;
			border: 1px solid #ccc;
			border-radius: 4px;
			margin-right: 10px;
			width: 200px;
		}
		.form button {
			padding: 8px 12px;
			border: none;
			background-color: #007bff;
			color: #fff;
			cursor: pointer;
			border-radius: 4px;
		}
		.output label {
			font-weight: bold;
		}
		.output textarea {
			width: 100%;
			height: 150px;
			padding: 8px;
			border: 1px solid #ccc;
			border-radius: 4px;
			resize: vertical;
		}
	</style>
</head>
<body>
<!-- Github : ryz-xfd
	Youtube : ryz. 
-->
<h1>Gemini | RYZ</h1>
<div class="form">
	<label>ASK GEMINI : </label>
	<input type="text" name="" id="input" placeholder="Code By ryz." value="">
	<button id="submit"><span class="material-symbols-outlined">search</span></button>
</div>
<div class="output">
	<label>OUTPUT</label>
	<textarea readonly id="output"></textarea>
</div>
<!--  <script type="importmap">
      {
        "imports": {
          "@google/generative-ai": "https://esm.run/@google/generative-ai"
        }
      }
    </script> -->
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script type="module">
	 import { GoogleGenerativeAI } from "@google/generative-ai";
     // const API_KEY = "AI-##########################"; 
      const genAI = new GoogleGenerativeAI(API_KEY);
      // const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});
	// async function run(string) {
	// 	const prompt = string;
	// 	const result = await model.generateContent(prompt);
	// 	const response = await result.response;
	// 	const text = await response.text();
	// 	return text;
	// }
	function thongbao(type, title, text) {
		Swal.fire({
			title: title,
			text: text,
			icon: type,
			// timer: 3000 // Đóng cửa sổ sau 3 giây (3000 milliseconds)
		// }).then(function () {
		// 	window.location.href = "index.php";
		// });
	}
	document.getElementById('submit').addEventListener("click", function () {
		const string = document.getElementById('input').value;
		if (string.trim() === "") {
			// thongbao('error', 'ERROR!', "Prompt Null");
		} else {
			run(string)
				.then(result => {
					// document.getElementById('output').value = result;
				})
				.catch(error => {
					// console.error(error);
					Swal.fire({
						icon: 'error',
						title: 'Oops...',
						text: 'Something went wrong!'
					});
				});
		}
	});
</script>
<!-- Github : ryz-xfd
	Youtube : ryz. 
-->
</body>
<!-- Github : ryz-xfd
	Youtube : ryz. 
-->
</html>
<!-- Github : ryz-xfd
	Youtube : ryz. 
-->