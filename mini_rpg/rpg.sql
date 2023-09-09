-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : db
-- Généré le : sam. 09 sep. 2023 à 20:02
-- Version du serveur : 8.1.0
-- Version de PHP : 8.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `rpg`
--

-- --------------------------------------------------------

--
-- Structure de la table `arme_amelioree`
--

CREATE TABLE `arme_amelioree` (
  `id` int NOT NULL,
  `nom` varchar(30) NOT NULL,
  `atk` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `arme_amelioree`
--

INSERT INTO `arme_amelioree` (`id`, `nom`, `atk`) VALUES
(1, 'épée en bois', 2),
(2, 'épée en fer', 4),
(3, 'épée en acier', 6),
(4, 'épée en platine', 8),
(5, 'griffe de chat', 1000),
(6, 'arc ', 6),
(7, 'evantail celeste', 9),
(8, 'bec de canard', 5);

-- --------------------------------------------------------

--
-- Structure de la table `monstres`
--

CREATE TABLE `monstres` (
  `id` int NOT NULL,
  `classe` varchar(50) NOT NULL,
  `pv` int NOT NULL,
  `attaque` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `monstres`
--

INSERT INTO `monstres` (`id`, `classe`, `pv`, `attaque`) VALUES
(1, 'Gobelin', 15, 10),
(2, 'Orc', 50, 20),
(3, 'Ogre', 75, 25),
(4, 'Slime', 5, 5),
(5, 'Dragon', 200, 50),
(6, 'marsouin', 300, 2);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `arme_amelioree`
--
ALTER TABLE `arme_amelioree`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `monstres`
--
ALTER TABLE `monstres`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `arme_amelioree`
--
ALTER TABLE `arme_amelioree`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `monstres`
--
ALTER TABLE `monstres`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
