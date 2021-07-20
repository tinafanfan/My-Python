# Use latex

Insert the following code in the beginning of your markdown file.

```jsx
<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']] && [['$$', '$$']]
            }
        });
    </script>
</head>
```

所有的文件都要套用的話可在主題那邊調整，請參考

[https://zhuanlan.zhihu.com/p/36302775](https://zhuanlan.zhihu.com/p/36302775)

# Resize the image inline article

Use html code instead of markdown to insert image.

Original markdown code:

```markdown
![/img/TD-learning/Untitled-0.png](/img/TD-learning/Untitled-0.png)
```

Change to:

```html
<img src="/img/TD-learning/Untitled-0.png" width="50%">
```

# Center the image through css setting

Adjust the css code in the file: /Users/tina/Github-page-ytfanfan/exampleSite/themes/hugo-future-imperfect-slim/assets/css/normalize.css. To center an image, set left and right margin to auto and make it into a block element.

```css
img {
  border-style: none; # this is the original setting
  display: block;
  margin-left: auto;
  margin-right: auto;
}
```
