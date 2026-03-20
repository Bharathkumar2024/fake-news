# 🚀 Deployment Guide

Complete guide for deploying the Fact-Checker system to different environments.

## Table of Contents
1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Cloud Deployment](#cloud-deployment)
4. [Production Setup](#production-setup)

---

## 🖥️ Local Development

### Windows (Easiest)

#### Method 1: Batch File (Double-Click)
```batch
SETUP_AND_RUN.bat
```

#### Method 2: PowerShell
```powershell
powershell -ExecutionPolicy Bypass -File SETUP_AND_RUN.ps1
```

#### Method 3: Command Prompt
```cmd
python SETUP_AND_RUN.py
```

### Mac/Linux

```bash
python SETUP_AND_RUN.py
```

### Access Application
- **URL**: http://localhost:5000
- **Stop**: Press Ctrl+C in terminal

---

## 🐳 Docker Deployment

### Prerequisites
- Docker installed: https://www.docker.com/products/docker-desktop
- Docker Desktop running

### Build & Run

#### Option 1: Using docker-compose (Easiest)
```bash
# Start the app
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the app
docker-compose down
```

#### Option 2: Using Docker CLI
```bash
# Build image
docker build -t fact-checker:latest .

# Run container
docker run -d -p 5000:5000 --name fact-checker fact-checker:latest

# View logs
docker logs -f fact-checker

# Stop container
docker stop fact-checker
docker rm fact-checker
```

### Access Application
- **URL**: http://localhost:5000

### Check Container Health
```bash
docker ps  # See running containers
docker logs fact-checker  # View logs
docker stats fact-checker  # See resource usage
```

---

## ☁️ Cloud Deployment

### Deploy to Azure Container Instances (ACI)

#### Prerequisites
- Azure account
- Azure CLI installed

#### Steps
```bash
# 1. Login to Azure
az login

# 2. Create resource group
az group create --name fact-checker-rg --location eastus

# 3. Create container registry
az acr create --resource-group fact-checker-rg \
  --name factcheckerregistry --sku Basic

# 4. Build and push image
az acr build --registry factcheckerregistry \
  --image fact-checker:latest .

# 5. Deploy to ACI
az container create \
  --resource-group fact-checker-rg \
  --name fact-checker-instance \
  --image factcheckerregistry.azurecr.io/fact-checker:latest \
  --ports 5000 \
  --registry-login-server factcheckerregistry.azurecr.io

# 6. Get public IP
az container show --resource-group fact-checker-rg \
  --name fact-checker-instance --query ipAddress.ip --output tsv
```

### Deploy to AWS (EC2)

#### Prerequisites
- AWS account
- SSH access to EC2 instance

#### Steps
```bash
# 1. SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-instance

# 2. Install Docker & Docker Compose
sudo apt-get update
sudo apt-get install -y docker.io docker-compose
sudo systemctl start docker
sudo usermod -aG docker ubuntu

# 3. Clone or upload project
git clone https://github.com/your-repo/fact-checker.git
cd fact-checker

# 4. Start application
docker-compose up -d

# 5. Configure security group
# Open port 5000 in AWS security group
```

### Deploy to Heroku

#### Prerequisites
- Heroku account
- Heroku CLI installed

#### Steps
```bash
# 1. Login to Heroku
heroku login

# 2. Create Heroku app
heroku create fact-checker-app

# 3. Set environment variables
heroku config:set FLASK_ENV=production

# 4. Deploy
git push heroku main

# 5. View logs
heroku logs --tail

# 6. Open app
heroku open
```

### Deploy to Google Cloud Run

#### Prerequisites
- Google Cloud account
- Google Cloud SDK installed

#### Steps
```bash
# 1. Configure gcloud
gcloud config set project YOUR_PROJECT_ID

# 2. Build container
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/fact-checker

# 3. Deploy to Cloud Run
gcloud run deploy fact-checker \
  --image gcr.io/YOUR_PROJECT_ID/fact-checker \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 5000

# 4. View logs
gcloud run logs read fact-checker
```

---

## 🏢 Production Setup

### Requirements for Production
- Python 3.7+
- 2GB+ RAM
- 5GB+ disk space (for models)
- Linux server (Ubuntu 20.04+ recommended)
- SSL certificate (HTTPS)
- Domain name (optional)

### Production Checklist
- [ ] Use environment variables for secrets
- [ ] Set `FLASK_ENV=production`
- [ ] Use SSL/TLS certificates
- [ ] Enable CORS properly for your domain
- [ ] Set up monitoring and logging
- [ ] Configure backup for data directory
- [ ] Use process manager (systemd, supervisor)
- [ ] Set up reverse proxy (nginx, Apache)
- [ ] Configure firewall rules
- [ ] Set resource limits

### Example: Production Setup on Ubuntu

#### 1. Server Setup
```bash
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y python3-pip python3-venv nginx certbot

# Create app user
sudo useradd -m factchecker
sudo -u factchecker mkdir -p /home/factchecker/app
```

#### 2. Application Setup
```bash
# Clone/upload project
cd /home/factchecker/app
sudo cp -r /path/to/fact-checker .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Nginx Configuration
Create `/etc/nginx/sites-available/fact-checker`:
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable it:
```bash
sudo ln -s /etc/nginx/sites-available/fact-checker /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 4. SSL Certificate (Let's Encrypt)
```bash
sudo certbot --nginx -d yourdomain.com
```

#### 5. Systemd Service
Create `/etc/systemd/system/fact-checker.service`:
```ini
[Unit]
Description=Fact-Checker Application
After=network.target

[Service]
Type=notify
User=factchecker
WorkingDirectory=/home/factchecker/app
Environment="PATH=/home/factchecker/app/venv/bin"
Environment="FLASK_ENV=production"
ExecStart=/home/factchecker/app/venv/bin/python web_app/backend/app.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable fact-checker
sudo systemctl start fact-checker
sudo systemctl status fact-checker
```

#### 6. Monitoring
```bash
# View logs
sudo journalctl -u fact-checker -f

# Check status
sudo systemctl status fact-checker

# Monitor resources
watch -n 1 ps aux | grep fact-checker
```

---

## 📊 Monitoring & Logging

### Application Logs
```bash
# Docker
docker logs -f fact-checker

# Systemd
sudo journalctl -u fact-checker -f

# File-based (if configured)
tail -f /var/log/fact-checker/app.log
```

### Health Checks
```bash
# Check API health
curl http://localhost:5000/api/health

# Get system info
curl http://localhost:5000/api/info
```

### Performance Monitoring
```bash
# CPU and memory usage
docker stats fact-checker

# Process information
ps aux | grep python
```

---

## 🔄 Backup & Recovery

### Backup Data
```bash
# Backup models and data
tar -czf fact-checker-backup-$(date +%Y%m%d).tar.gz \
  data/ web_app/

# Backup database (if using)
mysqldump -u user -p database > database-backup.sql
```

### Restore Data
```bash
# Extract backup
tar -xzf fact-checker-backup-20240101.tar.gz

# Restore database (if applicable)
mysql -u user -p database < database-backup.sql

# Restart application
docker-compose restart
```

---

## 🔐 Security

### Environment Variables
Create `.env` file:
```bash
FLASK_ENV=production
FLASK_DEBUG=False
FLASK_PORT=5000
CORS_ORIGINS=yourdomain.com
API_KEY=your-secret-key  # If using authentication
```

### Firewall Rules
```bash
# Allow SSH
sudo ufw allow 22

# Allow HTTP
sudo ufw allow 80

# Allow HTTPS
sudo ufw allow 443

# Enable firewall
sudo ufw enable
```

### Database Security (if applicable)
- Use strong passwords
- Bind to localhost only
- Regular backups
- Encryption at rest

---

## 📈 Scaling

### Horizontal Scaling (Multiple Instances)
```bash
# Docker Swarm
docker swarm init
docker stack deploy -c docker-compose.yml fact-checker

# Kubernetes
kubectl apply -f kubernetes-deployment.yaml
```

### Load Balancing
- Use nginx or HAProxy for load balancing
- Round-robin traffic between instances
- Use sticky sessions if needed

### Caching
- Enable Redis for session caching
- Cache embeddings and predictions
- Set appropriate TTLs

---

## 🆘 Troubleshooting

### Common Issues

#### Port 5000 Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill process
kill -9 <PID>
```

#### Container won't start
```bash
# Check logs
docker logs fact-checker

# Rebuild image
docker build -t fact-checker:latest .

# Run interactively to see errors
docker run -it fact-checker:latest bash
```

#### Out of Memory
```bash
# Reduce sample size in config.py
SAMPLE_SIZE = 500

# Or increase container memory
docker run -m 4g fact-checker:latest
```

#### Models not found
```bash
# Ensure training completed
python notebooks/Step_1_Load_Data.py
python notebooks/Step_6_Train_Model.py
python notebooks/Step_8_Save_Models.py
```

---

## 📚 Additional Resources

- **Docker**: https://docs.docker.com/
- **Azure**: https://docs.microsoft.com/en-us/azure/
- **AWS**: https://aws.amazon.com/documentation/
- **Google Cloud**: https://cloud.google.com/docs
- **Heroku**: https://devcenter.heroku.com/

---

**Need help? Check the main README.md or QUICK_START.md!**
