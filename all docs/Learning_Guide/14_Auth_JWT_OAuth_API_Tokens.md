# Authentication & Authorization - Complete Beginner's Guide

## Understanding Security in Web Applications

---

# PART 1: THE BASICS - WHAT ARE THEY?

---

## 1.1 Real-World Analogy: A Nightclub

```
┌─────────────────────────────────────────────────────────────────┐
│              AUTHENTICATION vs AUTHORIZATION                     │
│              The Nightclub Analogy                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Imagine you're going to an exclusive nightclub:                │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                                                         │    │
│  │                    🏢 NIGHTCLUB                         │    │
│  │                                                         │    │
│  │   STEP 1: AUTHENTICATION (Who are you?)                 │    │
│  │   ─────────────────────────────────────                 │    │
│  │                                                         │    │
│  │   🚪 Bouncer at the door:                               │    │
│  │      "Show me your ID please"                           │    │
│  │                                                         │    │
│  │   You show your ID card → Bouncer verifies it's you     │    │
│  │                                                         │    │
│  │   ✓ ID is valid = You ARE who you claim to be           │    │
│  │   ✗ ID is fake = You are NOT allowed in                 │    │
│  │                                                         │    │
│  │   This is AUTHENTICATION!                               │    │
│  │   Proving your IDENTITY.                                │    │
│  │                                                         │    │
│  │                                                         │    │
│  │   STEP 2: AUTHORIZATION (What can you do?)              │    │
│  │   ────────────────────────────────────────              │    │
│  │                                                         │    │
│  │   Now you're inside. But there are different areas:     │    │
│  │                                                         │    │
│  │   🎵 Main dance floor     → Everyone can access         │    │
│  │   🍸 Regular bar          → Everyone can access         │    │
│  │   ⭐ VIP section          → Only VIP members            │    │
│  │   🎛️ DJ booth             → Only staff                  │    │
│  │   💼 Manager's office     → Only managers               │    │
│  │                                                         │    │
│  │   Your ROLE determines what you CAN DO.                 │    │
│  │   This is AUTHORIZATION!                                │    │
│  │   Checking your PERMISSIONS.                            │    │
│  │                                                         │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.2 Definitions

```
┌─────────────────────────────────────────────────────────────────┐
│                    DEFINITIONS                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║                   AUTHENTICATION                           ║  │
│  ║                  (AuthN - "Who are you?")                  ║  │
│  ╠═══════════════════════════════════════════════════════════╣  │
│  ║                                                           ║  │
│  ║  The process of VERIFYING the IDENTITY of a user.         ║  │
│  ║                                                           ║  │
│  ║  It answers: "Are you really who you claim to be?"        ║  │
│  ║                                                           ║  │
│  ║  Examples:                                                 ║  │
│  ║  • Entering username and password                         ║  │
│  ║  • Scanning your fingerprint                              ║  │
│  ║  • Entering a code sent to your phone                     ║  │
│  ║  • Face recognition to unlock phone                       ║  │
│  ║  • Swiping your employee badge                            ║  │
│  ║                                                           ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                  │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║                   AUTHORIZATION                            ║  │
│  ║                  (AuthZ - "What can you do?")              ║  │
│  ╠═══════════════════════════════════════════════════════════╣  │
│  ║                                                           ║  │
│  ║  The process of VERIFYING what a user is ALLOWED to do.   ║  │
│  ║                                                           ║  │
│  ║  It answers: "What permissions do you have?"              ║  │
│  ║                                                           ║  │
│  ║  Examples:                                                 ║  │
│  ║  • Can this user delete files? (Admin: Yes, Guest: No)    ║  │
│  ║  • Can this user view salary data? (HR: Yes, Dev: No)     ║  │
│  ║  • Can this user access VIP section? (VIP: Yes, Basic: No)║  │
│  ║  • Can this app read your contacts? (Allowed vs Denied)   ║  │
│  ║                                                           ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.3 The Key Difference

```
┌─────────────────────────────────────────────────────────────────┐
│              AUTHENTICATION vs AUTHORIZATION                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ASPECT         │ AUTHENTICATION        │ AUTHORIZATION         │
│  ───────────────┼───────────────────────┼───────────────────────│
│                 │                       │                       │
│  Question       │ WHO are you?          │ WHAT can you do?      │
│                 │                       │                       │
│  Purpose        │ Verify identity       │ Verify permissions    │
│                 │                       │                       │
│  Happens        │ FIRST                 │ SECOND (after auth)   │
│                 │                       │                       │
│  Example        │ Login with password   │ Access admin panel    │
│                 │                       │                       │
│  If fails       │ "Invalid credentials" │ "Access denied" /     │
│                 │                       │ "403 Forbidden"       │
│                 │                       │                       │
│  Data used      │ Credentials (password,│ Roles, permissions,   │
│                 │ tokens, biometrics)   │ policies              │
│                 │                       │                       │
│  Abbreviation   │ AuthN                 │ AuthZ                 │
│                 │                       │                       │
│                                                                  │
│                                                                  │
│  FLOW:                                                           │
│  ─────                                                           │
│                                                                  │
│  User Request → [AUTHENTICATION] → [AUTHORIZATION] → Resource   │
│                    "Who is this?"    "Can they do this?"        │
│                                                                  │
│                                                                  │
│  SIMPLE SUMMARY:                                                 │
│  ───────────────                                                 │
│                                                                  │
│  Authentication = LOGIN (proving identity)                      │
│  Authorization = PERMISSIONS (what you can access)              │
│                                                                  │
│  You MUST authenticate BEFORE you can be authorized!            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.4 More Real-World Examples

```
┌─────────────────────────────────────────────────────────────────┐
│              REAL-WORLD EXAMPLES                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  EXAMPLE 1: Gmail                                                │
│  ────────────────                                                │
│                                                                  │
│  Authentication:                                                 │
│  • Enter email and password                                      │
│  • Maybe enter 2FA code from phone                              │
│  • Google verifies: "Yes, this is really John"                  │
│                                                                  │
│  Authorization:                                                  │
│  • John can read HIS OWN emails                                  │
│  • John CANNOT read Jane's emails                               │
│  • John can delete HIS OWN emails                               │
│  • John cannot access Google Admin Console                      │
│                                                                  │
│                                                                  │
│  EXAMPLE 2: Company System                                       │
│  ─────────────────────────                                       │
│                                                                  │
│  Authentication (same for everyone):                            │
│  • Employee logs in with company credentials                    │
│                                                                  │
│  Authorization (different by role):                             │
│  • Intern:    Can view documents                                │
│  • Developer: Can view + edit code                              │
│  • Manager:   Can view + edit + approve                         │
│  • Admin:     Can do everything + delete users                  │
│                                                                  │
│                                                                  │
│  EXAMPLE 3: Netflix                                              │
│  ──────────────────                                              │
│                                                                  │
│  Authentication:                                                 │
│  • Log in with email and password                               │
│                                                                  │
│  Authorization:                                                  │
│  • Basic plan: Can watch on 1 device, SD quality                │
│  • Standard plan: Can watch on 2 devices, HD quality            │
│  • Premium plan: Can watch on 4 devices, 4K quality             │
│  • Kids profile: Cannot watch R-rated content                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 2: HTTP REQUESTS AND AUTH HEADERS

---

## 2.1 What is an HTTP Request?

```
┌─────────────────────────────────────────────────────────────────┐
│                    HTTP REQUEST BASICS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  When your app talks to a server, it sends HTTP REQUESTS.       │
│                                                                  │
│  An HTTP Request has several parts:                             │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   HTTP REQUEST                          │    │
│  ├─────────────────────────────────────────────────────────┤    │
│  │                                                         │    │
│  │  1. METHOD (What action?)                               │    │
│  │     GET    = Retrieve data (read)                       │    │
│  │     POST   = Send/create data                           │    │
│  │     PUT    = Update data                                │    │
│  │     DELETE = Delete data                                │    │
│  │                                                         │    │
│  │  2. URL (Where to send?)                                │    │
│  │     https://api.example.com/users                       │    │
│  │                                                         │    │
│  │  3. HEADERS (Extra info about the request)              │    │
│  │     Content-Type: application/json                      │    │
│  │     Authorization: Bearer abc123...  ← AUTH INFO HERE!  │    │
│  │     Accept: application/json                            │    │
│  │                                                         │    │
│  │  4. BODY (Data you're sending - for POST/PUT)           │    │
│  │     {"name": "John", "email": "john@email.com"}         │    │
│  │                                                         │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                                                                  │
│  THE AUTHORIZATION HEADER:                                       │
│  ─────────────────────────                                       │
│                                                                  │
│  This header carries your authentication credentials!           │
│                                                                  │
│  Examples:                                                       │
│  • Authorization: Basic dXNlcjpwYXNz                            │
│  • Authorization: Bearer eyJhbGciOiJIUzI1NiIs...                │
│  • X-API-Key: your-api-key-here                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2.2 Authentication vs Authorization in HTTP

```
┌─────────────────────────────────────────────────────────────────┐
│              HTTP: AUTHENTICATION vs AUTHORIZATION               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CONFUSING NAMING ALERT!                                         │
│  ───────────────────────                                         │
│                                                                  │
│  In HTTP, the header is called "Authorization"                  │
│  BUT it's actually used for AUTHENTICATION!                     │
│                                                                  │
│  This is a historical naming confusion. Don't let it confuse    │
│  you about the concepts!                                        │
│                                                                  │
│                                                                  │
│  WHAT HAPPENS IN A REQUEST:                                      │
│  ──────────────────────────                                      │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                                                         │    │
│  │  CLIENT                              SERVER             │    │
│  │  ──────                              ──────             │    │
│  │                                                         │    │
│  │  Step 1: Send request with credentials                  │    │
│  │  ─────────────────────────────────────                  │    │
│  │                                                         │    │
│  │  GET /api/admin/users                                   │    │
│  │  Authorization: Bearer eyJhbGci...                      │    │
│  │                        ───────────────                  │    │
│  │                        This is for AUTHENTICATION       │    │
│  │                        (proving who you are)            │    │
│  │                                                         │    │
│  │                                                         │    │
│  │  Step 2: Server verifies                                │    │
│  │  ───────────────────────                                │    │
│  │                                                         │    │
│  │  Server reads token → AUTHENTICATION                    │    │
│  │  "Is this token valid? Who is this user?"              │    │
│  │  Result: "This is user John, role: admin"              │    │
│  │                                                         │    │
│  │                                                         │    │
│  │  Step 3: Server checks permissions                      │    │
│  │  ─────────────────────────────────                      │    │
│  │                                                         │    │
│  │  Server checks role → AUTHORIZATION                     │    │
│  │  "Can an admin access /api/admin/users?"               │    │
│  │  Result: "Yes, admins can access this"                 │    │
│  │                                                         │    │
│  │                                                         │    │
│  │  Step 4: Return response                                │    │
│  │  ───────────────────────                                │    │
│  │                                                         │    │
│  │  200 OK + user data                                     │    │
│  │  OR                                                     │    │
│  │  401 Unauthorized (authentication failed)              │    │
│  │  OR                                                     │    │
│  │  403 Forbidden (authorization failed)                  │    │
│  │                                                         │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                                                                  │
│  HTTP STATUS CODES:                                              │
│  ──────────────────                                              │
│                                                                  │
│  401 Unauthorized = AUTHENTICATION failed                       │
│                     "I don't know who you are"                  │
│                     (bad/missing credentials)                   │
│                                                                  │
│  403 Forbidden = AUTHORIZATION failed                           │
│                  "I know who you are, but you can't do this"   │
│                  (valid user, but no permission)                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 3: AUTHENTICATION METHODS

---

## 3.1 Overview of Methods

```
┌─────────────────────────────────────────────────────────────────┐
│              AUTHENTICATION METHODS OVERVIEW                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  There are several ways to authenticate:                        │
│                                                                  │
│  1. API KEYS          - Simple, static keys                     │
│  2. BASIC AUTH        - Username + password encoded             │
│  3. JWT TOKENS        - Self-contained tokens                   │
│  4. OAUTH 2.0         - Third-party login (Google, Facebook)   │
│  5. SESSION-BASED     - Server stores session                   │
│                                                                  │
│                                                                  │
│  COMPARISON:                                                     │
│  ───────────                                                     │
│                                                                  │
│  METHOD      │ SECURITY │ COMPLEXITY │ USE CASE                 │
│  ────────────┼──────────┼────────────┼──────────────────────────│
│  API Keys    │ Low-Med  │ Easy       │ Server-to-server APIs    │
│  Basic Auth  │ Low      │ Easy       │ Simple internal APIs     │
│  JWT         │ High     │ Medium     │ Modern APIs, SPAs        │
│  OAuth 2.0   │ High     │ Complex    │ Third-party login        │
│  Session     │ Medium   │ Medium     │ Traditional websites     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3.2 API Keys

```
┌─────────────────────────────────────────────────────────────────┐
│                       API KEYS                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WHAT IS IT?                                                     │
│  ───────────                                                     │
│  A long, random string that identifies your application.        │
│  Like a password for your app (not for a user).                 │
│                                                                  │
│                                                                  │
│  EXAMPLE API KEY:                                                │
│  ────────────────                                                │
│  sk_test_XXXXXX          │
│                                                                  │
│                                                                  │
│  HOW IT'S USED:                                                  │
│  ──────────────                                                  │
│                                                                  │
│  Method 1: In URL (Not recommended - visible in logs!)          │
│  ──────────────────────────────────────────────────              │
│  GET https://api.example.com/data?api_key=sk_test_XXXXXX...     │
│                                                                  │
│  Method 2: In Header (Recommended)                               │
│  ─────────────────────────────────                               │
│  GET https://api.example.com/data                               │
│  X-API-Key: sk_test_XXXXXX...                    │
│                                                                  │
│  OR                                                              │
│                                                                  │
│  Authorization: ApiKey sk_test_XXXXXX...         │
│                                                                  │
│                                                                  │
│  PYTHON CODE EXAMPLE:                                            │
│  ────────────────────                                            │
│                                                                  │
│  ```python                                                       │
│  import requests                                                 │
│                                                                  │
│  api_key = "sk_test_XXXXXX"                │
│                                                                  │
│  # Method 1: API key in header (RECOMMENDED)                    │
│  headers = {                                                     │
│      "X-API-Key": api_key                                       │
│  }                                                               │
│                                                                  │
│  response = requests.get(                                        │
│      "https://api.example.com/data",                            │
│      headers=headers                                             │
│  )                                                               │
│                                                                  │
│  print(response.json())                                          │
│  ```                                                             │
│                                                                  │
│                                                                  │
│  REAL-WORLD SERVICES USING API KEYS:                            │
│  ────────────────────────────────────                            │
│  • OpenAI API                                                    │
│  • Stripe (payment processing)                                   │
│  • Google Maps API                                               │
│  • SendGrid (email service)                                      │
│  • Weather APIs                                                  │
│                                                                  │
│                                                                  │
│  PROS:                                                           │
│  • Simple to implement                                           │
│  • Easy to understand                                            │
│  • Good for server-to-server communication                      │
│                                                                  │
│  CONS:                                                           │
│  • If leaked, anyone can use it                                  │
│  • No expiration (unless manually rotated)                      │
│  • Doesn't identify WHO is using it, just WHICH app             │
│                                                                  │
│                                                                  │
│  BEST PRACTICES:                                                 │
│  ───────────────                                                 │
│  • NEVER put API keys in code (use environment variables)       │
│  • NEVER commit API keys to Git                                 │
│  • Rotate keys periodically                                      │
│  • Use different keys for dev/prod                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3.3 Basic Authentication

```
┌─────────────────────────────────────────────────────────────────┐
│                    BASIC AUTHENTICATION                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WHAT IS IT?                                                     │
│  ───────────                                                     │
│  Sends username and password encoded in Base64.                 │
│  Very simple, but NOT very secure (only use over HTTPS!)        │
│                                                                  │
│                                                                  │
│  HOW IT WORKS:                                                   │
│  ─────────────                                                   │
│                                                                  │
│  1. Take username:password                                       │
│     Example: "john:secretpass123"                               │
│                                                                  │
│  2. Encode in Base64                                             │
│     "john:secretpass123" → "am9objpzZWNyZXRwYXNzMTIz"           │
│                                                                  │
│  3. Send in Authorization header                                 │
│     Authorization: Basic am9objpzZWNyZXRwYXNzMTIz              │
│                                                                  │
│                                                                  │
│  ⚠️ WARNING: Base64 is NOT encryption!                          │
│              Anyone can decode it easily!                        │
│              ALWAYS use HTTPS with Basic Auth!                  │
│                                                                  │
│                                                                  │
│  PYTHON CODE EXAMPLE:                                            │
│  ────────────────────                                            │
│                                                                  │
│  ```python                                                       │
│  import requests                                                 │
│  from requests.auth import HTTPBasicAuth                        │
│                                                                  │
│  username = "john"                                               │
│  password = "secretpass123"                                      │
│                                                                  │
│  # Method 1: Using requests built-in auth                       │
│  response = requests.get(                                        │
│      "https://api.example.com/data",                            │
│      auth=HTTPBasicAuth(username, password)                     │
│  )                                                               │
│                                                                  │
│  # Method 2: Shorter version                                    │
│  response = requests.get(                                        │
│      "https://api.example.com/data",                            │
│      auth=(username, password)  # Tuple works too!             │
│  )                                                               │
│                                                                  │
│  # Method 3: Manual header                                      │
│  import base64                                                   │
│  credentials = base64.b64encode(                                │
│      f"{username}:{password}".encode()                          │
│  ).decode()                                                      │
│                                                                  │
│  headers = {                                                     │
│      "Authorization": f"Basic {credentials}"                    │
│  }                                                               │
│  response = requests.get(                                        │
│      "https://api.example.com/data",                            │
│      headers=headers                                             │
│  )                                                               │
│  ```                                                             │
│                                                                  │
│                                                                  │
│  PROS:                                                           │
│  • Very simple to implement                                      │
│  • Widely supported                                              │
│  • No extra setup needed                                        │
│                                                                  │
│  CONS:                                                           │
│  • Credentials sent with EVERY request                          │
│  • Base64 is NOT encryption (easily decoded)                    │
│  • Must use HTTPS (otherwise credentials visible!)              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3.4 JWT (JSON Web Tokens)

```
┌─────────────────────────────────────────────────────────────────┐
│                    JWT - JSON WEB TOKENS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WHAT IS IT?                                                     │
│  ───────────                                                     │
│  A compact, self-contained token that carries user information. │
│  The server creates it, the client stores and sends it back.    │
│                                                                  │
│                                                                  │
│  WHAT A JWT LOOKS LIKE:                                          │
│  ──────────────────────                                          │
│                                                                  │
│  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.                          │
│  eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0Ijo.  │
│  SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c                    │
│                                                                  │
│  It has THREE parts separated by dots (.):                      │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                                                         │    │
│  │  HEADER.PAYLOAD.SIGNATURE                               │    │
│  │                                                         │    │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐           │    │
│  │  │  HEADER   │  │  PAYLOAD  │  │ SIGNATURE │           │    │
│  │  │           │  │           │  │           │           │    │
│  │  │ Algorithm │  │ User data │  │ Verifies  │           │    │
│  │  │ Token type│  │ Claims    │  │ integrity │           │    │
│  │  │           │  │ Expiry    │  │           │           │    │
│  │  └───────────┘  └───────────┘  └───────────┘           │    │
│  │                                                         │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│                                                                  │
│  DECODED JWT EXAMPLE:                                            │
│  ────────────────────                                            │
│                                                                  │
│  HEADER (tells how token was created):                          │
│  {                                                               │
│    "alg": "HS256",      ← Algorithm used                        │
│    "typ": "JWT"         ← Token type                            │
│  }                                                               │
│                                                                  │
│  PAYLOAD (the actual data):                                      │
│  {                                                               │
│    "sub": "1234567890",     ← User ID                           │
│    "name": "John Doe",      ← User name                         │
│    "email": "john@email.com", ← User email                      │
│    "role": "admin",         ← User role (for authorization!)   │
│    "iat": 1516239022,       ← Issued at (timestamp)            │
│    "exp": 1516242622        ← Expires at (timestamp)           │
│  }                                                               │
│                                                                  │
│  SIGNATURE (ensures token wasn't tampered):                     │
│  HMACSHA256(                                                     │
│    base64UrlEncode(header) + "." +                              │
│    base64UrlEncode(payload),                                    │
│    secret                                                        │
│  )                                                               │
│                                                                  │
│                                                                  │
│  HOW JWT FLOW WORKS:                                             │
│  ───────────────────                                             │
│                                                                  │
│  ┌──────────┐                              ┌──────────┐         │
│  │  CLIENT  │                              │  SERVER  │         │
│  └────┬─────┘                              └────┬─────┘         │
│       │                                         │               │
│       │  1. Login (username + password)         │               │
│       │ ───────────────────────────────────────→│               │
│       │                                         │               │
│       │                                         │ Verify user   │
│       │                                         │ Create JWT    │
│       │                                         │               │
│       │  2. Return JWT token                    │               │
│       │←─────────────────────────────────────── │               │
│       │                                         │               │
│       │ Store token (localStorage, cookie)     │               │
│       │                                         │               │
│       │  3. Request with token                  │               │
│       │  Authorization: Bearer <JWT>            │               │
│       │ ───────────────────────────────────────→│               │
│       │                                         │               │
│       │                                         │ Verify token  │
│       │                                         │ Read user info│
│       │                                         │               │
│       │  4. Return data                         │               │
│       │←─────────────────────────────────────── │               │
│       │                                         │               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3.5 Bearer Tokens

```
┌─────────────────────────────────────────────────────────────────┐
│                    BEARER TOKENS                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WHAT IS A BEARER TOKEN?                                         │
│  ───────────────────────                                         │
│                                                                  │
│  "Bearer" is just a TYPE of authentication scheme.              │
│  It means: "Whoever BEARS (carries) this token can access."     │
│                                                                  │
│  JWTs are commonly used AS bearer tokens, but any token can be. │
│                                                                  │
│                                                                  │
│  FORMAT:                                                         │
│  ───────                                                         │
│                                                                  │
│  Authorization: Bearer <your-token-here>                        │
│                                                                  │
│  Example:                                                        │
│  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...  │
│                                                                  │
│                                                                  │
│  PYTHON CODE EXAMPLE:                                            │
│  ────────────────────                                            │
│                                                                  │
│  ```python                                                       │
│  import requests                                                 │
│                                                                  │
│  # Your JWT token (usually received after login)                │
│  token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."              │
│                                                                  │
│  headers = {                                                     │
│      "Authorization": f"Bearer {token}"                         │
│  }                                                               │
│                                                                  │
│  response = requests.get(                                        │
│      "https://api.example.com/protected/data",                  │
│      headers=headers                                             │
│  )                                                               │
│                                                                  │
│  if response.status_code == 200:                                │
│      print("Success!", response.json())                         │
│  elif response.status_code == 401:                              │
│      print("Invalid token - authentication failed")             │
│  elif response.status_code == 403:                              │
│      print("Valid token but no permission - access denied")     │
│  ```                                                             │
│                                                                  │
│                                                                  │
│  WHY "BEARER"?                                                   │
│  ─────────────                                                   │
│                                                                  │
│  The term comes from "bearer instrument" in finance.            │
│  Like a bearer check - whoever holds it can cash it.           │
│  Similarly, whoever holds the bearer token can access.          │
│                                                                  │
│  ⚠️ This means: KEEP YOUR TOKENS SECRET!                        │
│     If someone steals your token, they can impersonate you!     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3.6 JWT Python Code Example

```
┌─────────────────────────────────────────────────────────────────┐
│              COMPLETE JWT EXAMPLE IN PYTHON                      │
├─────────────────────────────────────────────────────────────────┤

```python
import requests

# ═══════════════════════════════════════════════════════════════
# SCENARIO: Accessing a Protected API
# ═══════════════════════════════════════════════════════════════

# Step 1: Login to get JWT token
# ─────────────────────────────────
def login(username, password):
    """
    Authenticate and get a JWT token.
    This is AUTHENTICATION - proving who you are.
    """
    response = requests.post(
        "https://api.example.com/auth/login",
        json={
            "username": username,
            "password": password
        }
    )

    if response.status_code == 200:
        # Server returns the JWT token
        data = response.json()
        return data["access_token"]
    else:
        print("Login failed!")
        return None


# Step 2: Use token to access protected resources
# ─────────────────────────────────────────────────
def get_user_data(token):
    """
    Access protected endpoint using JWT.
    Server will check AUTHENTICATION (valid token?)
    and AUTHORIZATION (does user have permission?).
    """
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://api.example.com/users/me",
        headers=headers
    )

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        print("Token invalid or expired - need to login again")
        return None
    elif response.status_code == 403:
        print("You don't have permission to access this")
        return None


# Step 3: Access admin endpoint (requires admin role)
# ────────────────────────────────────────────────────
def get_all_users(token):
    """
    Access admin-only endpoint.
    Even with valid token, you need admin AUTHORIZATION.
    """
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        "https://api.example.com/admin/users",
        headers=headers
    )

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        print("Not authenticated")
        return None
    elif response.status_code == 403:
        print("Not authorized - admin access required")
        return None


# ═══════════════════════════════════════════════════════════════
# MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Login (AUTHENTICATION)
    token = login("john", "password123")

    if token:
        print("Login successful! Got token.")

        # Get own data (requires authentication)
        my_data = get_user_data(token)
        print(f"My data: {my_data}")

        # Try to access admin endpoint (requires authorization)
        all_users = get_all_users(token)
        # This might return 403 if john is not an admin!
```

│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 4: ACCESS TOKENS vs REFRESH TOKENS

---

## 4.1 The Problem

```
┌─────────────────────────────────────────────────────────────────┐
│              WHY DO WE NEED TWO TYPES OF TOKENS?                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  THE PROBLEM:                                                    │
│  ────────────                                                    │
│                                                                  │
│  If a token NEVER expires:                                       │
│  • Stolen tokens can be used FOREVER                            │
│  • Very insecure!                                                │
│                                                                  │
│  If a token expires QUICKLY (e.g., 15 minutes):                 │
│  • User has to login every 15 minutes                           │
│  • Very annoying!                                                │
│                                                                  │
│                                                                  │
│  THE SOLUTION: TWO TOKENS!                                       │
│  ──────────────────────────                                      │
│                                                                  │
│  1. ACCESS TOKEN                                                 │
│     • Short-lived (15 mins - 1 hour)                            │
│     • Used for actual API requests                              │
│     • Sent with every request                                    │
│     • If stolen, only works briefly                             │
│                                                                  │
│  2. REFRESH TOKEN                                                │
│     • Long-lived (days - weeks)                                  │
│     • Used ONLY to get new access tokens                        │
│     • Stored more securely                                       │
│     • If stolen, can be revoked                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4.2 Access Token vs Refresh Token

```
┌─────────────────────────────────────────────────────────────────┐
│              ACCESS TOKEN vs REFRESH TOKEN                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  COMPARISON:                                                     │
│  ───────────                                                     │
│                                                                  │
│  ASPECT          │ ACCESS TOKEN      │ REFRESH TOKEN            │
│  ────────────────┼───────────────────┼──────────────────────────│
│  Lifetime        │ Short (15 min-1hr)│ Long (7 days - 30 days) │
│  Purpose         │ Access resources  │ Get new access tokens   │
│  Sent to         │ Resource APIs     │ Auth server only        │
│  Frequency       │ Every request     │ Only when token expires │
│  If stolen       │ Limited damage    │ More serious, revokable │
│  Storage         │ Memory/localStorage│ HttpOnly cookie (safer)│
│                                                                  │
│                                                                  │
│  HOW THEY WORK TOGETHER:                                         │
│  ───────────────────────                                         │
│                                                                  │
│  ┌──────────┐                              ┌──────────┐         │
│  │  CLIENT  │                              │  SERVER  │         │
│  └────┬─────┘                              └────┬─────┘         │
│       │                                         │               │
│       │  1. Login (username + password)         │               │
│       │ ───────────────────────────────────────→│               │
│       │                                         │               │
│       │  2. Return BOTH tokens                  │               │
│       │←─────────────────────────────────────── │               │
│       │  {                                      │               │
│       │    access_token: "..." (15 min),        │               │
│       │    refresh_token: "..." (7 days)        │               │
│       │  }                                      │               │
│       │                                         │               │
│       │  3. Use access token for requests       │               │
│       │  Authorization: Bearer <access_token>   │               │
│       │ ───────────────────────────────────────→│               │
│       │                                         │               │
│       │  4. Data returned                       │               │
│       │←─────────────────────────────────────── │               │
│       │                                         │               │
│       │  ... 15 minutes later ...               │               │
│       │                                         │               │
│       │  5. Access token expired!               │               │
│       │  Request with old token → 401 Error     │               │
│       │                                         │               │
│       │  6. Use refresh token to get new access │               │
│       │  POST /auth/refresh                     │               │
│       │  { refresh_token: "..." }               │               │
│       │ ───────────────────────────────────────→│               │
│       │                                         │               │
│       │  7. Return NEW access token             │               │
│       │←─────────────────────────────────────── │               │
│       │  { access_token: "..." (new!) }         │               │
│       │                                         │               │
│       │  8. Continue with new access token      │               │
│       │ ───────────────────────────────────────→│               │
│       │                                         │               │
│                                                                  │
│                                                                  │
│  USER NEVER HAS TO LOGIN AGAIN (until refresh token expires!)   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4.3 Python Code Example

```
┌─────────────────────────────────────────────────────────────────┐
│              PYTHON: HANDLING TOKEN REFRESH                      │
├─────────────────────────────────────────────────────────────────┤

```python
import requests

class APIClient:
    """
    A client that automatically handles token refresh.
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.access_token = None
        self.refresh_token = None

    def login(self, username, password):
        """Login and get both tokens."""
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={"username": username, "password": password}
        )

        if response.status_code == 200:
            data = response.json()
            self.access_token = data["access_token"]
            self.refresh_token = data["refresh_token"]
            return True
        return False

    def refresh_access_token(self):
        """Use refresh token to get new access token."""
        response = requests.post(
            f"{self.base_url}/auth/refresh",
            json={"refresh_token": self.refresh_token}
        )

        if response.status_code == 200:
            data = response.json()
            self.access_token = data["access_token"]
            return True
        else:
            # Refresh token expired - need to login again
            return False

    def make_request(self, method, endpoint, **kwargs):
        """
        Make API request with automatic token refresh.
        """
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"

        # First attempt
        response = requests.request(
            method,
            f"{self.base_url}{endpoint}",
            headers=headers,
            **kwargs
        )

        # If 401 (token expired), try to refresh
        if response.status_code == 401:
            print("Token expired, refreshing...")

            if self.refresh_access_token():
                # Update header with new token
                headers["Authorization"] = f"Bearer {self.access_token}"

                # Retry the request
                response = requests.request(
                    method,
                    f"{self.base_url}{endpoint}",
                    headers=headers,
                    **kwargs
                )
            else:
                print("Refresh failed - need to login again")

        return response


# ═══════════════════════════════════════════════════════════════
# USAGE
# ═══════════════════════════════════════════════════════════════

client = APIClient("https://api.example.com")

# Login once
client.login("john", "password123")

# Make requests - token refresh happens automatically!
response = client.make_request("GET", "/users/me")
print(response.json())

# Even after token expires, this will auto-refresh
response = client.make_request("GET", "/users/me")
print(response.json())
```

│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 5: OAUTH 2.0

---

## 5.1 What is OAuth?

```
┌─────────────────────────────────────────────────────────────────┐
│                       OAUTH 2.0                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WHAT IS OAUTH?                                                  │
│  ──────────────                                                  │
│                                                                  │
│  OAuth 2.0 is a protocol that allows you to login to one app    │
│  using your account from ANOTHER service.                       │
│                                                                  │
│  You've seen this as:                                            │
│  • "Login with Google"                                           │
│  • "Login with Facebook"                                         │
│  • "Login with GitHub"                                          │
│  • "Login with Apple"                                            │
│                                                                  │
│                                                                  │
│  WHY USE OAUTH?                                                  │
│  ──────────────                                                  │
│                                                                  │
│  For USERS:                                                      │
│  • Don't need to create yet another account                     │
│  • Don't need to remember another password                      │
│  • More secure (Google/Facebook have better security)           │
│                                                                  │
│  For DEVELOPERS:                                                 │
│  • Don't need to handle passwords                               │
│  • Don't need to build forgot-password flows                    │
│  • Can access user data from provider (with permission)         │
│                                                                  │
│                                                                  │
│  KEY CONCEPT: OAuth is about AUTHORIZATION, not Authentication! │
│  ─────────────────────────────────────────────────────────────── │
│                                                                  │
│  OAuth = "Allow App X to access my data on Service Y"           │
│                                                                  │
│  Example:                                                        │
│  "Allow LinkedIn to read my Google Contacts"                    │
│  "Allow Spotify to post to my Facebook"                         │
│                                                                  │
│  But we commonly use it for authentication too (via OpenID)     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5.2 OAuth Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    OAUTH 2.0 FLOW                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  SCENARIO: User wants to login to MyApp using Google            │
│                                                                  │
│  PARTICIPANTS:                                                   │
│  • Resource Owner = User (you)                                   │
│  • Client = MyApp (wants to access user data)                   │
│  • Authorization Server = Google (handles login)                │
│  • Resource Server = Google API (has user data)                 │
│                                                                  │
│                                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                  │
│  │   USER   │    │  MY APP  │    │  GOOGLE  │                  │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘                  │
│       │               │               │                         │
│       │ 1. Click "Login with Google"  │                         │
│       │──────────────→│               │                         │
│       │               │               │                         │
│       │               │ 2. Redirect to Google                   │
│       │←──────────────│──────────────→│                         │
│       │               │               │                         │
│       │ 3. See Google login page      │                         │
│       │               │←──────────────│                         │
│       │               │               │                         │
│       │ 4. Enter Google credentials   │                         │
│       │───────────────────────────────→                         │
│       │               │               │                         │
│       │ 5. Google asks: "Allow MyApp  │                         │
│       │    to access your email?"     │                         │
│       │←──────────────────────────────│                         │
│       │               │               │                         │
│       │ 6. User clicks "Allow"        │                         │
│       │───────────────────────────────→                         │
│       │               │               │                         │
│       │               │ 7. Google sends authorization code      │
│       │               │←──────────────│                         │
│       │               │               │                         │
│       │               │ 8. MyApp exchanges code for token      │
│       │               │──────────────→│                         │
│       │               │               │                         │
│       │               │ 9. Google returns access token         │
│       │               │←──────────────│                         │
│       │               │               │                         │
│       │               │ 10. MyApp uses token to get user info │
│       │               │──────────────→│                         │
│       │               │               │                         │
│       │               │ 11. Google returns user profile        │
│       │               │←──────────────│                         │
│       │               │               │                         │
│       │ 12. User is now logged in!    │                         │
│       │←──────────────│               │                         │
│       │               │               │                         │
│                                                                  │
│                                                                  │
│  KEY POINTS:                                                     │
│  • User NEVER gives their Google password to MyApp              │
│  • MyApp only gets a LIMITED access token                       │
│  • User explicitly CONSENTS to what MyApp can access           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 6: SAML vs OAUTH

---

## 6.1 Comparison

```
┌─────────────────────────────────────────────────────────────────┐
│                    SAML vs OAUTH                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Both are protocols for authentication/authorization,           │
│  but they're designed for different use cases.                  │
│                                                                  │
│                                                                  │
│  SAML (Security Assertion Markup Language)                      │
│  ─────────────────────────────────────────                       │
│                                                                  │
│  • Uses XML format                                               │
│  • Older standard (2005)                                         │
│  • Designed for ENTERPRISE/SSO                                  │
│  • Common in corporate environments                             │
│  • Browser-based (redirects)                                     │
│  • "Login once, access all company apps"                        │
│                                                                  │
│  Example use cases:                                              │
│  • Employee logs into company portal                            │
│  • Accessing Office 365, Salesforce, Slack with one login      │
│  • Corporate Single Sign-On (SSO)                               │
│                                                                  │
│                                                                  │
│  OAuth 2.0                                                       │
│  ─────────                                                       │
│                                                                  │
│  • Uses JSON format                                              │
│  • Newer standard (2012)                                         │
│  • Designed for CONSUMER APPS / APIs                            │
│  • Common in web and mobile apps                                │
│  • API-based (tokens)                                            │
│  • "Allow this app to access my data"                           │
│                                                                  │
│  Example use cases:                                              │
│  • "Login with Google" on any website                           │
│  • Mobile app accessing your photos                             │
│  • Third-party apps accessing your data                         │
│                                                                  │
│                                                                  │
│  COMPARISON TABLE:                                               │
│  ─────────────────                                               │
│                                                                  │
│  ASPECT          │ SAML              │ OAuth 2.0                │
│  ────────────────┼───────────────────┼──────────────────────────│
│  Format          │ XML               │ JSON                     │
│  Age             │ Older (2005)      │ Newer (2012)             │
│  Primary use     │ Enterprise SSO    │ Consumer apps, APIs      │
│  Token type      │ XML assertions    │ Access tokens (JWT)      │
│  Complexity      │ More complex      │ Simpler                  │
│  Mobile support  │ Difficult         │ Excellent                │
│  Common in       │ Corporations      │ Consumer apps            │
│                                                                  │
│                                                                  │
│  SIMPLE RULE:                                                    │
│  ────────────                                                    │
│  • Enterprise/corporate login → SAML                            │
│  • Consumer apps/APIs → OAuth 2.0                               │
│  • Modern applications → OAuth 2.0 / OpenID Connect             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 7: STATEFUL vs STATELESS

---

## 7.1 What is State?

```
┌─────────────────────────────────────────────────────────────────┐
│                    STATEFUL vs STATELESS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WHAT IS "STATE"?                                                │
│  ────────────────                                                │
│                                                                  │
│  "State" = Information that the server remembers about you      │
│            between requests.                                     │
│                                                                  │
│  Example of state:                                               │
│  • You're logged in                                              │
│  • Your shopping cart has 3 items                               │
│  • You're on page 5 of search results                           │
│                                                                  │
│                                                                  │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║                   STATEFUL                                 ║  │
│  ║             (Server remembers you)                         ║  │
│  ╠═══════════════════════════════════════════════════════════╣  │
│  ║                                                           ║  │
│  ║  The SERVER stores information about your session.        ║  │
│  ║                                                           ║  │
│  ║  How it works:                                            ║  │
│  ║  1. You login                                             ║  │
│  ║  2. Server creates a "session" and stores it             ║  │
│  ║  3. Server gives you a "session ID" (cookie)             ║  │
│  ║  4. Every request, you send the session ID               ║  │
│  ║  5. Server looks up your session in its memory           ║  │
│  ║                                                           ║  │
│  ║  ┌──────────┐                    ┌──────────────────┐    ║  │
│  ║  │  CLIENT  │   session_id=abc   │     SERVER       │    ║  │
│  ║  │          │ ────────────────→  │                  │    ║  │
│  ║  └──────────┘                    │  Sessions:       │    ║  │
│  ║                                  │  abc → {user: 1} │    ║  │
│  ║                                  │  def → {user: 2} │    ║  │
│  ║                                  │  ghi → {user: 3} │    ║  │
│  ║                                  └──────────────────┘    ║  │
│  ║                                                           ║  │
│  ║  PROS:                                                    ║  │
│  ║  • Can store lots of data                                ║  │
│  ║  • Easy to invalidate (just delete session)             ║  │
│  ║  • Server has full control                               ║  │
│  ║                                                           ║  │
│  ║  CONS:                                                    ║  │
│  ║  • Server must store ALL sessions (memory/database)     ║  │
│  ║  • Hard to scale (multiple servers need shared storage) ║  │
│  ║  • More complex infrastructure                           ║  │
│  ║                                                           ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                  │
│                                                                  │
│  ╔═══════════════════════════════════════════════════════════╗  │
│  ║                   STATELESS                                ║  │
│  ║             (Server doesn't remember you)                  ║  │
│  ╠═══════════════════════════════════════════════════════════╣  │
│  ║                                                           ║  │
│  ║  The CLIENT carries all necessary information.            ║  │
│  ║  Server doesn't store sessions.                          ║  │
│  ║                                                           ║  │
│  ║  How it works with JWT:                                   ║  │
│  ║  1. You login                                             ║  │
│  ║  2. Server creates JWT with your info INSIDE it          ║  │
│  ║  3. Server gives you the JWT (doesn't store it!)         ║  │
│  ║  4. Every request, you send the JWT                      ║  │
│  ║  5. Server reads info FROM the JWT                       ║  │
│  ║                                                           ║  │
│  ║  ┌──────────────────┐           ┌──────────────────┐     ║  │
│  ║  │     CLIENT       │           │     SERVER       │     ║  │
│  ║  │                  │   JWT     │                  │     ║  │
│  ║  │ Token contains:  │ ───────→  │  No session      │     ║  │
│  ║  │ - user_id: 1     │           │  storage!        │     ║  │
│  ║  │ - role: admin    │           │                  │     ║  │
│  ║  │ - exp: 12345     │           │  Just reads      │     ║  │
│  ║  │                  │           │  the token       │     ║  │
│  ║  └──────────────────┘           └──────────────────┘     ║  │
│  ║                                                           ║  │
│  ║  PROS:                                                    ║  │
│  ║  • Easy to scale (any server can handle any request)    ║  │
│  ║  • No shared storage needed                              ║  │
│  ║  • Better performance (no database lookup per request)  ║  │
│  ║                                                           ║  │
│  ║  CONS:                                                    ║  │
│  ║  • Can't invalidate tokens easily (until they expire)   ║  │
│  ║  • Token can get large if storing lots of data          ║  │
│  ║  • Sensitive data in token must be handled carefully    ║  │
│  ║                                                           ║  │
│  ╚═══════════════════════════════════════════════════════════╝  │
│                                                                  │
│                                                                  │
│  COMPARISON:                                                     │
│  ───────────                                                     │
│                                                                  │
│  ASPECT          │ STATEFUL          │ STATELESS                │
│  ────────────────┼───────────────────┼──────────────────────────│
│  State stored    │ Server            │ Client (in token)        │
│  Scalability     │ Hard              │ Easy                     │
│  Typical token   │ Session ID        │ JWT                      │
│  Storage needed  │ Database/Memory   │ None                     │
│  Invalidation    │ Easy              │ Hard                     │
│  Common in       │ Traditional sites │ Modern APIs              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# PART 8: COMPLETE PYTHON EXAMPLES

---

## 8.1 Example: API Key Authentication

```python
"""
EXAMPLE 1: Using API Key Authentication
─────────────────────────────────────────
Real-world example: Accessing OpenAI API
"""

import requests
import os

# BEST PRACTICE: Store API key in environment variable
# Set it in terminal: export OPENAI_API_KEY="sk-..."
api_key = os.environ.get("OPENAI_API_KEY")

# If no env var, you could hardcode (NOT recommended for production!)
# api_key = "sk-your-api-key-here"

def call_openai_api():
    """
    Call OpenAI API with API key authentication.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",  # OpenAI uses Bearer format
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Hello!"}
        ]
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        print("Invalid API key!")
        return None
    else:
        print(f"Error: {response.status_code}")
        return None


# Example with Weather API (different API key format)
def get_weather(city):
    """
    Get weather data using API key in URL parameter.
    (Some APIs use this format instead of headers)
    """
    api_key = os.environ.get("WEATHER_API_KEY")

    # API key in URL (common for simple APIs)
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["location"]["name"],
            "temp": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"]
        }
    return None


if __name__ == "__main__":
    # Example usage
    weather = get_weather("London")
    if weather:
        print(f"Weather in {weather['city']}: {weather['temp']}°C, {weather['condition']}")
```

---

## 8.2 Example: Complete JWT Authentication Flow

```python
"""
EXAMPLE 2: Complete JWT Authentication System
───────────────────────────────────────────────
This shows both client-side and understanding of server-side
"""

import requests
import json
from datetime import datetime

class AuthClient:
    """
    A complete authentication client that handles:
    - Login (getting tokens)
    - Making authenticated requests
    - Token refresh
    - Error handling
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.access_token = None
        self.refresh_token = None
        self.user = None

    def login(self, email, password):
        """
        AUTHENTICATION: Prove who you are.
        Returns access and refresh tokens.
        """
        print(f"🔐 Attempting login for {email}...")

        response = requests.post(
            f"{self.base_url}/auth/login",
            json={
                "email": email,
                "password": password
            }
        )

        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("access_token")
            self.refresh_token = data.get("refresh_token")
            self.user = data.get("user")
            print(f"✅ Login successful! Welcome, {self.user.get('name', 'User')}")
            print(f"   Role: {self.user.get('role', 'unknown')}")
            return True

        elif response.status_code == 401:
            print("❌ Login failed: Invalid email or password")
            return False

        else:
            print(f"❌ Login failed: {response.status_code}")
            return False

    def _get_headers(self):
        """Get headers with authorization token."""
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def refresh_tokens(self):
        """
        Use refresh token to get new access token.
        Called automatically when access token expires.
        """
        print("🔄 Refreshing access token...")

        response = requests.post(
            f"{self.base_url}/auth/refresh",
            json={"refresh_token": self.refresh_token}
        )

        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("access_token")
            print("✅ Token refreshed successfully")
            return True
        else:
            print("❌ Token refresh failed - need to login again")
            return False

    def get(self, endpoint):
        """
        Make GET request with automatic token refresh.
        """
        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self._get_headers()
        )

        # If unauthorized, try to refresh token
        if response.status_code == 401:
            if self.refresh_tokens():
                # Retry with new token
                response = requests.get(
                    f"{self.base_url}{endpoint}",
                    headers=self._get_headers()
                )

        return response

    def post(self, endpoint, data):
        """
        Make POST request with automatic token refresh.
        """
        response = requests.post(
            f"{self.base_url}{endpoint}",
            headers=self._get_headers(),
            json=data
        )

        if response.status_code == 401:
            if self.refresh_tokens():
                response = requests.post(
                    f"{self.base_url}{endpoint}",
                    headers=self._get_headers(),
                    json=data
                )

        return response

    # ═══════════════════════════════════════════════════════════
    # EXAMPLE METHODS SHOWING AUTHORIZATION
    # ═══════════════════════════════════════════════════════════

    def get_my_profile(self):
        """
        Get current user's profile.
        REQUIRES: Authentication (any valid user)
        """
        print("\n📋 Getting my profile...")
        response = self.get("/users/me")

        if response.status_code == 200:
            profile = response.json()
            print(f"   Name: {profile.get('name')}")
            print(f"   Email: {profile.get('email')}")
            print(f"   Role: {profile.get('role')}")
            return profile
        else:
            print(f"   Error: {response.status_code}")
            return None

    def get_all_users(self):
        """
        Get all users in the system.
        REQUIRES: Authentication + ADMIN role (AUTHORIZATION!)
        """
        print("\n👥 Getting all users (admin only)...")
        response = self.get("/admin/users")

        if response.status_code == 200:
            users = response.json()
            print(f"   Found {len(users)} users")
            return users
        elif response.status_code == 403:
            print("   ❌ Access denied - you are not an admin")
            return None
        else:
            print(f"   Error: {response.status_code}")
            return None

    def delete_user(self, user_id):
        """
        Delete a user.
        REQUIRES: Authentication + ADMIN role (AUTHORIZATION!)
        """
        print(f"\n🗑️ Deleting user {user_id} (admin only)...")
        response = requests.delete(
            f"{self.base_url}/admin/users/{user_id}",
            headers=self._get_headers()
        )

        if response.status_code == 200:
            print("   ✅ User deleted successfully")
            return True
        elif response.status_code == 403:
            print("   ❌ Access denied - admin access required")
            return False
        elif response.status_code == 404:
            print("   ❌ User not found")
            return False
        else:
            print(f"   Error: {response.status_code}")
            return False


# ═══════════════════════════════════════════════════════════════
# DEMONSTRATION
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Create client
    client = AuthClient("https://api.example.com")

    # SCENARIO 1: Regular user
    print("\n" + "="*60)
    print("SCENARIO 1: Regular User")
    print("="*60)

    if client.login("john@example.com", "password123"):
        # This works - any authenticated user can see their profile
        client.get_my_profile()

        # This will fail with 403 - John is not an admin
        client.get_all_users()

    # SCENARIO 2: Admin user
    print("\n" + "="*60)
    print("SCENARIO 2: Admin User")
    print("="*60)

    if client.login("admin@example.com", "adminpass"):
        # This works
        client.get_my_profile()

        # This works too - admin has authorization!
        client.get_all_users()

        # Admin can delete users
        client.delete_user(123)
```

---

# PART 9: SECURITY BEST PRACTICES

---

```
┌─────────────────────────────────────────────────────────────────┐
│              SECURITY BEST PRACTICES                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. NEVER HARDCODE SECRETS                                       │
│  ──────────────────────────                                      │
│                                                                  │
│  ❌ BAD:                                                         │
│  api_key = "sk_test_XXXXXX"                                │
│                                                                  │
│  ✅ GOOD:                                                        │
│  api_key = os.environ.get("API_KEY")                            │
│                                                                  │
│                                                                  │
│  2. USE HTTPS ALWAYS                                             │
│  ───────────────────                                             │
│                                                                  │
│  ❌ BAD: http://api.example.com                                 │
│  ✅ GOOD: https://api.example.com                               │
│                                                                  │
│                                                                  │
│  3. STORE TOKENS SECURELY                                        │
│  ────────────────────────                                        │
│                                                                  │
│  Access tokens: Memory or sessionStorage                        │
│  Refresh tokens: HttpOnly cookies (not accessible by JS)        │
│                                                                  │
│                                                                  │
│  4. VALIDATE ON SERVER SIDE                                      │
│  ──────────────────────────                                      │
│                                                                  │
│  Never trust the client!                                         │
│  Always verify tokens and permissions on the server.            │
│                                                                  │
│                                                                  │
│  5. USE SHORT TOKEN LIFETIMES                                    │
│  ────────────────────────────                                    │
│                                                                  │
│  Access tokens: 15 minutes to 1 hour                            │
│  Refresh tokens: 7-30 days                                       │
│                                                                  │
│                                                                  │
│  6. ADD .env TO .gitignore                                       │
│  ─────────────────────────                                       │
│                                                                  │
│  # .gitignore                                                    │
│  .env                                                            │
│  .env.local                                                      │
│  *.key                                                           │
│                                                                  │
│                                                                  │
│  7. USE ENVIRONMENT-SPECIFIC KEYS                                │
│  ────────────────────────────────                                │
│                                                                  │
│  Development: Test API keys                                      │
│  Production: Live API keys                                       │
│  Never mix them!                                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

# SUMMARY

```
┌─────────────────────────────────────────────────────────────────┐
│                    KEY TAKEAWAYS                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  AUTHENTICATION vs AUTHORIZATION:                                │
│  • Authentication = WHO are you? (login)                        │
│  • Authorization = WHAT can you do? (permissions)               │
│  • Auth happens FIRST, then AuthZ                               │
│                                                                  │
│  COMMON METHODS:                                                 │
│  • API Keys: Simple, for server-to-server                       │
│  • Basic Auth: Username:password encoded                        │
│  • JWT: Self-contained tokens, modern standard                  │
│  • OAuth: "Login with Google/Facebook/etc."                     │
│                                                                  │
│  TOKENS:                                                         │
│  • Access Token: Short-lived, for API access                    │
│  • Refresh Token: Long-lived, to get new access tokens          │
│  • Bearer Token: Format for sending tokens                      │
│                                                                  │
│  STATEFUL vs STATELESS:                                          │
│  • Stateful: Server stores session                              │
│  • Stateless: Token contains all info (JWT)                     │
│                                                                  │
│  HTTP CODES:                                                     │
│  • 401 Unauthorized: Authentication failed                      │
│  • 403 Forbidden: Authorization failed                          │
│                                                                  │
│  REMEMBER:                                                       │
│  • Never hardcode secrets                                        │
│  • Always use HTTPS                                              │
│  • Store API keys in environment variables                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

**Previous:** [13_Quick_Reference_Card.md](./13_Quick_Reference_Card.md)
**Back to Index:** [00_Index.md](./00_Index.md)
