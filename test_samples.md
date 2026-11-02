# Test Samples

| No. | Test URL | Expected Result | Status |
|---|---|---|---|
| 1 | `https://google.com` | No warning signs | Pass |
| 2 | `http://example.com` | HTTP warning | Pass |
| 3 | `https://user@example.com` | @ symbol warning | Pass |
| 4 | Long URL over 100 characters | Length warning | Pass |
| 5 | `http://192.168.1.1/login` | IP address and HTTP warnings | Pass |
| 6 | `https://a.b.c.d.example.com` | Many subdomains warning | Pass |
| 7 | `https://xn--e1afmkfd.example` | Punycode warning | Pass |
