from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse(
        """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <title>Recuros Humanos</title>
</head>

<body style="background-color: black;">
    <div>
        <nav>
            <ul class="nav justify-content-end">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Exit
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-box-arrow-right" viewBox="0 0 16 16">
                            <path fill-rule="evenodd"
                                d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0z" />
                            <path fill-rule="evenodd"
                                d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708z" />
                        </svg>
                    </a>
                </li>
            </ul>
        </nav>
    </div>
    <div class="container-fluid">
        <main>
            <div class="container">
                <nav class="navbar navbar-expand-lg navbar-dark">
                    <div class="container-fluid">
                        <a class="navbar-brand fw-bold" href="#">
                            EMPLEADOS
                        </a>
                        <!-- Botón hamburguesa -->
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                            data-bs-target="#navbarNav">
                            <span class="navbar-toggler-icon"></span>
                        </button>

                        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                            <ul class="navbar-nav">
                                <li class="nav-item">
                                    <a class="nav-link active" href="#adicionar">
                                        Adicionar Empleado
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#asistencia">
                                        Asistencia Control
                                    </a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="#organigrama">
                                        Organigrama
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                <section>
                    <table class="table">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Primer Nombre</th>
                                <th scope="col">Segundo Nombre</th>
                                <th scope="col">PrimerApellido</th>
                                <th scope="col">SegundoApellido</th>
                                <th scope="col">Cargo</th>
                                <th scope="col">Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row">1</th>
                                <td>Juan</td>
                                <td>Felipe</td>
                                <td>Delgadillo</td>
                                <td>Vanegas</td>
                                <td>Administrador</td>
                                <td><button type="button" class="btn btn-primary">Información</button></td>
                            </tr>
                            <tr>
                                <th scope="row">1</th>
                                <td>Juan</td>
                                <td>Felipe</td>
                                <td>Delgadillo</td>
                                <td>Vanegas</td>
                                <td>Administrador</td>
                                <td><button type="button" class="btn btn-primary">Información</button></td>
                            </tr>
                            <tr>
                                <th scope="row">1</th>
                                <td>Juan</td>
                                <td>Felipe</td>
                                <td>Delgadillo</td>
                                <td>Vanegas</td>
                                <td>Administrador</td>
                                <td><button type="button" class="btn btn-primary">Información</button></td>
                            </tr>
                        </tbody>
                    </table>
                </section>
            </div>
        </main>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
        crossorigin="anonymous"></script>
</body>

</html>
        """
    )
    
"""
def homeParameters(request, name, age):
    return HttpResponse("Hello, " + name + ". You are " + age + " years old.")
"""