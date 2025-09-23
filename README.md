# sale-hunter

sale-hunter is a Python-based tool designed for monitoring and notifying users about sales and price changes on popular e-commerce platforms such as Ozon and Wildberries (WB). It supports automated scheduling to fetch prices and sends notifications upon detecting relevant updates.

## Features

- Monitor product prices from Ozon and Wildberries via parsers
- Schedule periodic price checks and notifications
- Manage user sessions and subscriptions for tailored alerts
- Bot interface for receiving user commands and delivering notifications
- Persistent storage through database integration
- Modular design with separated layers for command processing, business logic, data access, and API parsing

## Architecture Overview

The project is structured into several layers:

- **Bot Interface:** Handles user commands and message delivery
- **Command Processing:** Manages command parsing and session management
- **Business Logic & Session Management:** Maintains user sessions and notification logic
- **Parsers:** Interfaces with external APIs (Ozon, WB) to fetch product data
- **Data Access Layer:** Connects to the database and persists data models
- **Scheduler:** Triggers routine price checks and updates
- **Notification Service:** Sends notifications to users based on price changes

```mermaid
graph TB
    %% Triggers
    User["User"]
    Scheduler["Scheduler/Monitor"] 
 
    %% Shared Libraries
    subgraph "Shared Libraries"
        Config["Config (global_constants)"]:::inbound
        Utils["Utils"]:::external
    end
 
    %% Bot Layer
    BotInterface["Bot Interface"]:::inbound
    click BotInterface "https://github.com/baikoby228/sale-hunter/blob/main/bot.py"
 
    %% Command Processing
    subgraph "Command Processing Layer"
        CommandProcessing["app/processing/"]:::inbound
    end
    click CommandProcessing "https://github.com/baikoby228/sale-hunter/tree/main/app/processing/"
 
    %% Business Logic & Session Management
    subgraph "Business Logic & Session Management"
        SessionManager["Session Manager"]:::persistence
        Notification["Notification Service"]:::outbound
    end
    click SessionManager "https://github.com/baikoby228/sale-hunter/tree/main/app/session/"
    click Notification "https://github.com/baikoby228/sale-hunter/blob/main/app/notification.py"
 
    %% Parsers / External APIs
    subgraph "Parsers / External APIs"
        Parsers["Parsers (Ozon, WB)"]:::external
    end
    click Parsers "https://github.com/baikoby228/sale-hunter/tree/main/app/parsers/"
 
    %% Data Access Layer
    subgraph "Data Access Layer"
        DataAccess["DB Connectors"]:::persistence
        Models["Data Models"]:::persistence
    end
    click DataAccess "https://github.com/baikoby228/sale-hunter/tree/main/infra/database/"
    click Models "https://github.com/baikoby228/sale-hunter/tree/main/models/"
 
    %% Database
    Database["Database"]:::persistence
 
    %% Flows: User commands
    User -->|sends commands| BotInterface
    BotInterface -->|dispatches| CommandProcessing
    CommandProcessing -->|reads/writes| SessionManager
    CommandProcessing -->|persists subscriptions| DataAccess
    SessionManager -->|persists session| DataAccess
    DataAccess -->|stores data| Database
 
    %% Scheduled price checks
    Scheduler -->|triggers| Parsers
    Parsers -->|fetch prices| DataAccess
    Parsers -->|notify logic| Notification
 
    %% Notifications flow
    Notification -->|sends updates| BotInterface
    BotInterface -->|delivers messages| User
 
    %% Shared libraries usage
    Config --> BotInterface
    Config --> CommandProcessing
    Config --> Parsers
    Utils --> CommandProcessing
    Utils --> Parsers
 
    %% Styles
    classDef inbound fill:#E0F7FA,stroke:#039BE5,color:#006064
    classDef outbound fill:#E8F5E9,stroke:#43A047,color:#1B5E20
    classDef persistence fill:#FFF3E0,stroke:#FB8C00,color:#E65100
    classDef external fill:#ECEFF1,stroke:#90A4AE,color:#37474F
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/baikoby228/sale-hunter.git
   cd sale-hunter
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure any global constants or credentials as needed in the configuration files.

## Usage

- Run the bot interface to start receiving user commands.
- Use the provided session management commands to subscribe or unsubscribe from price alerts.
- The scheduler will automatically trigger price checks and notifications based on configured intervals.

Refer to the code documentation in the `app/`, `bot.py`, and `app/parsers/` directories for detailed usage and customization.

## Contributing

Contributions are welcome. Please fork the repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the AGPL-3.0 License.

