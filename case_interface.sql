/*
 Navicat Premium Data Transfer

 Source Server         : mysql8.0(cs)
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : 192.168.8.8:3306
 Source Schema         : istester

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 12/05/2020 09:33:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for case_interface
-- ----------------------------
DROP TABLE IF EXISTS `case_interface`;
CREATE TABLE `case_interface`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name_interface` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '接口名称',
  `exe_lever` int(0) NULL DEFAULT NULL COMMENT '执行优先级',
  `exe_model` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '执行方式',
  `url_interface` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '接口地址',
  `header_interface` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '接口请求的头文件，可以',
  `param_interface` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '接口请求参数',
  `result_interface` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '接口返回结果',
  `code_to_compare` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '特比较的code值，用户自定义，例如returnCode和code等',
  `code_actual` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '接口实际返回的code值',
  `code_expect` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '接口预期code值',
  `result_code_compare` int(0) NULL DEFAULT NULL COMMENT 'code比较结果，1-pass，2-无待比参数，3-比较出错，4-返回包不合法，9-系统异常',
  `params_to_compare` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '接口比较参数集合，用于比较参数的完整性',
  `param_actual` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '接口实际返回参数',
  `result_params_compare` int(0) NULL DEFAULT NULL,
  `case_status` int(0) NULL DEFAULT NULL COMMENT '1有效  0无效',
  `create_time` timestamp(6) NULL DEFAULT NULL COMMENT '创建时间',
  `updata_time` timestamp(6) NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '接口用例表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
