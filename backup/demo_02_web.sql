/*
 Navicat MySQL Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50639
 Source Host           : localhost:3306
 Source Schema         : demo_02_web

 Target Server Type    : MySQL
 Target Server Version : 50639
 File Encoding         : 65001

 Date: 20/11/2018 13:37:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for blogs
-- ----------------------------
DROP TABLE IF EXISTS `blogs`;
CREATE TABLE `blogs`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_image` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `summary` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_created_at`(`created_at`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of blogs
-- ----------------------------
INSERT INTO `blogs` VALUES ('0015426280808014eb71196eba6464d940450661cb42ce7000', '1', 'Administrator', 'http://test.download.cycore.cn/test/5ed5fc74-f110-42df-ade8-c5a2f10d572a.png', '博客2', '新增数据', '新增数据的内容', 1542628080.80147);

-- ----------------------------
-- Table structure for comments
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `blog_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_image` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_created_at`(`created_at`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of comments
-- ----------------------------
INSERT INTO `comments` VALUES ('001542684908575e9806878c0244974b556a7cf5ebf2960000', '0015426280808014eb71196eba6464d940450661cb42ce7000', '1', 'Administrator', 'http://test.download.cycore.cn/test/5ed5fc74-f110-42df-ade8-c5a2f10d572a.png', '评论一下', 1542684908.57507);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `passwd` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `image` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_email`(`email`) USING BTREE,
  INDEX `idx_created_at`(`created_at`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('00154261167414899282f1645754a8b9abd66008c86ebe7000', 'cs@example.com', '41bb867e4f0ba0351b882a26c375506f16ba3ed9', 0, 'cs', 'http://test.download.cycore.cn/test/5ed5fc74-f110-42df-ade8-c5a2f10d572a.png', 1542611753.52476);
INSERT INTO `users` VALUES ('0015426857661739b219265a3fc4c328d4e147aeef6a41b000', '123asd@example.com', '7d69346f087a796c11007832a0f1010f89a84310', 0, '123asd', 'http://test.download.cycore.cn/test/5ed5fc74-f110-42df-ade8-c5a2f10d572a.png', 1542685766.17376);
INSERT INTO `users` VALUES ('1', 'admin@example.com', '4b033db597e9f9b14dfe43228ed2391a05f8e7ec', 1, 'Administrator', 'http://test.download.cycore.cn/test/5ed5fc74-f110-42df-ade8-c5a2f10d572a.png', 1);
INSERT INTO `users` VALUES ('2', 'test@example.com', '4b033db597e9f9b14dfe43228ed2391a05f8e7ec', 0, 'Test', 'http://test.download.cycore.cn/test/5ed5fc74-f110-42df-ade8-c5a2f10d572a.png', 2);

SET FOREIGN_KEY_CHECKS = 1;
