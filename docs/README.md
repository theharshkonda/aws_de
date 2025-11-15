# AWS Data Engineer Bootcamp - Website

A beautiful, interactive learning dashboard for the AWS Data Engineer 2-Month Bootcamp.

## 🌐 Live Website

Visit: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`

## ✨ Features

### 📊 Progress Tracking
- Track daily study hours
- Monitor task completion
- View weekly progress charts
- Export/import your progress data

### 📚 8-Week Curriculum
- Detailed weekly modules
- Day-by-day learning plans
- Interactive checklists
- Resource links

### 🎯 Learning Tools
- Daily task manager
- Learning log with notes
- Progress visualization
- Timeline roadmap

### 📱 Fully Responsive
- Works on all devices
- Mobile-friendly navigation
- Touch-optimized interface

## 🚀 Quick Start

### For Users (Learners)

1. Visit the website
2. Start with Week 1-2
3. Check off tasks as you complete them
4. Log your daily hours
5. Track your progress!

### For Developers (Customization)

1. Clone this repository
2. Edit files in root directory:
   - `index.html` - Main page
   - `assets/css/style.css` - Styling
   - `assets/js/main.js` - Functionality
   - `pages/*.html` - Week pages

3. Test locally:
   - Open `index.html` in browser
   - Or use a local server:
     ```bash
     python -m http.server 8000
     ```
   - Visit `http://localhost:8000`

4. Deploy to GitHub Pages:
   - Push changes to repository
   - Enable GitHub Pages in settings
   - Select `main` branch and `/ (root)` folder

## 📁 File Structure

```
docs/
├── index.html              # Main homepage
├── _config.yml            # GitHub Pages configuration
├── README.md              # This file
│
├── assets/
│   ├── css/
│   │   └── style.css      # All styles
│   ├── js/
│   │   └── main.js        # All JavaScript
│   └── images/            # (Add your images here)
│
└── pages/
    ├── week1-2.html       # Week 1-2 details
    ├── week3.html         # Week 3 details
    ├── week4.html         # Week 4 details
    ├── week5.html         # Week 5 details
    ├── week6.html         # Week 6 details
    ├── week7.html         # Week 7 details
    ├── week8.html         # Week 8 details
    ├── interview.html     # Interview prep
    ├── setup.html         # Setup guide
    └── aws-setup.html     # AWS Free Tier guide
```

## 🎨 Customization

### Change Colors

Edit `assets/css/style.css`:

```css
:root {
    --primary-color: #FF9900;      /* Change primary color */
    --secondary-color: #232F3E;    /* Change secondary color */
    --accent-color: #1E88E5;       /* Change accent color */
    /* ... more colors */
}
```

### Update Content

Edit HTML files directly:
- `index.html` - Homepage content
- `pages/week*.html` - Weekly content

### Add Pages

1. Create new HTML file in `pages/`
2. Copy structure from existing page
3. Update navigation links

## 💾 Data Storage

### Local Storage

All progress is saved in browser's localStorage:
- `bootcamp_progress` - Overall progress stats
- `learning_logs` - Daily learning logs
- `daily_tasks` - Task list
- `weekly_progress` - Week-by-week completion

### Export/Import

Users can:
- Export progress as JSON file
- Import previously saved progress
- Share progress with others

## 🔧 Technical Details

### Technologies Used

- **HTML5** - Structure
- **CSS3** - Styling with CSS Variables
- **JavaScript (ES6+)** - Interactivity
- **Chart.js** - Progress charts
- **Font Awesome** - Icons
- **LocalStorage API** - Data persistence

### Browser Support

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Mobile browsers

### Performance

- Fast loading (< 1 second)
- No external dependencies (except CDN fonts/icons)
- Optimized CSS and JavaScript
- Responsive images

## 🐛 Known Issues

None currently. Report issues if you find any!

## 📝 To-Do (Future Enhancements)

- [ ] Add dark mode toggle
- [ ] PDF export of progress reports
- [ ] Calendar view for study logs
- [ ] Pomodoro timer integration
- [ ] Study streak tracker
- [ ] Achievement badges
- [ ] Social sharing
- [ ] Mobile app version

## 🤝 Contributing

This is a personal learning dashboard, but feel free to:
1. Fork the repository
2. Make improvements
3. Use for your own learning journey

## 📄 License

Free to use for personal and educational purposes.

## 🙏 Credits

- Built with dedication for aspiring data engineers
- Icons by Font Awesome
- Charts by Chart.js
- Inspired by modern learning platforms

## 📞 Support

For questions or issues:
1. Check the documentation
2. Review browser console for errors
3. Ensure JavaScript is enabled
4. Clear cache and reload

## 🎯 Goals

This dashboard helps you:
- ✅ Stay organized throughout the 8-week bootcamp
- ✅ Track progress visually
- ✅ Maintain consistency
- ✅ Build accountability
- ✅ Celebrate milestones
- ✅ Achieve your goal of becoming an AWS Data Engineer!

---

**Start your journey today!** 🚀

Visit the website and begin Week 1!
