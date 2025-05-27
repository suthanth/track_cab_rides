#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting project setup...${NC}"

# Make the script executable
chmod +x setup.sh

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo -e "${YELLOW}Installing Homebrew...${NC}"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" </dev/null
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# Check if Python 3.8 is installed, if not install it
if ! command -v python3.8 &> /dev/null; then
    echo -e "${YELLOW}Python 3.8 is not installed. Installing Python 3.8...${NC}"
    brew install python@3.8
    echo -e "${YELLOW}Adding Python to PATH...${NC}"
    echo 'export PATH="/opt/homebrew/opt/python@3.8/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
fi

# Install PostgreSQL if not installed
if ! command -v postgres &> /dev/null; then
    echo -e "${YELLOW}Installing PostgreSQL...${NC}"
    brew install postgresql@14
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3.8 -m venv venv
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Upgrade pip
echo -e "${YELLOW}Upgrading pip...${NC}"
python3.8 -m pip install --upgrade pip

# Install requirements
echo -e "${YELLOW}Installing project dependencies...${NC}"
pip3 install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}Creating .env file...${NC}"
    cat > .env << EOL
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://localhost:5432/track_cab_rides
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
EOL
fi

echo -e "${GREEN}Setup completed successfully!${NC}"
echo -e "${YELLOW}Virtual environment is activated. You can start working on your project.${NC}"

# Run unit tests
echo -e "${GREEN}Running test suite...${NC}"
python manage.py test track_rides_application.track_rides_api.tests.AreaViewTests.test_create_area -v 2
