# TODO

- [x] Inspect existing base layout and global CSS.
- [x] Inspect current templates and how they fit the existing CSS selectors.
- [ ] Fix staticfiles warning (`STATICFILES_DIRS` points to a non-existent directory).
- [ ] Fix `ImageField` warning by installing Pillow (or switching to CharField if you don’t need images).
- [ ] Confirm CSS is loading by checking browser DevTools Network tab for `/static/style.css`.
- [ ] If still failing, ensure `staticfiles` urls are served in development (`urlpatterns += static(...)`).

