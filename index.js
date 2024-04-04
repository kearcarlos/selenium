const express = require("express");
const app = express();

app.use(express.static("public"));
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

// ELEMENTOS PARA CONECTAR CON MONGODB
// SIEMPRE IGUALES. DOS FORMAS.
// MONGOOSE Y MONGO CLIENT. EMPEZAMOS CON MC POR ESTABILIDAD.

const mongodb = require("mongodb");
let MongoClient = mongodb.MongoClient;

// CONEXIÓN CON MONGODB VÍA MONGO CLIENT

MongoClient.connect("mongodb://0.0.0.0:27017/", function (err, client) {
  if (err != null) {
    console.log(err);
    console.log("No se ha podido conectar con MongoDB");
  } else {
    app.locals.db = client.db("EjercicioHotel");
    console.log(
      "Conexión correcta a la base de datos EjercicioHotel de MongoDB"
    );
  }
});

// AQUÍ LAS RUTAS
app.post("/reservas/registro", function (req, res) {
  let nombre = req.body.nombre;
  let apellido = req.body.apellido;
  let dni = req.body.dni;
  let numHab = req.body.numHab;
  let fechaCheckIn = req.body.fechaCheckIn;
  let fechaCheckOut = req.body.fechaCheckOut;

  let reserva = {
    nombre: nombre,
    apellido: apellido,
    dni: dni,
    numHab: numHab,
    fechaCheckIn: fechaCheckIn,
    fechaCheckOut: fechaCheckOut,
  };

  req.app.locals.db
    .collection("clientes")
    .find({ dni: dni })
    .toArray(function (err, datos) {
      if (datos.length == 0) {
        res.send({ mensaje: "cliente no encontrado" });
      } else {
        // requerimos a otra colección
        app.locals.db
          .collection("habitaciones")
          .find({ numHab: parseInt(numHab) })
          .toArray(function (err, datos) {
            if (datos.length == 0) {
              res.send({ mensaje: "Error. La habitación no existe" });
            } else if (datos[0].estado == "ocupada") {
              res.send({
                mensaje: "Error. Habitación ya reservada, intente otra",
              });
            } else {
              req.app.locals.db
                .collection("habitaciones")
                .updateOne(
                  { numHab: parseInt(numHab) },
                  { $set: { estado: "ocupada" } }
                );
              req.app.locals.db
                .collection("reservas")
                .insertOne(reserva, function (err, res) {
                 console.log("habitación reservada con éxito")
                });
            }
          });
      }
    });
});

// PETICIÓN DE TIPO PUT: EDITA LA INFO *EC
app.put("/clientes", (req, res) => {
  let nuevo = {
    nombre: req.body.nombre,
    apellido: req.body.apellido,
    dni: req.body.dni,
  };

  // AHORA TENDRÉ QUE MIRAR EN LA BASE DE DATOS
  // SI HAY COINCIDENCIA Y, EN CASO DE QUE
  // LA HAYA, MODIFICAR EL RESTO DE VALORES

  app.locals.db.collection("clientes").updateOne(
    { nombre: nuevo.nombre },
    {
      $set: {
        apellido: nuevo.apellido,
        dni: nuevo.dni,
      },
    },
    function (err, res) {
      if (err != null) {
        console.log(err);
      } else {
        console.log("Cliente modificado correctamente");
      }
    }
  );
});
// AQUÍ LAS RUTAS mostrar **
app.get("/clientes", function (req, res) {
  app.locals.db
    .collection("clientes")
    .find()
    .toArray(function (err, datos) {
      if (err != null) {
        console.log(err);
      } else {
        console.log(datos);
        res.send(datos);
      }
    });
});

app.get("/habitaciones", function (req, res) {
  app.locals.db
    .collection("habitaciones")
    .find()
    .toArray(function (err, datos) {
      if (err != null) {
        console.log(err);
      } else {
        console.log(datos);
        res.send(datos);
      }
    });
});

app.get("/reservas", function (req, res) {
  app.locals.db
    .collection("reservas")
    .find()
    .toArray(function (err, datos) {
      if (err != null) {
        console.log(err);
      } else {
        console.log(datos);
        res.send(datos);
      }
    });
});

// Y EL PUERTO

app.listen(process.env.PORT || 3000, () => {
  console.log("Servidor (Express JS) conectado correctamente al puerto 3000");
});
