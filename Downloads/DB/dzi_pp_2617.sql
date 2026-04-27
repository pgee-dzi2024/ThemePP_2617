-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Време на генериране: 22 апр 2026 в 01:10
-- Версия на сървъра: 10.4.32-MariaDB
-- Версия на PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данни: `dzi_pp_2617`
--

-- --------------------------------------------------------

--
-- Структура на таблица `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура на таблица `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура на таблица `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Схема на данните от таблица `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Събитие при движение', 7, 'add_motionevent'),
(26, 'Can change Събитие при движение', 7, 'change_motionevent'),
(27, 'Can delete Събитие при движение', 7, 'delete_motionevent'),
(28, 'Can view Събитие при движение', 7, 'view_motionevent'),
(29, 'Can add Видео източник', 8, 'add_camerasource'),
(30, 'Can change Видео източник', 8, 'change_camerasource'),
(31, 'Can delete Видео източник', 8, 'delete_camerasource'),
(32, 'Can view Видео източник', 8, 'view_camerasource');

-- --------------------------------------------------------

--
-- Структура на таблица `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Схема на данните от таблица `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$64dZkuOCugCzPnKydWuWeq$ubcqT5zU7+/kQKodi+lJ7bpDnf4SJ5hnNITrv7XjrqY=', '2026-04-21 21:56:34.563282', 1, 'user_26', '', '', '', 1, 1, '2026-02-11 08:47:57.603297');

-- --------------------------------------------------------

--
-- Структура на таблица `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура на таблица `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура на таблица `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура на таблица `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Схема на данните от таблица `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'main', 'camerasource'),
(7, 'main', 'motionevent'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Структура на таблица `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Схема на данните от таблица `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-02-11 08:47:24.012263'),
(2, 'auth', '0001_initial', '2026-02-11 08:47:25.076490'),
(3, 'admin', '0001_initial', '2026-02-11 08:47:25.340096'),
(4, 'admin', '0002_logentry_remove_auto_add', '2026-02-11 08:47:25.358208'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2026-02-11 08:47:25.375104'),
(6, 'contenttypes', '0002_remove_content_type_name', '2026-02-11 08:47:25.492132'),
(7, 'auth', '0002_alter_permission_name_max_length', '2026-02-11 08:47:25.600003'),
(8, 'auth', '0003_alter_user_email_max_length', '2026-02-11 08:47:25.640527'),
(9, 'auth', '0004_alter_user_username_opts', '2026-02-11 08:47:25.656900'),
(10, 'auth', '0005_alter_user_last_login_null', '2026-02-11 08:47:25.750196'),
(11, 'auth', '0006_require_contenttypes_0002', '2026-02-11 08:47:25.756192'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2026-02-11 08:47:25.772177'),
(13, 'auth', '0008_alter_user_username_max_length', '2026-02-11 08:47:25.802794'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2026-02-11 08:47:25.835414'),
(15, 'auth', '0010_alter_group_name_max_length', '2026-02-11 08:47:25.868378'),
(16, 'auth', '0011_update_proxy_permissions', '2026-02-11 08:47:25.890726'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2026-02-11 08:47:25.920362'),
(18, 'sessions', '0001_initial', '2026-02-11 08:47:25.982333'),
(19, 'main', '0001_initial', '2026-04-21 21:55:26.091295'),
(20, 'main', '0002_alter_camerasource_stream_url', '2026-04-21 23:03:17.105991');

-- --------------------------------------------------------

--
-- Структура на таблица `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Схема на данните от таблица `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('irijic8mmzgttk8ot4lql2w8bzjoenp2', '.eJxVjMsOwiAQRf-FtSFI5TEu3fcbyAwMUjWQlHZl_HfbpAvdnnPufYuA61LC2nkOUxJXcRanX0YYn1x3kR5Y703GVpd5Irkn8rBdji3x63a0fwcFe9nWdgAw1qIDMmA4X5T2GYjAJgaK1nnSaFilgUBtEF220YAHNNolyuLzBdg_OAs:1wFJ58:f4uD7dsqW1Xz4nToHwN0eWxGCO3EHd88bFTFYbFZJqo', '2026-05-05 21:56:34.565826');

-- --------------------------------------------------------

--
-- Структура на таблица `main_camerasource`
--

CREATE TABLE `main_camerasource` (
  `id` bigint(20) NOT NULL,
  `name` varchar(120) NOT NULL,
  `source_type` varchar(20) NOT NULL,
  `stream_url` varchar(500) DEFAULT NULL,
  `device_index` int(10) UNSIGNED NOT NULL CHECK (`device_index` >= 0),
  `is_active` tinyint(1) NOT NULL,
  `sensitivity_threshold` int(10) UNSIGNED NOT NULL CHECK (`sensitivity_threshold` >= 0),
  `min_area` int(10) UNSIGNED NOT NULL CHECK (`min_area` >= 0),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Схема на данните от таблица `main_camerasource`
--

INSERT INTO `main_camerasource` (`id`, `name`, `source_type`, `stream_url`, `device_index`, `is_active`, `sensitivity_threshold`, `min_area`, `created_at`, `updated_at`) VALUES
(1, 'камера 1', 'ip', 'rtsp://admin:gimas1613@192.168.100.110:554/cam/realmonitor?channel=1&subtype=0', 0, 1, 25, 500, '2026-04-21 22:23:23.347572', '2026-04-21 23:05:25.558523');

-- --------------------------------------------------------

--
-- Структура на таблица `main_motionevent`
--

CREATE TABLE `main_motionevent` (
  `id` bigint(20) NOT NULL,
  `detected_at` datetime(6) NOT NULL,
  `message` varchar(255) NOT NULL,
  `frame_path` varchar(255) DEFAULT NULL,
  `camera_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Схема на данните от таблица `main_motionevent`
--

INSERT INTO `main_motionevent` (`id`, `detected_at`, `message`, `frame_path`, `camera_id`) VALUES
(1, '2026-04-21 23:03:57.811706', 'Движение засечено', NULL, 1),
(2, '2026-04-21 23:04:00.014272', 'Движение засечено', NULL, 1),
(3, '2026-04-21 23:04:02.023837', 'Движение засечено', NULL, 1),
(4, '2026-04-21 23:04:04.086955', 'Движение засечено', NULL, 1),
(5, '2026-04-21 23:04:06.121189', 'Движение засечено', NULL, 1),
(6, '2026-04-21 23:04:08.161767', 'Движение засечено', NULL, 1),
(7, '2026-04-21 23:04:10.206591', 'Движение засечено', NULL, 1),
(8, '2026-04-21 23:04:13.041990', 'Движение засечено', NULL, 1),
(9, '2026-04-21 23:04:15.786388', 'Движение засечено', NULL, 1),
(10, '2026-04-21 23:04:17.943297', 'Движение засечено', NULL, 1),
(11, '2026-04-21 23:04:20.104531', 'Движение засечено', NULL, 1),
(12, '2026-04-21 23:04:22.184336', 'Движение засечено', NULL, 1),
(13, '2026-04-21 23:04:25.108525', 'Движение засечено', NULL, 1),
(14, '2026-04-21 23:04:27.746909', 'Движение засечено', NULL, 1),
(15, '2026-04-21 23:04:30.004562', 'Движение засечено', NULL, 1),
(16, '2026-04-21 23:04:32.051966', 'Движение засечено', NULL, 1),
(17, '2026-04-21 23:04:34.103760', 'Движение засечено', NULL, 1),
(18, '2026-04-21 23:04:36.186869', 'Движение засечено', NULL, 1),
(19, '2026-04-21 23:04:40.410021', 'Движение засечено', NULL, 1),
(20, '2026-04-21 23:04:43.147008', 'Движение засечено', NULL, 1),
(21, '2026-04-21 23:04:46.192176', 'Движение засечено', NULL, 1),
(22, '2026-04-21 23:04:50.067647', 'Движение засечено', NULL, 1),
(23, '2026-04-21 23:04:54.057441', 'Движение засечено', NULL, 1),
(24, '2026-04-21 23:04:56.131055', 'Движение засечено', NULL, 1),
(25, '2026-04-21 23:05:50.598172', 'Движение засечено', NULL, 1),
(26, '2026-04-21 23:05:53.134217', 'Движение засечено', NULL, 1),
(27, '2026-04-21 23:05:55.216380', 'Движение засечено', NULL, 1),
(28, '2026-04-21 23:05:58.213811', 'Движение засечено', NULL, 1),
(29, '2026-04-21 23:06:01.057064', 'Движение засечено', NULL, 1),
(30, '2026-04-21 23:06:04.016038', 'Движение засечено', NULL, 1),
(31, '2026-04-21 23:06:06.172400', 'Движение засечено', NULL, 1),
(32, '2026-04-21 23:06:10.088318', 'Движение засечено', NULL, 1),
(33, '2026-04-21 23:06:12.134246', 'Движение засечено', NULL, 1),
(34, '2026-04-21 23:06:14.202754', 'Движение засечено', NULL, 1),
(35, '2026-04-21 23:06:17.063407', 'Движение засечено', NULL, 1),
(36, '2026-04-21 23:06:20.134051', 'Движение засечено', NULL, 1),
(37, '2026-04-21 23:06:22.203548', 'Движение засечено', NULL, 1),
(38, '2026-04-21 23:06:25.012861', 'Движение засечено', NULL, 1),
(39, '2026-04-21 23:06:27.053931', 'Движение засечено', NULL, 1),
(40, '2026-04-21 23:06:30.123665', 'Движение засечено', NULL, 1),
(41, '2026-04-21 23:06:32.204968', 'Движение засечено', NULL, 1),
(42, '2026-04-21 23:06:35.081355', 'Движение засечено', NULL, 1),
(43, '2026-04-21 23:06:38.082952', 'Движение засечено', NULL, 1),
(44, '2026-04-21 23:06:40.123048', 'Движение засечено', NULL, 1),
(45, '2026-04-21 23:06:42.204033', 'Движение засечено', NULL, 1),
(46, '2026-04-21 23:06:45.032804', 'Движение засечено', NULL, 1),
(47, '2026-04-21 23:06:47.054771', 'Движение засечено', NULL, 1),
(48, '2026-04-21 23:06:50.123312', 'Движение засечено', NULL, 1),
(49, '2026-04-21 23:06:52.163919', 'Движение засечено', NULL, 1),
(50, '2026-04-21 23:06:54.166083', 'Движение засечено', NULL, 1),
(51, '2026-04-21 23:06:57.053003', 'Движение засечено', NULL, 1),
(52, '2026-04-21 23:07:01.861150', 'Движение засечено', NULL, 1);

--
-- Indexes for dumped tables
--

--
-- Индекси за таблица `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Индекси за таблица `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Индекси за таблица `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Индекси за таблица `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Индекси за таблица `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Индекси за таблица `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Индекси за таблица `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Индекси за таблица `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Индекси за таблица `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Индекси за таблица `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Индекси за таблица `main_camerasource`
--
ALTER TABLE `main_camerasource`
  ADD PRIMARY KEY (`id`);

--
-- Индекси за таблица `main_motionevent`
--
ALTER TABLE `main_motionevent`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_motionevent_camera_id_372f64f3_fk_main_camerasource_id` (`camera_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `main_camerasource`
--
ALTER TABLE `main_camerasource`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `main_motionevent`
--
ALTER TABLE `main_motionevent`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- Ограничения за дъмпнати таблици
--

--
-- Ограничения за таблица `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ограничения за таблица `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ограничения за таблица `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения за таблица `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения за таблица `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения за таблица `main_motionevent`
--
ALTER TABLE `main_motionevent`
  ADD CONSTRAINT `main_motionevent_camera_id_372f64f3_fk_main_camerasource_id` FOREIGN KEY (`camera_id`) REFERENCES `main_camerasource` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
