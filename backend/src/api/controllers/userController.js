// userController.js

// 获取用户信息
exports.getUser = (req, res) => {
  // 可以添加获取用户信息的逻辑
  res.send("User details for user " + req.params.id);
};

// 更新用户信息
exports.updateUser = (req, res) => {
  // 可以添加更新用户信息的逻辑
  res.send("Update user " + req.params.id);
};

