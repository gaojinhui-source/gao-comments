# gao-comments
基于flask实现的留言板

需求链接详情：https://lexiangla.com/teams/k100003/docs/0f0baef08fbd11e891fa525400bab841?lxref=search-company&company_from=a2d7f952d35411e7b621525400ebd317


## 功能描述
1. 留言板基本增删改查
2. 登录登出功能（基于手机号登录以及wx登录）
3. 用户注册（提供接口，但无前端）

## 方案

### db设计

#### 表结构
1. 留言表
```
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `content_body` varchar(4096) NOT NULL COMMENT '????????',
  `user_id` int(11) NOT NULL COMMENT '?û?id',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '????ʱ??',
  `mtime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '????ʱ??',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4
```
2. 用户表
```
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `nickname` varchar(256) NOT NULL COMMENT '?ǳ?',
  `phone` varchar(32) NOT NULL COMMENT '?ֻ???',
  `email` varchar(64) DEFAULT NULL COMMENT '????',
  `sex` tinyint(4) NOT NULL DEFAULT '1' COMMENT '?Ա? 1 ?? 0 Ů',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '????ʱ??',
  `mtime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '????ʱ??',
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=100003 DEFAULT CHARSET=utf8mb4 COMMENT='?û??
```
3. 用户企业微信映射表
```
CREATE TABLE `qywx_user_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `wx_id` varchar(256) NOT NULL COMMENT ' wx账号id',
  `user_id` int(11) NOT NULL COMMENT '统一账号',
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `mtime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `wx_id` (`wx_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='绑定关系表'
```

#### E-R图

