<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Marked in the browser</title>
</head>
<body>
  <div id="content"></div>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script>
    // 使用 Fetch API 获取同目录下的 md.md 文件内容
    fetch('md.md')  // 使用相对路径
      .then(response => response.text())
      .then(markdownContent => {
        // 使用 marked.js 将 Markdown 转换为 HTML 并插入到页面中
        document.getElementById('content').innerHTML = marked.parse(markdownContent);
      })
      .catch(error => {
        console.error('Error fetching Markdown file:', error);
      });
  </script>
</body>
</html>
