from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "MovieMix"
app.version = "0.0.1"

#Captura de errores
app.add_middleware(ErrorHandler)

#Rutas para Movies
app.include_router(movie_router)

#Rutas para Users
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'], response_class=HTMLResponse)
def message():
    return """
		<html>
			<head>
				<title>MovieMix</title>
				<style>
					body {
						background-color: #7469B6;
						margin: 0;
						padding: 0;
						display: flex;
						justify-content: center;
						align-items: center;
						height: 100%;
						width: 100%;
						text-align: center;
					}
					.container {
						padding: 0px;
					}
					h1 {
						transition: color 0.5s ease-in-out;
						font-size: 7rem;
						font-family: "Agbalumo", system-ui;
						font-weight: 800;
						font-style: normal;
						transition: color 1s ease-in-out;
						background-image: linear-gradient(45deg, #E1AFD1, #FFDB5C, #C3FF93, #FF70AB);
						background-size: 200% 200%;
						background-clip: text;
						-webkit-background-clip: text;
						color: transparent;
						cursor: pointer;
						padding: 0;
						margin: 0;
					}
					h1:hover {
						animation: gradient-rotate 4s infinite;
					}
					p {
						font-family: "Montserrat", sans-serif;
						font-optical-sizing: auto;
						font-weight: 400;
						font-style: normal;
						color: #FFE6E6;
					}
					#description {
						font-size: 1.2vw;
					}
					#author {
						font-size: 0.7vw;
					}

					@keyframes gradient-rotate {
						0% {
							background-position: 0% 50%;
						}
						25% {
							background-position: 100% 75%;
						}
						50% {
							background-position: 100% 50%;
						}
						50% {
							background-position: 75% 100%;
						}
						100% {
							background-position: 0% 50%;
						}
					}
				</style>
				<link rel="preconnect" href="https://fonts.googleapis.com">
				<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
				<link href="https://fonts.googleapis.com/css2?family=Agbalumo&family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
			</head>
			<body>
				<div class="container">
					<h1>MovieMix</h1>
					<p id="description">API de Movies recomendadas</p>
					<p id="author">by @mstovarh</p>
				</div>
			</body>
		</html>
    """