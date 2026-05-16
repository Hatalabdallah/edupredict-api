# 🤝 Contributing to EduPredict

Thank you for your interest in contributing to **EduPredict: Student Success Analytics**! We welcome contributions from the community.



## 📋 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [hatalabdallah@gmail.com](mailto:hatalabdallah@gmail.com).



## 🚀 How Can I Contribute?

### 🐛 Reporting Bugs

1. **Search existing issues** — your bug may already be reported
2. If not, **open a new issue** using the Bug Report template
3. Include:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected behavior vs actual behavior
   - Screenshots if applicable
   - Your environment (OS, Python version, etc.)

### 💡 Suggesting Enhancements

1. **Search existing issues** — your enhancement may already be suggested
2. Open a new issue using the Feature Request template
3. Describe:
   - The problem your enhancement solves
   - Your proposed solution
   - Any alternatives you've considered

### 🔧 Pull Requests

1. **Fork the repository**
2. **Create a branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** following our coding standards
4. **Commit**: `git commit -m 'Add: descriptive message'`
   - Use prefixes: `Add:`, `Fix:`, `Update:`, `Remove:`, `Refactor:`
5. **Push**: `git push origin feature/your-feature-name`
6. **Open a Pull Request** against the `main` branch



## 📏 Coding Standards

### Python
- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints where possible
- Document functions with docstrings (Google style)
- Keep functions small and single-purpose

### Commit Messages
```
Add: Brief description of change
Fix: Brief description of bug fix
Update: Brief description of modification
Remove: Brief description of removal
Refactor: Brief description of restructuring
```

### Branch Naming
```
feature/short-description
bugfix/short-description
docs/short-description
refactor/short-description
```



## 🧪 Testing

Before submitting a PR:
1. Test your changes locally
2. Verify the API endpoints work:
   ```bash
   # Health check
   curl http://localhost:8000/
   
   # Prediction
   curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{...}'
   ```
3. Run the Streamlit app: `streamlit run app.py`
4. Ensure no existing functionality is broken



## 📁 Project Structure

See [README.md](README.md#-project-structure) for the full project layout.



## 👥 Recognition

All contributors will be recognized in the project's contributors list. We value every contribution, from code to documentation to bug reports.



## 📞 Questions?

- **Email**: [hatalabdallah@gmail.com](mailto:hatalabdallah@gmail.com)
- **WhatsApp**: [+256 701 019242](https://wa.me/256701019242)
- **Twitter**: [@Hatalabdallah](https://x.com/Hatalabdallah)
- **LinkedIn**: [ddumbaka](https://www.linkedin.com/in/ddumbaka/)

<p align="center">❤️ Thank you for contributing to EduPredict!</p>
```


## 🚀 Push to GitHub

Now in your VS Code terminal, run:

```
git add README.md LICENSE CONTRIBUTING.md
git commit -m "Add professional documentation: README, LICENSE, CONTRIBUTING"
git push origin main
```
