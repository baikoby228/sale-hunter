mermaid
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