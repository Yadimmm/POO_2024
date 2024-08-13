-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-08-2024 a las 15:02:05
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_spa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `id_cliente` int(11) NOT NULL,
  `id_persona` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`id_cliente`, `id_persona`) VALUES
(2, NULL),
(3, NULL),
(4, NULL),
(5, NULL),
(6, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id_empleado` int(11) NOT NULL,
  `id_persona` int(11) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `especialidad` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id_empleado`, `id_persona`, `password`, `especialidad`) VALUES
(1, NULL, 'M4n0fSte3l007$', 'masajista');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notificacion`
--

CREATE TABLE `notificacion` (
  `id_notificacion` int(11) NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `mensaje` text DEFAULT NULL,
  `fecha_envio` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `notificacion`
--

INSERT INTO `notificacion` (`id_notificacion`, `id_cliente`, `mensaje`, `fecha_envio`) VALUES
(1, NULL, 'Se han consultado las reservas existentes.', '2024-08-10 21:56:03'),
(2, 3, 'Reserva actualizada para el cliente ID 3.', '2024-08-10 21:58:31'),
(3, 5, 'Reserva creada para el cliente yadim pebes con el servicio Tratamiento Antiestrés.', '2024-08-10 22:58:41'),
(4, 5, 'Reserva creada para el cliente yadim pebes con el servicio Masaje Relajante.', '2024-08-10 23:14:05'),
(5, 5, 'Reserva actualizada para el cliente ID 5.', '2024-08-10 23:41:50'),
(6, 3, 'Reserva ID 2 eliminada para el cliente adanely.', '2024-08-10 23:47:11'),
(7, 6, 'Reserva creada para el cliente jose  kanzaki con el servicio Masaje con Piedras Calientes.', '2024-08-10 23:59:01'),
(8, 5, 'Reserva creada para el cliente yadim pebes con el servicio Masaje con Piedras Calientes.', '2024-08-10 23:59:52'),
(9, NULL, 'Se han consultado las reservas existentes.', '2024-08-11 00:00:24'),
(10, 5, 'Reserva ID 5 actualizada para el cliente yadim con el servicio Manicure Spa.', '2024-08-11 00:01:08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

CREATE TABLE `persona` (
  `id_persona` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `fecha_nacimiento` datetime NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `correo_electronico` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`id_persona`, `nombre`, `apellidos`, `fecha_nacimiento`, `telefono`, `correo_electronico`) VALUES
(1, 'yadier', 'perez', '2005-05-26 00:00:00', '6182222815', 'yadier472@gmail.com'),
(2, 'pablo', 'vazquez', '2005-05-26 00:00:00', '6182232921', 'pable@gmail.com'),
(3, 'adanely', 'chakalilla', '2005-02-22 00:00:00', '61869666969', 'chakalilla@gmail.com'),
(4, 'amisadai', 'ontiveros', '2005-04-23 00:00:00', '6181231234', 'ami@gmail.com'),
(5, 'yadim', 'pebes', '2005-05-05 00:00:00', '6183333816', 'archangelmysticalmx@gmail.com'),
(6, 'jose ', 'kanzaki', '2002-10-10 00:00:00', '6184445656', 'kanzaki@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reserva`
--

CREATE TABLE `reserva` (
  `id_reserva` int(11) NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_empleado` int(11) DEFAULT NULL,
  `id_servicio` int(11) DEFAULT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reserva`
--

INSERT INTO `reserva` (`id_reserva`, `id_cliente`, `id_empleado`, `id_servicio`, `fecha`, `hora`) VALUES
(3, 4, NULL, 10, '2024-08-14', '10:30:00'),
(4, 5, NULL, 9, '2024-08-19', '12:30:00'),
(5, 5, NULL, 6, '2024-08-16', '12:00:00'),
(6, 6, NULL, 7, '2024-08-11', '10:00:00'),
(7, 5, NULL, 7, '2024-08-14', '10:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio`
--

CREATE TABLE `servicio` (
  `id_servicio` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `duracion` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `servicio`
--

INSERT INTO `servicio` (`id_servicio`, `nombre`, `descripcion`, `duracion`, `precio`) VALUES
(1, 'Masaje Relajante', 'Masaje corporal completo para relajar y aliviar el estrés.', 60, 50.00),
(2, 'Masaje Terapéutico', 'Masaje enfocado en aliviar dolores musculares específicos.', 45, 55.00),
(3, 'Facial Rejuvenecedor', 'Tratamiento facial que hidrata y rejuvenece la piel.', 30, 40.00),
(4, 'Exfoliación Corporal', 'Tratamiento que elimina las células muertas de la piel.', 45, 45.00),
(5, 'Pedicure Spa', 'Pedicure completo con tratamiento hidratante y masaje.', 60, 35.00),
(6, 'Manicure Spa', 'Manicure completo con exfoliación e hidratación.', 45, 30.00),
(7, 'Masaje con Piedras Calientes', 'Masaje que utiliza piedras calientes para relajar los músculos.', 75, 70.00),
(8, 'Envoltura Corporal', 'Tratamiento que envuelve el cuerpo en productos nutritivos y calientes.', 90, 80.00),
(9, 'Tratamiento Antiestrés', 'Combinación de técnicas de masaje para aliviar el estrés acumulado.', 60, 65.00),
(10, 'Tratamiento Capilar', 'Tratamiento nutritivo para el cabello con masajes en el cuero cabelludo.', 30, 35.00);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`id_cliente`),
  ADD KEY `id_persona` (`id_persona`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id_empleado`),
  ADD KEY `id_persona` (`id_persona`);

--
-- Indices de la tabla `notificacion`
--
ALTER TABLE `notificacion`
  ADD PRIMARY KEY (`id_notificacion`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- Indices de la tabla `persona`
--
ALTER TABLE `persona`
  ADD PRIMARY KEY (`id_persona`);

--
-- Indices de la tabla `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`id_reserva`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_empleado` (`id_empleado`),
  ADD KEY `id_servicio` (`id_servicio`);

--
-- Indices de la tabla `servicio`
--
ALTER TABLE `servicio`
  ADD PRIMARY KEY (`id_servicio`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `notificacion`
--
ALTER TABLE `notificacion`
  MODIFY `id_notificacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `persona`
--
ALTER TABLE `persona`
  MODIFY `id_persona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `reserva`
--
ALTER TABLE `reserva`
  MODIFY `id_reserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `servicio`
--
ALTER TABLE `servicio`
  MODIFY `id_servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`);

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`);

--
-- Filtros para la tabla `notificacion`
--
ALTER TABLE `notificacion`
  ADD CONSTRAINT `notificacion_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`);

--
-- Filtros para la tabla `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `reserva_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  ADD CONSTRAINT `reserva_ibfk_2` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id_empleado`),
  ADD CONSTRAINT `reserva_ibfk_3` FOREIGN KEY (`id_servicio`) REFERENCES `servicio` (`id_servicio`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
