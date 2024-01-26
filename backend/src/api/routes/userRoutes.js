// userRoutes.js

const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');

// 路由指向控制器的方法
router.get('/user/:id', userController.getUser);
router.post('/user/:id', userController.updateUser);

module.exports = router;