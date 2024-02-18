# Gif Player

Gif Player is a dash component that follows the same approach as here: [dash-gif-player](https://pypi.org/project/dash-gif-component/). The only difference is that I made a few changes so the component now can receive: id, height and width.

```
gif_player.GifPlayer(
        id='input',
        gif='https://urltogif/gif.gif',
        still='https://urltogif/picture.png',
        height=300,
        width=500
    )
```

I added those things because they were neccesary to the project that I was working on, I take no credit for this package I would've liked to add this features to the actual package but the owner didn't reply to me.

# Acknowledgments

* [Maxim Kupfer](https://pypi.org/user/mbkupfer/) - For developing the component.