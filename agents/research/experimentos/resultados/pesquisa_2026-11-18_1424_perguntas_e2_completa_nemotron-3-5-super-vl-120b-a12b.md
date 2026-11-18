# Agente Pesquisa RAG (com LLM)

| q | esperado | posição na busca | na busca inicial | aprofundado | ferramentas chamadas | achado por nova consulta | nos achados | novas consultas | s |
|---|---|---|---|---|---|---|---|---|---|
| q-001 | DAN-211 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-002 | DAN-142 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-003 | DAN-164 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-004 | DAN-137 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-005 | DAN-015 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-006 | DAN-015 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-007 | DAN-142 | 3 | sim | sim | search | não | sim | 0 | 7 |
| q-008 | DAN-142 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-009 | DAN-137 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-010 | DAN-137 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-011 | DAN-211 | 6 | sim | sim | search | não | sim | 0 | 7 |
| q-012 | DAN-211 | 5 | sim | sim | search | não | sim | 0 | 8 |
| q-013 | DAN-078 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-014 | DAN-078 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-015 | DAN-067 | 2 | sim | sim | search | não | sim | 0 | 14 |
| q-016 | DAN-067 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-017 | DAN-162 | 1 | sim | sim | search | não | sim | 0 | 26 |
| q-018 | DAN-162 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-019 | DAN-164 | 4 | sim | sim | search | não | sim | 0 | 8 |
| q-020 | DAN-164 | 4 | sim | sim | search | não | sim | 0 | 13 |
| q-021 | DAN-104 | 6 | sim | sim | search | não | sim | 0 | 12 |
| q-022 | DAN-104 | 4 | sim | sim | search | não | sim | 0 | 9 |
| q-023 | DAN-004 | 5 | sim | sim | search | não | sim | 0 | 10 |
| q-024 | DAN-004 | 1 | sim | sim | search | não | sim | 0 | 24 |
| q-025 | DAN-011 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-026 | DAN-011 | 1 | sim | sim | search | não | sim | 0 | 25 |
| q-027 | DAN-137 | 2 | sim | sim | search | não | sim | 0 | 7 |
| q-028 | DAN-137 | 2 | sim | sim | search | não | sim | 0 | 11 |
| q-029 | DAN-078 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-030 | DAN-078 | 1 | sim | sim | search | não | sim | 0 | 19 |
| q-031 | DAN-104 | 10 | sim | sim | search | não | sim | 0 | 14 |
| q-032 | DAN-104 | 7 | sim | sim | search | não | sim | 0 | 15 |
| q-033 | DAN-004 | 8 | sim | sim | search | não | sim | 0 | 18 |
| q-034 | DAN-004 | 12 | não | não | search | não | não | 0 | 12 |
| q-035 | DAN-019 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-036 | DAN-019 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-037 | DAN-090 | 2 | sim | sim | search | não | sim | 0 | 6 |
| q-038 | DAN-090 | 2 | sim | sim | search | não | sim | 0 | 6 |
| q-039 | (nenhum) | — | — | — | find → find | — | — | 4 | 8 |
| q-040 | (nenhum) | — | — | — | search | — | — | 0 | 10 |
| q-041 | (nenhum) | — | — | — | find → find | — | — | 4 | 8 |
| q-042 | (nenhum) | — | — | — | find → find | — | — | 4 | 17 |
| q-043 | (nenhum) | — | — | — | search | — | — | 0 | 18 |
| q-044 | DAN-001 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-045 | DAN-001 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-046 | DAN-003 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-047 | DAN-003 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-048 | DAN-017 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-049 | DAN-017 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-050 | DAN-018 | 3 | sim | sim | search | não | sim | 0 | 12 |
| q-051 | DAN-018 | 2 | sim | sim | search | não | sim | 0 | 6 |
| q-052 | DAN-020 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-053 | DAN-020 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-054 | DAN-022 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-055 | DAN-022 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-056 | DAN-026 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-057 | DAN-026 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-058 | DAN-033 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-059 | DAN-033 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-060 | DAN-042 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-061 | DAN-042 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-062 | DAN-043 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-063 | DAN-043 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-064 | DAN-048 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-065 | DAN-048 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-066 | DAN-049 | 2 | sim | sim | search | não | sim | 0 | 14 |
| q-067 | DAN-049 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-068 | DAN-050 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-069 | DAN-050 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-070 | DAN-058 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-071 | DAN-058 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-072 | DAN-059 | 2 | sim | sim | search | não | sim | 0 | 14 |
| q-073 | DAN-059 | 2 | sim | sim | search | não | sim | 0 | 14 |
| q-074 | DAN-060 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-075 | DAN-060 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-076 | DAN-065 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-077 | DAN-065 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-078 | DAN-069 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-079 | DAN-069 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-080 | DAN-073 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-081 | DAN-073 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-082 | DAN-076 | 1 | sim | sim | search | não | sim | 0 | 3 |
| q-083 | DAN-076 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-084 | DAN-083 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-085 | DAN-083 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-086 | DAN-085 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-087 | DAN-085 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-088 | DAN-086 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-089 | DAN-086 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-090 | DAN-088 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-091 | DAN-088 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-092 | DAN-092 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-093 | DAN-092 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-094 | DAN-093 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-095 | DAN-093 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-096 | DAN-106 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-097 | DAN-106 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-098 | DAN-116 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-099 | DAN-116 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-100 | DAN-118 | 4 | sim | sim | search | não | sim | 0 | 20 |
| q-101 | DAN-118 | 4 | sim | sim | search | não | sim | 0 | 6 |
| q-102 | DAN-121 | 6 | sim | sim | search | não | sim | 0 | 12 |
| q-103 | DAN-121 | 4 | sim | sim | search | não | sim | 0 | 10 |
| q-104 | DAN-122 | 2 | sim | sim | search | não | sim | 0 | 8 |
| q-105 | DAN-122 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-106 | DAN-124 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-107 | DAN-124 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-108 | DAN-125 | 2 | sim | sim | search | não | sim | 0 | 9 |
| q-109 | DAN-125 | 1 | sim | sim | search | não | sim | 0 | 42 |
| q-110 | DAN-126 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-111 | DAN-126 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-112 | DAN-127 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-113 | DAN-127 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-114 | DAN-129 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-115 | DAN-129 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-116 | DAN-145 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-117 | DAN-145 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-118 | DAN-148 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-119 | DAN-148 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-120 | DAN-152 | 3 | sim | sim | search | não | sim | 0 | 10 |
| q-121 | DAN-152 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-122 | DAN-154 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-123 | DAN-154 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-124 | DAN-165 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-125 | DAN-165 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-126 | DAN-170 | 1 | sim | sim | search | não | sim | 0 | 22 |
| q-127 | DAN-170 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-128 | DAN-180 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-129 | DAN-180 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-130 | DAN-183 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-131 | DAN-183 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-132 | DAN-186 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-133 | DAN-186 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-134 | DAN-188 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-135 | DAN-188 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-136 | DAN-189 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-137 | DAN-189 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-138 | DAN-194 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-139 | DAN-194 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-140 | DAN-197 | 3 | sim | sim | search | não | sim | 0 | 6 |
| q-141 | DAN-197 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-142 | DAN-200 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-143 | DAN-200 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-144 | DAN-204 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-145 | DAN-204 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-146 | DAN-205 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-147 | DAN-205 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-148 | DAN-207 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-149 | DAN-207 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-150 | DAN-208 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-151 | DAN-208 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-152 | DAN-215 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-153 | DAN-215 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-154 | DAN-226 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-155 | DAN-226 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-156 | DAN-235 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-157 | DAN-235 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-158 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-159 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 3 |
| q-160 | DAN-237 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-161 | DAN-237 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-162 | DAN-240 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-163 | DAN-240 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-164 | DAN-001 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-165 | DAN-001 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-166 | DAN-003 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-167 | DAN-003 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-168 | DAN-017 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-169 | DAN-017 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-170 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 19 |
| q-171 | DAN-018 | 4 | sim | sim | search | não | sim | 0 | 15 |
| q-172 | DAN-020 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-173 | DAN-020 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-174 | DAN-022 | 1 | sim | sim | search | não | sim | 0 | 22 |
| q-175 | DAN-022 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-176 | DAN-026 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-177 | DAN-026 | 1 | sim | sim | search | não | sim | 0 | 25 |
| q-178 | DAN-033 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-179 | DAN-033 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-180 | DAN-042 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-181 | DAN-042 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-182 | DAN-043 | 1 | sim | sim | search | não | sim | 0 | 19 |
| q-183 | DAN-043 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-184 | DAN-048 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-185 | DAN-048 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-186 | DAN-049 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-187 | DAN-049 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-188 | DAN-050 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-189 | DAN-050 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-190 | DAN-058 | 2 | sim | sim | search | não | sim | 0 | 12 |
| q-191 | DAN-058 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-192 | DAN-059 | 2 | sim | sim | search | não | sim | 0 | 9 |
| q-193 | DAN-059 | 2 | sim | sim | search | não | sim | 0 | 11 |
| q-194 | DAN-060 | 3 | sim | sim | search | não | sim | 0 | 9 |
| q-195 | DAN-060 | 1 | sim | sim | search | não | sim | 0 | 16 |
| q-196 | DAN-065 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-197 | DAN-065 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-198 | DAN-069 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-199 | DAN-069 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-200 | DAN-073 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-201 | DAN-073 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-202 | DAN-076 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-203 | DAN-076 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-204 | DAN-083 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-205 | DAN-083 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-206 | DAN-085 | 2 | sim | sim | search | não | sim | 0 | 7 |
| q-207 | DAN-085 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-208 | DAN-086 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-209 | DAN-086 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-210 | DAN-088 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-211 | DAN-088 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-212 | DAN-092 | 1 | sim | sim | search | não | sim | 0 | 21 |
| q-213 | DAN-092 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-214 | DAN-093 | 3 | sim | sim | search | não | sim | 0 | 17 |
| q-215 | DAN-093 | 3 | sim | sim | search | não | sim | 0 | 11 |
| q-216 | DAN-106 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-217 | DAN-106 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-218 | DAN-116 | 9 | sim | sim | search | não | sim | 0 | 7 |
| q-219 | DAN-116 | 7 | sim | sim | search | não | sim | 0 | 11 |
| q-220 | DAN-118 | 2 | sim | sim | search | não | sim | 0 | 16 |
| q-221 | DAN-118 | 2 | sim | sim | search | não | sim | 0 | 13 |
| q-222 | DAN-121 | 4 | sim | sim | search | não | sim | 0 | 11 |
| q-223 | DAN-121 | 8 | sim | sim | search | não | sim | 0 | 13 |
| q-224 | DAN-122 | 2 | sim | sim | search | não | sim | 0 | 10 |
| q-225 | DAN-122 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-226 | DAN-124 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-227 | DAN-124 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-228 | DAN-125 | 11 | não | não | search | não | não | 0 | 11 |
| q-229 | DAN-125 | 10 | sim | sim | search | não | sim | 0 | 12 |
| q-230 | DAN-126 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-231 | DAN-126 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-232 | DAN-127 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-233 | DAN-127 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-234 | DAN-129 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-235 | DAN-129 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-236 | DAN-145 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-237 | DAN-145 | 1 | sim | sim | search | não | sim | 0 | 23 |
| q-238 | DAN-148 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-239 | DAN-148 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-240 | DAN-152 | 4 | sim | sim | search | não | sim | 0 | 19 |
| q-241 | DAN-152 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-242 | DAN-154 | — | não | não | search | não | não | 0 | 11 |
| q-243 | DAN-154 | 12 | não | não | search | não | não | 0 | 13 |
| q-244 | DAN-165 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-245 | DAN-165 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-246 | DAN-170 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-247 | DAN-170 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-248 | DAN-180 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-249 | DAN-180 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-250 | DAN-183 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-251 | DAN-183 | 1 | sim | sim | search | não | sim | 0 | 22 |
| q-252 | DAN-186 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-253 | DAN-186 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-254 | DAN-188 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-255 | DAN-188 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-256 | DAN-189 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-257 | DAN-189 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-258 | DAN-194 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-259 | DAN-194 | 1 | sim | sim | search | não | sim | 0 | 4 |
| q-260 | DAN-197 | 19 | não | não | search | não | não | 0 | 17 |
| q-261 | DAN-197 | — | não | não | search | não | não | 0 | 20 |
| q-262 | DAN-200 | 10 | sim | sim | search | não | sim | 0 | 10 |
| q-263 | DAN-200 | 5 | sim | sim | search | não | sim | 0 | 11 |
| q-264 | DAN-204 | 3 | sim | sim | search | não | sim | 0 | 12 |
| q-265 | DAN-204 | 2 | sim | sim | search | não | sim | 0 | 8 |
| q-266 | DAN-205 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-267 | DAN-205 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-268 | DAN-207 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-269 | DAN-207 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-270 | DAN-208 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-271 | DAN-208 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-272 | DAN-215 | 1 | sim | sim | search | não | sim | 0 | 12 |
| q-273 | DAN-215 | 2 | sim | sim | search | não | sim | 0 | 11 |
| q-274 | DAN-226 | 1 | sim | sim | search | não | sim | 0 | 7 |
| q-275 | DAN-226 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-276 | DAN-235 | 1 | sim | sim | search | não | sim | 0 | 15 |
| q-277 | DAN-235 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-278 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-279 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-280 | DAN-237 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-281 | DAN-237 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-282 | DAN-240 | 1 | sim | sim | search | não | sim | 0 | 13 |
| q-283 | DAN-240 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-284 | DAN-164 | 1 | sim | sim | search | não | sim | 0 | 18 |
| q-285 | DAN-164 | 1 | sim | sim | search | não | sim | 0 | 9 |
| q-286 | DAN-104 | 1 | sim | sim | search | não | sim | 0 | 10 |
| q-287 | DAN-104 | 1 | sim | sim | search | não | sim | 0 | 17 |
| q-288 | DAN-090 | 1 | sim | sim | search | não | sim | 0 | 8 |
| q-289 | DAN-090 | 1 | sim | sim | search | não | sim | 0 | 11 |
| q-290 | DAN-071 | 3 | sim | sim | search | não | sim | 0 | 10 |
| q-291 | DAN-071 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-292 | DAN-084 | 1 | sim | sim | search | não | sim | 0 | 6 |
| q-293 | DAN-084 | 1 | sim | sim | search | não | sim | 0 | 5 |
| q-294 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 14 |
| q-295 | DAN-236 | 1 | sim | sim | search | não | sim | 0 | 12 |

## q-001 (esperado: DAN-211)

- busca inicial: DAN-211, DAN-154, DAN-059, DAN-145, DAN-148, DAN-023, DAN-209, DAN-011, DAN-193, DAN-024
- justificativa: 
- aprofundar DAN-211: `Roblox outage root cause Consul BoltDB fix remediation` — É o único incidente sobre a mesma interrupção do Roblox em outubro de 2021, com mesmo componente (Consul streaming) e duração de 73 horas.
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.833: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  But what was going on with the slow leaders? We did not figure this out during the incident, but HashiCorp engineers determined the root cause in the
  - DAN-211 (llm) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.804: ### Early Triage (10/28 13:37 – 10/29 02:00)  The initial investigation suggested that the Consul cluster that Vault and many other services depend on was unhealthy.  Specifically, the Consul cluster 
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 

## q-002 (esperado: DAN-142)

- busca inicial: DAN-142, DAN-154, DAN-137, DAN-173, DAN-086, DAN-016, DAN-011, DAN-009, DAN-017, DAN-226
- justificativa: 
- aprofundar DAN-142: `content validator bug out-of-bounds memory read BSOD fix revert` — É exatamente o mesmo incidente CrowdStrike de julho de 2024, com mesma causa (bug no Content Validator) e mesmo efeito (BSOD em Windows), ao contrário dos outros que são de outros provedores e causas diferentes.
  - DAN-142 (llm) [Q: What happened?] 0.651: ### Q: What happened?  On July 19, 2024, a Rapid Response Content update was delivered to certain Windows hosts, evolving a new sensor capability first released in February 2024 that enabled visibilit
  - DAN-142 (llm) [What Went Wrong and Why?] 0.581: ### What Went Wrong and Why?  Template Type Stress Testing: On March 05, 2024, a stress test of the IPC Template Type was executed in our staging environment, which consists of a variety of operating 
  - DAN-142 (causa) [Third Party Validation] 0.38: ### Third Party Validation  - Conduct multiple independent third-party security code reviews. - Conduct independent reviews of end-to-end quality processes from development through deployment.  *In ad
  - DAN-142 (correcao) [Q: Has this issue been fixed?] 0.463: ### Q: Has this issue been fixed?  Channel File 291 was identified and fixed 78 minutes after it was released, at 1:27 a.m. EDT on July 19. A logic error in our Content Validator (software that perfor
  - DAN-142 (correcao) [Remediation Videos] 0.449: ## Remediation Videos  ### CrowdStrike Host Self-Remediation for Remote Users  This video outlines the steps required to self-remediate impacted remote Windows laptops. Follow these instructions if di

## q-003 (esperado: DAN-164)

- busca inicial: DAN-164, DAN-097, DAN-094, DAN-078, DAN-058, DAN-132, DAN-056, DAN-043, DAN-146, DAN-175
- justificativa: 
- aprofundar DAN-164: `root cause wrong directory deleted database replication lag recovery fix` — É o único incidente do GitLab na lista e corresponde diretamente ao incidente de banco de dados de 2017: admin deletou o diretório errado, replicação atrasou e houve perda de dados.
  - DAN-164 (llm) [Root cause analysis] 0.77: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.698: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-004 (esperado: DAN-137)

- busca inicial: DAN-137, DAN-005, DAN-012, DAN-016, DAN-019, DAN-011, DAN-087, DAN-010, DAN-008, DAN-007
- justificativa: 
- aprofundar DAN-137: `WAF rule regular expression backtracking CPU exhaustion 502 fix rollback` — DAN-137 é o único que descreve exatamente uma regex mal escrita em uma regra WAF/firewall causando esgotamento de CPU e downtime global na Cloudflare em julho de 2019, correspondendo ao incidente atual (regex na regra de firewall e erros 502). Outros incidentes envolvem configurações BGP, banco de dados, roteamento ou Lua, não regex em WAF.
  - DAN-137 (llm) [The events of July 2] 0.737: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (llm) [Appendix: About Regular Expression Backtracking] 0.726: ### Appendix: About Regular Expression Backtracking  To fully understand how ``(?:(?:\"|'|\]|\}|\\|\d|(?:nan|infinity|true|false|null|undefined|symbol|math)|\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*
  - DAN-137 (causa) [sem seção] 0.482: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D

## q-005 (esperado: DAN-015)

- busca inicial: DAN-015, DAN-140, DAN-053, DAN-184, DAN-073, DAN-221, DAN-044, DAN-017, DAN-086, DAN-131
- justificativa: 
- aprofundar DAN-015: `credential rotation storage credentials authentication failure fix` — Bate por envolver rotação de credenciais de armazenamento de objetos e falha de autenticação após remoção das credenciais antigas; não bate por ser específico do R2 da Cloudflare.
- aprofundar DAN-017: `deployment bug staging production HTTP 401 authentication fix` — Bate por erros HTTP 401 de autenticação causados por implantação incorreta; não bate por não envolver rotação de credenciais.
- aprofundar DAN-044: `bad config Azure Storage service interruption root cause fix` — Bate por interrupção de serviço de armazenamento causada por configuração ruim; não bate por não mencionar rotação de credenciais nem erros de autenticação.
  - DAN-015 (llm) [Next steps] 0.698: ## Next steps  The list above is not exhaustive: as we work through the above items, we will likely uncover other improvements to our systems, controls, and processes that we’ll be applying to improve
  - DAN-015 (llm) [Next steps] 0.669: ## Next steps  This incident happened because of human error and lasted longer than it should have because we didn’t have proper visibility into which credentials were being used by the R2 Gateway Wor
  - DAN-015 (causa) [Incident timeline] 0.42: ## Incident timeline  Given gradual decline in availability metrics, R2 engineering team suspected a potential regression in propagation of new credentials in storage infrastructure. | | Mar 21, 2025 
  - DAN-015 (correcao) [Resolution] 0.484: ## Resolution  Once we identified the root cause, we were able to resolve the incident quickly by deploying the new credentials to the production R2 Gateway Worker. This resulted in an immediate recov
  - DAN-015 (correcao) [sem seção] 0.434: We’re deeply sorry for this incident and the disruption it may have caused to you or your users. We hold ourselves to a high standard and this is not acceptable. This blog post exactly explains the im
  - DAN-017 (llm) [Analysis] 0.516: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [What was impacted] 0.511: ### What was impacted  A number of Cloudflare services depend on Workers KV for distributing configuration, routing information, static asset serving, and authentication state globally. These services
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Resolution] 0.424: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-044 (llm) [Update to Azure Customers:] 0.802: ## Update to Azure Customers:  Incident Information Incident ID 3071402 Incident Title Microsoft Azure Service Incident : Connectivity to multiple Azure Services – Partial Service Interruption Service
  - DAN-044 (llm) [Update to Azure Customers:] 0.78: ## Update to Azure Customers:  We will continue to investigate what led to this event and will drive the needed improvements to avoid similar situations in the future. In the meantime, we believe it’s
  - DAN-044 (causa) [Update to Azure Customers:] 0.39: ## Update to Azure Customers:  As a mitigation, we leveraged Twitter and other social media forums. We also provided targeted communication to the Management Portal for affected customers as available
  - DAN-044 (correcao) [sem seção] 0.481: Once we detected this issue, the change was rolled back promptly, but a restart of the storage front ends was required in order to fully undo the update. Once the mitigation steps were deployed, most 
  - DAN-044 (correcao) [sem seção] 0.398: Update: 11/22/2014, 12:41 PM PST  Since Wednesday, we have been working to help a subset of customers take final steps to fully recover from Tuesday’s storage service interruption. The incident has no

## q-006 (esperado: DAN-015)

- busca inicial: DAN-015, DAN-184, DAN-140, DAN-221, DAN-086, DAN-009, DAN-066, DAN-053, DAN-017, DAN-204
- justificativa: 
- aprofundar DAN-015: `credential rotation storage credentials wrong environment authentication fix` — Trata de object storage (R2) com falha de autenticação logo após rotação de credenciais causada por flag de ambiente ausente, espelhando o incidente atual, embora o componente seja o R2 Gateway.
- aprofundar DAN-017: `deployment tool staging production 401 authentication error fix` — Erro de implantação faz produção apontar para build de staging e retornar 401, similar à confusão de ambiente, mas sem rotação de credenciais de storage.
- aprofundar DAN-009: `service tokens release error authentication 401 recovery fix` — Falha na release de tokens de serviço causa erros 401 em vários produtos, relacionado à autenticação, mas não à rotação de credenciais de object storage.
  - DAN-015 (llm) [Incident timeline] 0.668: ## Incident timeline  **All timestamps referenced are in Coordinated Universal Time (UTC).**  | Time | Event | |---|---| | Mar 21, 2025 - 19:49 UTC | The R2 engineering team started the credential rot
  - DAN-015 (llm) [Next steps] 0.65: ## Next steps  This incident happened because of human error and lasted longer than it should have because we didn’t have proper visibility into which credentials were being used by the R2 Gateway Wor
  - DAN-015 (causa) [Next steps] 0.493: ## Next steps  The list above is not exhaustive: as we work through the above items, we will likely uncover other improvements to our systems, controls, and processes that we’ll be applying to improve
  - DAN-015 (correcao) [Resolution] 0.484: ## Resolution  Once we identified the root cause, we were able to resolve the incident quickly by deploying the new credentials to the production R2 Gateway Worker. This resulted in an immediate recov
  - DAN-015 (correcao) [sem seção] 0.434: We’re deeply sorry for this incident and the disruption it may have caused to you or your users. We hold ourselves to a high standard and this is not acceptable. This blog post exactly explains the im
  - DAN-017 (llm) [Analysis] 0.562: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Analysis] 0.529: ### Analysis  Workers KV is a low-latency key-value store that allows users to store persistent data on Cloudflare's network, as close to the users as possible. This distributed key-value store is use
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Resolution] 0.424: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-009 (llm) [What went wrong?] 0.638: ### What went wrong?  As a result of the bug, any Cloudflare account that used a service token to authenticate during the 10 minutes “last seen at” release was out would have its “client secret” value
  - DAN-009 (llm) [How did we fix the issue?] 0.636: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i
  - DAN-009 (causa) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (correcao) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (correcao) [Incident Timeline] 0.424: ### Incident Timeline  At 2023-01-24 18:56 The same solution was implemented on the Cloudflare API account, impacting Cache Purge, Cache Reserve, Images and R2. **Impact ended for Cache Purge, Cache R

## q-007 (esperado: DAN-142)

- busca inicial: DAN-154, DAN-146, DAN-142, DAN-226, DAN-126, DAN-217, DAN-074, DAN-116, DAN-103, DAN-069
- justificativa: 
- aprofundar DAN-142: `content validator bug out-of-bounds memory read Windows BSOD security update revert fix` — O DAN-142 descreve uma atualização de conteúdo de segurança (CrowdStrike Falcon) que causou BSOD em massa em máquinas Windows devido a leitura fora de limites na memória, correspondendo diretamente ao incidente atual de Windows servers blue-screening após update de software de segurança.
  - DAN-142 (llm) [Q: What happened?] 0.736: ### Q: What happened?  On July 19, 2024, a Rapid Response Content update was delivered to certain Windows hosts, evolving a new sensor capability first released in February 2024 that enabled visibilit
  - DAN-142 (llm) [Technical Details] 0.597: ## Technical Details  - Technical Details on the outage can be found here: Read the blog Published 2024-07-20 0100 UTC - We assure our customers that *CrowdStrike is operating normally and this issue 
  - DAN-142 (causa) [What Went Wrong and Why?] 0.384: ### What Went Wrong and Why?  Template Type Stress Testing: On March 05, 2024, a stress test of the IPC Template Type was executed in our staging environment, which consists of a variety of operating 
  - DAN-142 (correcao) [Q: Has this issue been fixed?] 0.463: ### Q: Has this issue been fixed?  Channel File 291 was identified and fixed 78 minutes after it was released, at 1:27 a.m. EDT on July 19. A logic error in our Content Validator (software that perfor
  - DAN-142 (correcao) [Remediation Videos] 0.449: ## Remediation Videos  ### CrowdStrike Host Self-Remediation for Remote Users  This video outlines the steps required to self-remediate impacted remote Windows laptops. Follow these instructions if di

## q-008 (esperado: DAN-142)

- busca inicial: DAN-142, DAN-154, DAN-146, DAN-126, DAN-226, DAN-116, DAN-217, DAN-074, DAN-143, DAN-103
- justificativa: 
- aprofundar DAN-142: `content validator bug out-of-bounds memory read BSOD revert fix remediation` — Bate: atualização de software de segurança causando BSOD em muitos Windows servers de uma vez. Não bate: é específico do CrowdStrike Falcon, não necessariamente o mesmo produto do incidente atual.
  - DAN-142 (llm) [Q: What happened?] 0.664: ### Q: What happened?  On July 19, 2024, a Rapid Response Content update was delivered to certain Windows hosts, evolving a new sensor capability first released in February 2024 that enabled visibilit
  - DAN-142 (llm) [What Went Wrong and Why?] 0.594: ### What Went Wrong and Why?  Template Type Stress Testing: On March 05, 2024, a stress test of the IPC Template Type was executed in our staging environment, which consists of a variety of operating 
  - DAN-142 (causa) [Third Party Validation] 0.38: ### Third Party Validation  - Conduct multiple independent third-party security code reviews. - Conduct independent reviews of end-to-end quality processes from development through deployment.  *In ad
  - DAN-142 (correcao) [Q: Has this issue been fixed?] 0.463: ### Q: Has this issue been fixed?  Channel File 291 was identified and fixed 78 minutes after it was released, at 1:27 a.m. EDT on July 19. A logic error in our Content Validator (software that perfor
  - DAN-142 (correcao) [Remediation Videos] 0.449: ## Remediation Videos  ### CrowdStrike Host Self-Remediation for Remote Users  This video outlines the steps required to self-remediate impacted remote Windows laptops. Follow these instructions if di

## q-009 (esperado: DAN-137)

- busca inicial: DAN-137, DAN-016, DAN-005, DAN-011, DAN-012, DAN-139, DAN-035, DAN-007, DAN-183, DAN-220
- justificativa: 
- aprofundar DAN-137: `WAF rule regex backtracking CPU exhaustion root cause fix` — WAF rule change causou esgotamento de CPU, igual ao incidente atual (firewall + 100% CPU após mudança de regra); difere por ser backtracking de regex específico.
- aprofundar DAN-016: `deployed rule infinite loop 100% CPU cookie validation fix` — Nova regra implantada causou loop infinito e 100% de CPU, correspondendo à mudança de regra e ao consumo total de CPU; difere por envolver validação de cookie em rate-limiting, não WAF.
- aprofundar DAN-012: `WAF config change Lua exception ruleset module fix` — Mudança de configuração no WAF afetou o módulo de regras do proxy; corresponde ao componente WAF e mudança de configuração, mas difere pelo sintoma (HTTP 500, não CPU a 100%).
  - DAN-137 (llm) [The events of July 2] 0.742: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (llm) [Appendix: About Regular Expression Backtracking] 0.734: ### Appendix: About Regular Expression Backtracking  To fully understand how ``(?:(?:\"|'|\]|\}|\\|\d|(?:nan|infinity|true|false|null|undefined|symbol|math)|\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*
  - DAN-137 (causa) [sem seção] 0.482: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.693: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.677: ## Technical description of the error and how it happened  ``` for (rule in active_mitigations) {    // ... (ignore other rule types)    if (rule.match_current_request()) {        if (!has_valid_cooki
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Remediation and follow-up steps] 0.472: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-012 (llm) [What happened] 0.684: ### What happened  `[lua] Failed to run module rulesets callback late_routing: /usr/local/nginx-fl/lua/modules/init.lua:314: attempt to index field 'execute' (a nil value)` resulting in HTTP code 500 
  - DAN-012 (llm) [What happened] 0.667: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 

## q-010 (esperado: DAN-137)

- busca inicial: DAN-137, DAN-016, DAN-005, DAN-035, DAN-183, DAN-026, DAN-220, DAN-148, DAN-106, DAN-012
- justificativa: 
- aprofundar DAN-137: `WAF rule regular expression backtracking CPU exhaustion fix rollback` — Bate: regra de edge/WAF implantada causando esgotamento de CPU; não bate: regex específico versus regra de firewall genérica.
- aprofundar DAN-016: `DDoS mitigation rule cookie validation infinite loop 100% CPU fix` — Bate: regra recém implantada causando 100% CPU nos handlers de requisição do edge; não bate: regra de DDoS e validação de cookie versus firewall.
- aprofundar DAN-012: `WAF testing tool disable config change Lua exception proxy fix` — Bate: mudança de configuração do WAF propagada globalmente afetando o proxy; não bate: desativação de ferramenta de teste versus mudança de regra de firewall e erro 500 versus CPU.
  - DAN-137 (llm) [Appendix: About Regular Expression Backtracking] 0.751: ### Appendix: About Regular Expression Backtracking  To fully understand how ``(?:(?:\"|'|\]|\}|\\|\d|(?:nan|infinity|true|false|null|undefined|symbol|math)|\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*
  - DAN-137 (llm) [The events of July 2] 0.728: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (causa) [sem seção] 0.482: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.726: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.696: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
  - DAN-012 (llm) [What happened] 0.694: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (llm) [What happened] 0.613: ### What happened  `[lua] Failed to run module rulesets callback late_routing: /usr/local/nginx-fl/lua/modules/init.lua:314: attempt to index field 'execute' (a nil value)` resulting in HTTP code 500 
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 

## q-011 (esperado: DAN-211)

- busca inicial: DAN-220, DAN-020, DAN-129, DAN-109, DAN-066, DAN-211, DAN-222, DAN-101, DAN-144, DAN-113
- justificativa: 
- aprofundar DAN-020: `service discovery config bad client dependency failure fix` — Bate: envolve diretamente a camada de service discovery falhando globalmente e afetando clientes dependentes. Não bate: o gatilho é configuração ruim de um cliente, não lentidão de writes com timeout.
- aprofundar DAN-211: `Consul streaming BoltDB service discovery health check load fix` — Bate: envolve Consul (service discovery) com degradação de performance sob load de health checks. Não bate: incidente específico de streaming/BoltDB em outage de 73 horas.
- aprofundar DAN-109: `metadata service timeout storage node cascading failure recovery` — Bate: timeouts excedidos gerando cascata de falhas com retries que mantêm carga alta. Não bate: é DynamoDB metadata/storage, não service discovery.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.676: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (llm) [The failure of a core system] 0.67: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter
  - DAN-211 (llm) [Return to Service Attempt #1 (10/29 02:00 – 04:00)] 0.68: ### Return to Service Attempt #1 (10/29 02:00 – 04:00)  The reset went smoothly, and initially, the metrics looked good. When we removed the iptables block, the service discovery and health check load
  - DAN-211 (llm) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.646: ### Early Triage (10/28 13:37 – 10/29 02:00)  The initial investigation suggested that the Consul cluster that Vault and many other services depend on was unhealthy.  Specifically, the Consul cluster 
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.614: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.608: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-012 (esperado: DAN-211)

- busca inicial: DAN-220, DAN-020, DAN-129, DAN-109, DAN-211, DAN-066, DAN-222, DAN-113, DAN-101, DAN-133
- justificativa: 
- aprofundar DAN-020: `service discovery config bad client cascading fix` — Explicitly about service discovery being brought down globally by a dependent client, matching the current incident's service discovery slowness and cascading impact on other services.
- aprofundar DAN-211: `Consul performance degradation service discovery fix` — Involves Consul (service discovery) performance degradation affecting service discovery and health check load, closely matching the current incident's slow service discovery layer.
- aprofundar DAN-109: `metadata service timeout cascading failure fix` — Metadata services experienced load causing timeouts and cascading node failures, analogous to service discovery slowness and writes timing out with downstream service failures.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.673: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (llm) [A thundering herd] 0.655: ## A thundering herd  Back to our fateful day. When the smaller, latency-measuring cluster was recycled (scaled down and back up again), its nodes were unreachable for enough time for the larger clust
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter
  - DAN-211 (llm) [Return to Service Attempt #2 (10/29 04:00 – 10/30 02:00)] 0.674: ### Return to Service Attempt #2 (10/29 04:00 – 10/30 02:00)  At this point, it was clear that overall Consul usage was not the only contributing factor to the performance degradation that we first no
  - DAN-211 (llm) [Return to Service Attempt #1 (10/29 02:00 – 04:00)] 0.669: ### Return to Service Attempt #1 (10/29 02:00 – 04:00)  The reset went smoothly, and initially, the metrics looked good. When we removed the iptables block, the service discovery and health check load
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.614: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.578: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-013 (esperado: DAN-078)

- busca inicial: DAN-078, DAN-048, DAN-066, DAN-164, DAN-006, DAN-162, DAN-096, DAN-106, DAN-209, DAN-075
- justificativa: 
- aprofundar DAN-078: `network partition MySQL failover data divergence cross continent latency fix` — Bate: particionamento de rede causou failover de master MySQL e novo mestre não recebeu gravações, gerando divergência de dados entre sites. Não bate: foi durante manutenção planejada, não um hiccup espontâneo.
- aprofundar DAN-048: `RDS Multi-AZ failover MySQL configuration data loss fix` — Bate: failover de banco relacional resultou em perda de dados. Não bate: gatilho foi falha de hardware e configuração incorreta, não partição de rede entre regiões.
- aprofundar DAN-106: `EC2 RDS networking upgrade outage Availability Zones volume loss recovery` — Bate: erro de rede durante mudança afetou RDS entre zonas de disponibilidade. Não bate: não houve failover entre regiões com divergência de dados entre sites.
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.679: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [Incident timeline] 0.671: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-048 (llm) [Final thoughts] 0.827: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (llm) [Incorrect configuration variable] 0.808: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.788: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  With the opening up of API access in the affected Availability Zone, APIs were now operating across all Availabil
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.775: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Customers can choose to operate RDS instances either in a single Availability Zone (“single-AZ”) or replicated ac
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 

## q-014 (esperado: DAN-078)

- busca inicial: DAN-078, DAN-066, DAN-006, DAN-048, DAN-164, DAN-205, DAN-043, DAN-162, DAN-116, DAN-023
- justificativa: 
- aprofundar DAN-078: `MySQL master failover cross-continent latency writes not propagated data integrity recovery` — Bate por ter partição de rede entre data centers, failover do MySQL master e dados divergentes por latência intercontinental; não menciona exatamente dois sites ativos simultâneos, mas o mecanismo é o mesmo.
- aprofundar DAN-048: `RDS Multi-AZ failover MySQL configuration data loss recovery` — Bate por failover de banco (RDS Multi-AZ) com perda de dados após falha, embora o gatilho seja falha de hardware e não apenas pane de rede.
- aprofundar DAN-205: `data center connectivity high latency quorum failure recovery` — Bate por problemas de conectividade e alta latência entre data centers com impacto em quorum, mas não envolve divergência de dados de banco após failover.
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.691: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [Incident timeline] 0.675: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-048 (llm) [Incorrect configuration variable] 0.808: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (llm) [Final thoughts] 0.795: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-205 (llm) [The Outage] 0.645: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Background] 0.624: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (causa) [Long term] 0.47: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Outage Post-Mortem – April 13, 2013] 0.374: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 

## q-015 (esperado: DAN-067)

- busca inicial: DAN-068, DAN-067, DAN-064, DAN-023, DAN-209, DAN-191, DAN-069, DAN-063, DAN-070, DAN-062
- justificativa: 
- aprofundar DAN-067: `data center power failure generator restart control plane analytics outage` — Bate por pane de energia em datacenter afetando control plane e analytics, com atraso na restauração dos geradores; não bate o provedor específico.
- aprofundar DAN-068: `data center power loss breaker coordination redundant power paths fix` — Bate por pane completa de energia em datacenter por falha em disjuntores; não menciona analytics nem tempo de recuperação.
- aprofundar DAN-063: `utility power lost generator failure manual restart recovery fix` — Bate por perda de energia utilitária e falha de geradores exigindo intervenção manual; não envolve control panel/analytics.
  - DAN-067 (llm) [Disaster Recovery] 0.716: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 
  - DAN-067 (llm) [Flexential Data Center Power Failure] 0.697: ### Flexential Data Center Power Failure  The largest of the three facilities in Oregon is run by Flexential. We refer to this facility as “PDX-DC04”. Cloudflare leases space in PDX-04 where we house 
  - DAN-067 (causa) [Lessons and Remediation] 0.574: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-068 (llm) [What happened to the power in the data center?] 0.732: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.68: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.632: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.532: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i

## q-016 (esperado: DAN-067)

- busca inicial: DAN-067, DAN-068, DAN-064, DAN-069, DAN-023, DAN-063, DAN-191, DAN-060, DAN-209, DAN-062
- justificativa: 
- aprofundar DAN-067: `data center power failure control plane analytics outage remediation` — O título e o sintoma (painel/controle e analytics fora após falha de energia no datacenter) são quase idênticos ao incidente atual, embora a causa específica precise ser confirmada.
- aprofundar DAN-068: `breaker coordination data center power loss redundant power fix` — Trata-se de falha de energia em datacenter com camadas redundantes afetadas, mas o gatilho é configuração incorreta de disjuntores, não apenas perda de utilidade.
- aprofundar DAN-063: `utility power loss generator failover network config remediation` — Envolve perda de energia elétrica em AZ com falha de geradores e impacto em rede, embora inclua um problema de configuração de rede secundário.
  - DAN-067 (llm) [Lessons and Remediation] 0.755: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Flexential Data Center Power Failure] 0.728: ### Flexential Data Center Power Failure  The largest of the three facilities in Oregon is run by Flexential. We refer to this facility as “PDX-DC04”. Cloudflare leases space in PDX-04 where we house 
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-068 (llm) [What happened to the power in the data center?] 0.723: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.674: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.644: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.631: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.438: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo

## q-017 (esperado: DAN-162)

- busca inicial: DAN-162, DAN-026, DAN-164, DAN-020, DAN-096, DAN-075, DAN-194, DAN-186, DAN-066, DAN-078
- justificativa: 
- aprofundar DAN-162: `database migration DNS resolution failure recovery repointing cross-site connectivity temporary resolvers fix` — Corresponde exatamente: migração de banco quebrou DNS, e a tentativa de recuperação (repointing) quebrou conectividade entre sites, exatamente como o incidente atual.
- aprofundar DAN-026: `Puppet IP change DNS zone file corrupt recovery NXDOMAIN memory exhaustion fix` — Semelhança parcial: falha DNS com correção durante resposta que agravou o problema (zona corrompida), embora o gatilho seja mudança de IP e não migração de banco.
- aprofundar DAN-096: `MySQL ProxySQL failover emergency index throttling memory profiling connection failure fix` — Semelhança parcial: problema de banco de dados e ação de diagnóstico/correção (memory profiling) desencadeou outra falha, mas sem relação com DNS ou migração como gatilho.
  - DAN-162 (llm) [sem seção] 0.587: In October, we experienced one incident that resulted in degraded performance across GitHub services.  **October 11 05:59 UTC (lasting 19 hours and 12 minutes)**  On October 11, 2024, starting at 05:5
  - DAN-026 (llm) [What happened…] 0.695: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [Total number of processes across fileservers] 0.629: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (causa) [What we’re doing about it…] 0.461: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [Summary] 0.443: # Summary  We realize that GitHub is an important part of your development and workflow. Again, I would like to take a moment to apologize for the impact that this outage had to your operations. We ta
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.686: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.651: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev

## q-018 (esperado: DAN-162)

- busca inicial: DAN-162, DAN-026, DAN-010, DAN-164, DAN-075, DAN-020, DAN-087, DAN-066, DAN-186, DAN-049
- justificativa: 
- aprofundar DAN-162: `database migration broke DNS resolution recovery temporary resolvers fix` — É o único caso em que uma migração de banco de dados quebrou diretamente a resolução DNS em um site, mesmo gatilho e sintoma do incidente atual, embora a recuperação tenha exigido repointing entre sites e deploy de resolvers temporários.
  - DAN-162 (llm) [sem seção] 0.538: In October, we experienced one incident that resulted in degraded performance across GitHub services.  **October 11 05:59 UTC (lasting 19 hours and 12 minutes)**  On October 11, 2024, starting at 05:5

## q-019 (esperado: DAN-164)

- busca inicial: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048, DAN-092, DAN-091, DAN-058, DAN-103, DAN-066
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion human error backup recovery postmortem` — Bate: engenheiros deletaram banco de produção por acidente, com backup e perda de dados, igual ao incidente atual. Não bate: banco gerenciado DigitalOcean com backup diário, não especifica comando de manutenção.
- aprofundar DAN-056: `accidental environment variable truncate production database root cause fix` — Bate: erro humano envolvendo banco de produção com perda/truncamento de dados. Não bate: variável de ambiente em testes, não comando de manutenção direto.
- aprofundar DAN-164: `admin deleted wrong directory database outage root cause remediation` — Bate: administrador deletou algo errado causando perda de dados no banco. Não bate: gatilho foi sobrecarga de replicação, não manutenção planejada.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.74: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.676: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-056 (llm) [What We Learned] 0.73: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.694: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a
  - DAN-164 (llm) [Root cause analysis] 0.709: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [sem seção] 0.605: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-020 (esperado: DAN-164)

- busca inicial: DAN-043, DAN-056, DAN-146, DAN-164, DAN-048, DAN-091, DAN-186, DAN-092, DAN-066, DAN-058
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion backup recovery root cause` — Escolhi porque relata exclusão acidental do banco de produção, igual ao incidente atual, embora o banco seja gerenciado da DigitalOcean com backup diário.
- aprofundar DAN-164: `admin deleted wrong directory database data loss fix` — Escolhi porque envolve administrador que excluiu o caminho errado causando perda de dados, sem ser exatamente exclusão do banco durante manutenção.
- aprofundar DAN-056: `environment variable tests truncate production database fix` — Escolhi porque descreve perda acidental de dados do banco de produção por variável de ambiente, embora o gatilho sejam testes e não manutenção direta.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.723: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [What happened?] 0.666: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [sem seção] 0.395: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-164 (llm) [Root cause analysis] 0.596: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [sem seção] 0.58: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.724: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.709: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-021 (esperado: DAN-104)

- busca inicial: DAN-189, DAN-191, DAN-209, DAN-103, DAN-106, DAN-104, DAN-067, DAN-048, DAN-146, DAN-084
- justificativa: 
- aprofundar DAN-104: `human error typo remove servers S3 outage fix remediation` — O operador digitou parâmetro errado ao remover servidores e derrubou serviço de armazenamento por horas, exatamente como o incidente atual; diferem apenas o provedor e o serviço específico.
- aprofundar DAN-189: `operator wrong parameter reboot all servers input validation fix` — O operador usou parâmetro incorreto em ferramenta com validação frouxa e afetou muito mais servidores do que o pretendido, semelhante ao erro humano do atual, embora seja reboot e não remoção de servidores e não seja serviço de armazenamento.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.655: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.644: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.612: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.543: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-022 (esperado: DAN-104)

- busca inicial: DAN-191, DAN-189, DAN-146, DAN-104, DAN-064, DAN-067, DAN-073, DAN-109, DAN-209, DAN-103
- justificativa: 
- aprofundar DAN-104: `S3 human error remove servers typo outage remediation` — Bate: operador executou comando para remover poucos servidores e removeu muitos por engano, derrubando armazenamento (S3) e dependentes. Não bate: foi erro de digitação em playbook da Amazon, não apenas remoção intencional.
- aprofundar DAN-189: `operator reboot servers input validation outage remediation` — Bate: erro de operador com comando em servidores afetou muitos além do previsto. Não bate: era reboot, não remoção, e não envolvia especificamente serviço de armazenamento.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.599: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.583: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.642: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.61: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-023 (esperado: DAN-004)

- busca inicial: DAN-012, DAN-005, DAN-137, DAN-051, DAN-004, DAN-011, DAN-016, DAN-220, DAN-023, DAN-009
- justificativa: 
- aprofundar DAN-004: `out of band WAF change Terraform pipeline blocked traffic fix` — Bate por mudança fora do pipeline de infraestrutura (Terraform) em WAF/firewall que bloqueou tráfego legítimo para UI e API; não bate por envolver gap de IAM-role e detecção automatizada de drift.
- aprofundar DAN-051: `firewall config iptables HAProxy blocked traffic fix` — Bate por configuração incorreta de firewall que bloqueou todo o tráfego dos sites; não bate por usar iptables em HAProxy e por ser uma interrupção curta de 6 minutos.
- aprofundar DAN-012: `WAF config change global rollout Lua exception fix` — Bate por mudança de configuração de WAF propagada sem rollout gradual afetando tráfego; não bate por ser exceção Lua no módulo de regras do proxy e não mencionar pipeline de infraestrutura.
  - DAN-004 (llm) [**Root Cause Analysis**] 0.671: ## **Root Cause Analysis**  While we manage all our infrastructure, including WAF, almost entirely with Terraform, we discovered during this incident a misconfiguration in IAM controls that allowed a 
  - DAN-004 (llm) [What Happened] 0.64: ## What Happened  - **01:15:** Initial investigation revealed broad connectivity issues between the frontend and our backing APIs, including CORS (Cross-Origin Resource Sharing) errors. The team explo
  - DAN-004 (causa) [Summary] 0.416: ## Summary  On April 4, 2025, from 00:16 to 01:49 UTC (approximately 1 hour and 33 minutes), CircleCI experienced a service disruption affecting both our user interface and build capabilities. During 
  - DAN-004 (correcao) [Future Prevention and Process Improvement] 0.505: ## Future Prevention and Process Improvement  This incident highlighted the strength of our existing systems while identifying several areas where we can improve and make them even more robust:  1. We
  - DAN-004 (correcao) [What Happened] 0.435: ## What Happened  (all times UTC)  The WAF is a critical security component that sits in front of our services and protects them from malicious traffic, while allowing legitimate requests to pass thro
  - DAN-051 (llm) [sem seção] 0.627: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi
  - DAN-051 (llm) [sem seção] 0.59: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f
  - DAN-012 (llm) [What happened] 0.726: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (llm) [What happened] 0.661: ### What happened  `[lua] Failed to run module rulesets callback late_routing: /usr/local/nginx-fl/lua/modules/init.lua:314: attempt to index field 'execute' (a nil value)` resulting in HTTP code 500 
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 

## q-024 (esperado: DAN-004)

- busca inicial: DAN-004, DAN-017, DAN-137, DAN-091, DAN-005, DAN-066, DAN-102, DAN-130, DAN-012, DAN-154
- justificativa: 
- aprofundar DAN-004: `IAM role WAF out-of-band Terraform drift detection fix` — Tráfego bloqueado para UI e build triggers (api.circleci.com, circleci.com) com mudança fora do pipeline de infra (IAM/WAF fora do Terraform), igual ao sintoma atual; não houve mudança no pipeline do incidente atual.
- aprofundar DAN-012: `WAF testing tool config Lua exception rulesets fix` — Mudança de configuração WAF se propagou globalmente causando erros HTTP, mas envolve mudança registrada, diferente de "nenhuma mudança encontrada" no incidente atual.
  - DAN-004 (llm) [**Root Cause Analysis**] 0.735: ## **Root Cause Analysis**  While we manage all our infrastructure, including WAF, almost entirely with Terraform, we discovered during this incident a misconfiguration in IAM controls that allowed a 
  - DAN-004 (llm) [Future Prevention and Process Improvement] 0.68: ## Future Prevention and Process Improvement  This incident highlighted the strength of our existing systems while identifying several areas where we can improve and make them even more robust:  1. We
  - DAN-004 (causa) [Summary] 0.416: ## Summary  On April 4, 2025, from 00:16 to 01:49 UTC (approximately 1 hour and 33 minutes), CircleCI experienced a service disruption affecting both our user interface and build capabilities. During 
  - DAN-004 (correcao) [What Happened] 0.473: ## What Happened  - **01:15:** Initial investigation revealed broad connectivity issues between the frontend and our backing APIs, including CORS (Cross-Origin Resource Sharing) errors. The team explo
  - DAN-004 (correcao) [What Happened] 0.435: ## What Happened  (all times UTC)  The WAF is a critical security component that sits in front of our services and protects them from malicious traffic, while allowing legitimate requests to pass thro
  - DAN-012 (llm) [What happened] 0.663: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (llm) [The runtime error] 0.633: ### The runtime error  ``` if rule_result.action == "execute" then   rule_result.execute.results = ruleset_results[tonumber(rule_result.execute.results_index)] end ``` This code expects that, if the r
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 

## q-025 (esperado: DAN-011)

- busca inicial: DAN-011, DAN-005, DAN-019, DAN-016, DAN-007, DAN-035, DAN-049, DAN-020, DAN-008, DAN-012
- justificativa: 
- aprofundar DAN-011: `database permissions bot detection file size limit global propagation fix` — Semelhante porque envolve sistema de filtro de tráfego (bot-detection), arquivo gerado automaticamente que excedeu limites e propagação global na rede, embora o gatilho seja permissão de banco.
- aprofundar DAN-012: `WAF configuration change global rollout proxy Lua exception fix` — Semelhante porque envolve ferramenta de filtragem de tráfego (WAF), mudança de configuração propagada globalmente sem rollout gradual, embora não mencione arquivo que cresceu.
- aprofundar DAN-008: `tiered cache configuration change CDN requests fail rollback fix` — Semelhante porque é incidente em CDN (Tiered Cache) com mudança que causou falhas globais em requests, embora não seja exatamente filtro de tráfego nem arquivo crescente.
  - DAN-011 (llm) [Memory preallocation] 0.556: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (llm) [Remediation and follow-up steps] 0.526: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-012 (llm) [What happened] 0.738: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (llm) [What happened] 0.672: ### What happened  `[lua] Failed to run module rulesets callback late_routing: /usr/local/nginx-fl/lua/modules/init.lua:314: attempt to index field 'execute' (a nil value)` resulting in HTTP code 500 
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 
  - DAN-008 (llm) [sem seção] 0.742: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.693: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac

## q-026 (esperado: DAN-011)

- busca inicial: DAN-011, DAN-005, DAN-019, DAN-016, DAN-007, DAN-012, DAN-049, DAN-035, DAN-008, DAN-018
- justificativa: 
- aprofundar DAN-012: `WAF testing tool config change global rollout Lua exception fix` — Bate porque é uma mudança de configuração propagada globalmente que gerou erros HTTP 500 em todo o CDN, mas não bate porque não envolve arquivo gerado automaticamente nem sistema de filtragem de tráfego.
- aprofundar DAN-011: `bot detection generated file exceeded limits propagated network outage fix` — Bate porque uma mudança gerou um arquivo que excedeu limites e se propagou pela rede causando pane generalizada, mas não bate porque o componente é bot-detection e o gatilho foi permissão de banco, não push de config de filtro de tráfego.
- aprofundar DAN-016: `DDoS mitigation rule rate limiting infinite loop CPU rollback fix` — Bate porque uma regra recém implantada de mitigação de DDoS (filtragem de tráfego) se propagou entre data centers causando falha, mas não bate porque o sintoma é loop de CPU por validação de cookie, não erro de CDN por arquivo de config.
  - DAN-012 (llm) [What happened] 0.702: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (llm) [What happened] 0.615: ### What happened  `[lua] Failed to run module rulesets callback late_routing: /usr/local/nginx-fl/lua/modules/init.lua:314: attempt to index field 'execute' (a nil value)` resulting in HTTP code 500 
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 
  - DAN-011 (llm) [Remediation and follow-up steps] 0.65: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [How Cloudflare processes requests, and how this went wrong today] 0.574: ## How Cloudflare processes requests, and how this went wrong today  This feature file is refreshed every few minutes and published to our entire network and allows us to react to variations in traffi
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.663: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.656: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi

## q-027 (esperado: DAN-137)

- busca inicial: DAN-016, DAN-137, DAN-183, DAN-005, DAN-025, DAN-035, DAN-011, DAN-113, DAN-114, DAN-148
- justificativa: 
- aprofundar DAN-016: `cookie validation infinite loop CPU root cause fix` — Nova regra de segurança implantada causou loop infinito e 100% CPU nos handlers de requisição, igual ao incidente atual; difere por envolver validação de cookie em vez de payloads específicos.
- aprofundar DAN-137: `WAF regular expression backtracking CPU exhaustion fix` — Regra WAF recém-implantada causou exaustão de CPU por backtracking excessivo, igual ao incidente atual; difere por ser regex mal escrita, não um loop condicional a payloads.
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.68: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.651: ## Technical description of the error and how it happened  ``` for (rule in active_mitigations) {    // ... (ignore other rule types)    if (rule.match_current_request()) {        if (!has_valid_cooki
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Remediation and follow-up steps] 0.472: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-137 (llm) [Appendix: About Regular Expression Backtracking] 0.778: ### Appendix: About Regular Expression Backtracking  To fully understand how ``(?:(?:\"|'|\]|\}|\\|\d|(?:nan|infinity|true|false|null|undefined|symbol|math)|\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*
  - DAN-137 (llm) [The events of July 2] 0.722: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (causa) [sem seção] 0.482: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D

## q-028 (esperado: DAN-137)

- busca inicial: DAN-016, DAN-137, DAN-148, DAN-005, DAN-064, DAN-183, DAN-106, DAN-035, DAN-129, DAN-115
- justificativa: 
- aprofundar DAN-016: `DDoS mitigation rule rate limiting cookie validation infinite loop CPU fix` — Nova regra de segurança (DDoS) causou 100% de CPU global após implantação, mas o resumo não menciona validação de cookie nem loops infinitos.
- aprofundar DAN-137: `WAF rule regular expression backtracking CPU exhaustion rollback fix` — Regra WAF de segurança causou exaustão de CPU global após implantação rápida, mas o atual não menciona regex nem backtracking.
- aprofundar DAN-005: `router rule configuration edge routers crash fix rollback` — Regra de configuração derrubou roteadores de borda globalmente, mas não é regra de segurança e não menciona CPU.
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.751: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.715: ## Technical description of the error and how it happened  ``` for (rule in active_mitigations) {    // ... (ignore other rule types)    if (rule.match_current_request()) {        if (!has_valid_cooki
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Remediation and follow-up steps] 0.472: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-137 (llm) [Appendix: About Regular Expression Backtracking] 0.751: ### Appendix: About Regular Expression Backtracking  To fully understand how ``(?:(?:\"|'|\]|\}|\\|\d|(?:nan|infinity|true|false|null|undefined|symbol|math)|\`|\-|\+)+[)]*;?((?:\s|-|~|!|{}|\|\||\+)*.*
  - DAN-137 (llm) [The events of July 2] 0.718: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (causa) [sem seção] 0.482: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D
  - DAN-005 (llm) [Bad Rule] 0.686: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.622: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp

## q-029 (esperado: DAN-078)

- busca inicial: DAN-078, DAN-066, DAN-048, DAN-205, DAN-006, DAN-164, DAN-043, DAN-091, DAN-023, DAN-143
- justificativa: 
- aprofundar DAN-078: `network partition MySQL failover write propagation data integrity recovery` — Mesmo gatilho (partição de rede entre data centers) e mesmo componente (banco de dados/MySQL) com failover automático e writes divergentes após recuperação, exigindo restauração de integridade; difere por ocorrer durante manutenção planejada e não um blip não planejado.
  - DAN-078 (llm) [Incident timeline] 0.704: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.684: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa

## q-030 (esperado: DAN-078)

- busca inicial: DAN-078, DAN-066, DAN-048, DAN-164, DAN-006, DAN-075, DAN-043, DAN-205, DAN-060, DAN-058
- justificativa: 
- aprofundar DAN-078: `network partition MySQL failover cross continent latency writes not propagated data integrity fix` — Partição de rede curta causou failover de banco e writes não propagados entre regiões, exatamente como o atual, embora tenha ocorrido durante manutenção.
- aprofundar DAN-205: `network latency data center quorum failover connectivity root cause fix` — Conectividade instável entre data centers afetou quorum e failover, mas não descreve divergem de writes em cada região após failover de banco.
  - DAN-078 (llm) [Incident timeline] 0.688: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.669: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-205 (llm) [The Outage] 0.658: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Background] 0.613: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (causa) [Long term] 0.47: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Outage Post-Mortem – April 13, 2013] 0.374: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 

## q-031 (esperado: DAN-104)

- busca inicial: DAN-189, DAN-210, DAN-109, DAN-125, DAN-191, DAN-220, DAN-064, DAN-103, DAN-143, DAN-104
- justificativa: 
- aprofundar DAN-104: `S3 typo remove servers playbook full restart root cause fix` — O operador pretendia remover poucos servidores via comando de playbook, mas um erro de digitação removeu um conjunto maior, exigindo reinicialização completa do serviço de armazenamento — igual ao incidente atual.
- aprofundar DAN-189: `Joyent reboot all servers missing flag lax input validation fix` — O operador queria reiniciar poucos servidores em manutenção, mas parâmetro ausente reiniciou todo o datacenter; o alvo é reinicialização e não remoção, mas o erro de parâmetro com escala não intencional se assemelha.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.541: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.53: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.603: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [What Happened?] 0.575: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (causa) [Next Steps] 0.434: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-032 (esperado: DAN-104)

- busca inicial: DAN-109, DAN-210, DAN-189, DAN-191, DAN-067, DAN-073, DAN-104, DAN-103, DAN-026, DAN-070
- justificativa: 
- aprofundar DAN-104: `human error command remove servers typo S3 outage fix` — Bate exatamente: comando destinado a remover poucos servidores removeu um conjunto maior por erro humano e derrubou o serviço de armazenamento S3, que precisou de reinicialização completa para se recuperar.
- aprofundar DAN-189: `operator reboot all servers lax input validation outage remediation` — Bate parcialmente: operador queria afetar poucos servidores em manutenção, mas validação de entrada falha afetou todo o datacenter, embora seja reinicialização e não remoção, e o componente afetado seja computação, não armazenamento.
- aprofundar DAN-109: `storage nodes metadata load timeout self shutdown recovery fix` — Bate parcialmente: envolve nós de armazenamento que se desligam sozinhos e não se recuperam, mas o gatilho é sobrecarga de metadados por falha de rede, não um comando do operador para remover servidores.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.642: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.613: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.646: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.621: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.549: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.533: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-033 (esperado: DAN-004)

- busca inicial: DAN-005, DAN-137, DAN-012, DAN-113, DAN-220, DAN-016, DAN-011, DAN-004, DAN-006, DAN-007
- justificativa: 
- aprofundar DAN-004: `WAF out-of-band change blocked traffic Terraform pipeline drift detection fix` — O DAN-004 envolve mudança fora do pipeline no WAF que bloqueou tráfego legítimo e resposta lenta porque a equipe assumiu que mudanças passam pelo pipeline, exatamente como o incidente atual.
- aprofundar DAN-012: `WAF config change global rollout Lua exception HTTP 500 fix` — O DAN-012 trata de mudança de configuração WAF propagada sem rollout gradual, mas não menciona a suposição de que mudanças passam pelo pipeline normal.
- aprofundar DAN-137: `WAF rule regex CPU exhaustion backtracking outage fix rollback` — O DAN-137 envolve uma regra WAF que causou pane global implantada rapidamente, mas não aborda a demora por confiar no pipeline de mudanças.
  - DAN-004 (llm) [**Root Cause Analysis**] 0.72: ## **Root Cause Analysis**  While we manage all our infrastructure, including WAF, almost entirely with Terraform, we discovered during this incident a misconfiguration in IAM controls that allowed a 
  - DAN-004 (llm) [What Happened] 0.683: ## What Happened  - **01:15:** Initial investigation revealed broad connectivity issues between the frontend and our backing APIs, including CORS (Cross-Origin Resource Sharing) errors. The team explo
  - DAN-004 (causa) [Summary] 0.416: ## Summary  On April 4, 2025, from 00:16 to 01:49 UTC (approximately 1 hour and 33 minutes), CircleCI experienced a service disruption affecting both our user interface and build capabilities. During 
  - DAN-004 (correcao) [Future Prevention and Process Improvement] 0.505: ## Future Prevention and Process Improvement  This incident highlighted the strength of our existing systems while identifying several areas where we can improve and make them even more robust:  1. We
  - DAN-004 (correcao) [What Happened] 0.435: ## What Happened  (all times UTC)  The WAF is a critical security component that sits in front of our services and protects them from malicious traffic, while allowing legitimate requests to pass thro
  - DAN-012 (llm) [What happened] 0.766: ### What happened  The graph below shows HTTP 500 errors served by our network during the incident timeframe (red line at the bottom), compared to unaffected total Cloudflare traffic (green line at th
  - DAN-012 (llm) [What happened] 0.739: ### What happened  `[lua] Failed to run module rulesets callback late_routing: /usr/local/nginx-fl/lua/modules/init.lua:314: attempt to index field 'execute' (a nil value)` resulting in HTTP code 500 
  - DAN-012 (causa) [sem seção] 0.396: *Note: This post was updated to clarify the relationship of the internal WAF tool with the incident on Dec. 5.*  On December 5, 2025, at 08:47 UTC (all times in this blog are UTC), a portion of Cloudf
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.524: ### What about the changes being made after the incident on November 18, 2025?  We made an unrelated change that caused a similar, <u>longer availability incident</u> two weeks ago on November 18, 202
  - DAN-012 (correcao) [What about the changes being made after the incident on November 18, 2025?] 0.458: ### What about the changes being made after the incident on November 18, 2025?  - **Enhanced Rollouts & Versioning**: Similar to how we slowly deploy software with strict health validation, data used 
  - DAN-137 (llm) [The events of July 2] 0.753: ### The events of July 2  The CPU exhaustion was caused by a single WAF rule that contained a poorly written regular expression that ended up creating excessive backtracking. The regular expression th
  - DAN-137 (llm) [sem seção] 0.734: ###  What went wrong  As noted, we deploy dozens of new rules to the WAF every week, and we have numerous systems in place to prevent any negative impact of that deployment. So when things do go wrong
  - DAN-137 (causa) [What happened] 0.441: ### What happened  Let’s begin with the sequence of events. All times in this blog are UTC.  At 13:42 an engineer working on the firewall team deployed a minor change to the rules for XSS detection vi
  - DAN-137 (correcao) [Conclusion] 0.559: ### Conclusion  This was an upsetting outage for our customers and for the team. We responded quickly to correct the situation and are correcting the process deficiencies that allowed the outage to oc
  - DAN-137 (correcao) [What’s happened since last Tuesday] 0.435: ### What’s happened since last Tuesday  Firstly, we stopped all release work on the WAF completely and are doing the following:  1. Re-introduce the excessive CPU usage protection that got removed. (D

## q-034 (esperado: DAN-004)

- busca inicial: DAN-005, DAN-137, DAN-051, DAN-012, DAN-220, DAN-011, DAN-016, DAN-014, DAN-006, DAN-113
- justificativa: 
- aprofundar DAN-051: `firewall configuration change blocked all traffic root cause fix` — Mesmo componente (firewall) e mesmo sintoma (todo tráfego bloqueado); difere porque lá havia uma mudança explícita de iptables, enquanto no atual ninguém lembra de ter mudado nada.
- aprofundar DAN-014: `human error disabled service admin tooling root cause fix` — Bate com 'ninguém lembra de fazer mudança' (erro humano durante operação desativou serviço sem querer), mas o componente é um gateway, não um firewall.
- aprofundar DAN-006: `typo network configuration traffic crash root cause fix` — Erro de configuração de rede afetando todo o tráfego, mas não se trata especificamente de uma regra de firewall bloqueando tudo.
  - DAN-051 (llm) [sem seção] 0.616: On August 25, 2014 there was an outage of all Stack Exchange sites (Q&A sites as well as Careers) from 7:26 pm to 7:32 pm UTC (approximately 6 minutes). The cause was an incorrect change to network fi
  - DAN-051 (llm) [sem seção] 0.581: - We need a mechanism to access our sites on the secondary/inactive load balancers, so that we can apply these changes there first. This was already planned, but this outage has highlighted the need f
  - DAN-014 (llm) [Deep dive] 0.624: ## Deep dive  **Due to human error and insufficient validation safeguards in our admin tooling, the R2 Gateway service was taken down as part of a routine remediation for a phishing URL.**  During a r
  - DAN-014 (llm) [Incident timeline and impact] 0.582: ## Incident timeline and impact  | | 2025-02-06 08:42 | Root cause identified as R2 team reviews service deployment history and configuration, which surfaces the action and the validation gap that all
  - DAN-014 (causa) [Incident timeline and impact] 0.428: ## Incident timeline and impact  The incident timeline, including the initial impact, investigation, root cause, and remediation, are detailed below.  **All timestamps referenced are in Coordinated Un
  - DAN-014 (correcao) [Remediation and follow-up steps] 0.593: ## Remediation and follow-up steps  We’re continuing to discuss & review additional steps and effort that can continue to reduce the blast radius of any system- or human- action that could result in d
  - DAN-014 (correcao) [Remediation and follow-up steps] 0.539: ## Remediation and follow-up steps  We have taken immediate steps to resolve the validation gaps in our tooling to prevent this specific failure from occurring in the future.  We are prioritizing seve
  - DAN-006 (llm) [sem seção] 0.563: Today a configuration error in our backbone network caused an outage for Internet properties and Cloudflare services that lasted 27 minutes. We saw traffic drop by about 50% across our network. Becaus
  - DAN-006 (llm) [Conclusion] 0.547: ### Conclusion  We’ve never experienced an outage on our backbone and our team responded quickly to restore service in the affected locations, but this was a very painful period for everyone involved.
  - DAN-006 (causa) [Timeline] 0.391: ### Timeline  All timestamps are UTC.  First, an issue occurred on the backbone link between Newark and Chicago which led to backbone congestion in between Atlanta and Washington, DC.  In responding t
  - DAN-006 (correcao) [What happened and what we’re doing about it] 0.372: ### What happened and what we’re doing about it  - Introduce a maximum-prefix limit on our backbone BGP sessions - this would have shut down the backbone in Atlanta, but our network is built to functi
  - DAN-006 (correcao) [What happened and what we’re doing about it] 0.314: ### What happened and what we’re doing about it  As there was backbone congestion in Atlanta, the team had decided to remove some of Atlanta’s backbone traffic. But instead of removing the Atlanta rou

## q-035 (esperado: DAN-019)

- busca inicial: DAN-019, DAN-007, DAN-006, DAN-022, DAN-005, DAN-065, DAN-059, DAN-023, DAN-159, DAN-113
- justificativa: 
- aprofundar DAN-019: `route leak BGP export prefix list filter internal IPv6 prefixes peers correction` — É o mais parecido: mudança na política de roteamento removeu filtros e anunciou prefixos internos para peers externos, exatamente o cenário do incidente atual.
- aprofundar DAN-007: `BGP advertised prefixes ordering malfunction root cause fix outage` — Envolve ordem incorreta de prefixos BGP anunciados em políticas de exportação, mas causa mau funcionamento em datacenters, não necessariamente vazamento para peers externos.
- aprofundar DAN-023: `backbone router configuration change route advertisement outage root cause fix` — Mudanças de configuração em routers backbone causaram outage global, mas o resumo não especifica vazamento de rotas internas para peers/provedores.
  - DAN-019 (llm) [What happened: the configuration error] 0.704: ### What happened: the configuration error  ``` policy-options policy-statement 6-TELIA-ACCEPT-EXPORT {     term ADV-SITELOCAL-GRE-RECEIVER {         from route-type internal;         then {          
  - DAN-019 (llm) [What happened: the configuration error] 0.691: ### What happened: the configuration error  [edit policy-options policy-statement 6-PRIVATE-PEER-ANYCAST-OUT term ADV-SITELOCAL from] -      prefix-list 6-BOG04-SITE-LOCAL; [edit policy-options policy
  - DAN-019 (causa) [What happened: the configuration error] 0.381: ### What happened: the configuration error  A|1769113609.854028|2801:14:9000::6:4112:1|64112|2a03:2880:f17c::/48|64112 22850 174 3356 13335 32934|IGP|2801:14:9000::6:4112:1|0|0|22850:65151|false|||pit
  - DAN-019 (correcao) [Follow-ups and preventing route leaks] 0.369: ### Follow-ups and preventing route leaks  We are big supporters and active contributors to efforts within the <u>IETF</u> and <u>infrastructure community</u> that strengthen routing security. We know
  - DAN-019 (correcao) [Timeline] 0.398: ### Timeline  | Time (UTC) | Event | |---|---| | 2026-01-22 19:52 UTC | A change that ultimately triggers the routing policy bug is merged in our network automation code repository | | 2026-01-22 20:2
  - DAN-007 (llm) [Incident timeline and impact] 0.726: ### Incident timeline and impact  In order to be reachable on the Internet, networks like Cloudflare make use of a protocol called BGP. As part of this protocol, operators define policies which decide
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.684: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We
  - DAN-023 (llm) [sem seção] 0.583: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.532: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da

## q-036 (esperado: DAN-019)

- busca inicial: DAN-019, DAN-007, DAN-005, DAN-006, DAN-059, DAN-022, DAN-023, DAN-210, DAN-159, DAN-013
- justificativa: 
- aprofundar DAN-019: `route leak BGP export policy prefix list filter removal fix` — O incidente envolve vazamento de rotas (route leak) após erro de política de roteamento que removeu filtros de prefixos na exportação BGP, anunciando prefixos internos a peers externos — igual ao sintoma atual, exceto ser IPv6 e durar 25 minutos.
- aprofundar DAN-007: `BGP advertised prefixes incorrect ordering disabled fix rollback` — O incidente trata de ordenação incorreta de prefixos BGP anunciados desabilitados em policy-statement, afetando anúncios de rotas em vários datacenters — parecido pelo componente BGP e mudança de política, mas não menciona peers/providers reportando rotas indevidas.
  - DAN-019 (llm) [What happened: the configuration error] 0.731: ### What happened: the configuration error  [edit policy-options policy-statement 6-PRIVATE-PEER-ANYCAST-OUT term ADV-SITELOCAL from] -      prefix-list 6-BOG04-SITE-LOCAL; [edit policy-options policy
  - DAN-019 (llm) [What happened: the configuration error] 0.704: ### What happened: the configuration error  On January 22, 2026, at 20:25 UTC, we pushed a change via our policy automation platform to remove the BGP announcements from Miami for one of our data cent
  - DAN-019 (causa) [What happened: the configuration error] 0.381: ### What happened: the configuration error  A|1769113609.854028|2801:14:9000::6:4112:1|64112|2a03:2880:f17c::/48|64112 22850 174 3356 13335 32934|IGP|2801:14:9000::6:4112:1|0|0|22850:65151|false|||pit
  - DAN-019 (correcao) [Follow-ups and preventing route leaks] 0.369: ### Follow-ups and preventing route leaks  We are big supporters and active contributors to efforts within the <u>IETF</u> and <u>infrastructure community</u> that strengthen routing security. We know
  - DAN-019 (correcao) [Timeline] 0.398: ### Timeline  | Time (UTC) | Event | |---|---| | 2026-01-22 19:52 UTC | A change that ultimately triggers the routing policy bug is merged in our network automation code repository | | 2026-01-22 20:2
  - DAN-007 (llm) [Incident timeline and impact] 0.707: ### Incident timeline and impact  In order to be reachable on the Internet, networks like Cloudflare make use of a protocol called BGP. As part of this protocol, operators define policies which decide
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.678: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We

## q-037 (esperado: DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-221, DAN-184, DAN-015, DAN-008, DAN-216, DAN-009, DAN-066, DAN-129
- justificativa: 
- aprofundar DAN-090: `certificate expired root cause fix renewal authentication` — Certificate expiry caused Firefox add-ons to stop working — directly parallels SSL certificate expiry breaking mobile app authentication. Same failure type: expired certificate causing service-wide auth failure.
- aprofundar DAN-086: `certificate expiration date invalid root cause fix Azure outage` — Certificate validity date bug caused Azure global outage — certificate-related failure but different trigger (leap year date calculation, not actual expiry). Worth checking for fix patterns.
  - DAN-090 (llm) [Root Cause Analysis] 0.63: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.412: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (causa) [sem seção] 0.366: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a
  - DAN-086 (llm) [Prevention] 0.668: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.664: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Detection] 0.426: ### Detection  - **Fail Fast.** GA failures were not surfaced until 75 minutes after a long timeout.  We are taking steps to better classify errors so that we fail-fast in these cases, alert these fai
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-038 (esperado: DAN-090)

- busca inicial: DAN-086, DAN-090, DAN-221, DAN-154, DAN-015, DAN-066, DAN-220, DAN-010, DAN-129, DAN-148
- justificativa: 
- aprofundar DAN-086: `certificate expiration leap year root cause fix remediation` — Certificados expiraram simultaneamente causando pane global, semelhante ao erro atual, embora o gatilho tenha sido ano bissexto.
- aprofundar DAN-090: `expired certificate add-ons root cause fix remediation` — Certificado expirado derrubou complementos de todos os clientes Firefox, correspondendo ao padrão de falha em massa por expiração de certificado.
  - DAN-086 (llm) [The Leap Day Bug] 0.618: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.557: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [Root Cause Analysis] 0.694: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.571: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (causa) [sem seção] 0.366: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q-039 (esperado: nenhum)

- busca inicial: DAN-152, DAN-173, DAN-222, DAN-050, DAN-017, DAN-045, DAN-051, DAN-216, DAN-224, DAN-230
- justificativa: 
- novos incidentes nos achados: DAN-177, DAN-122, DAN-237, DAN-124, DAN-142, DAN-018, DAN-029, DAN-095, DAN-226, DAN-094

## q-040 (esperado: nenhum)

- busca inicial: DAN-069, DAN-073, DAN-072, DAN-191, DAN-068, DAN-015, DAN-013, DAN-062, DAN-210, DAN-018
- justificativa: 
- aprofundar DAN-062: `severe weather power loss data center facility backup energy` — Escolhi porque cita clima severo causando perda de energia em instalação, o único com gatilho climático direto, embora seja Sydney e não Paris.
- aprofundar DAN-069: `transmission lines foliage alarm bug cascading failure fix` — Escolhi porque falha em linhas de transmissão por vegetação pode estar ligada a condições climáticas, mas não menciona clima nem Paris.
- aprofundar DAN-068: `breaker coordination settings power failure redundant paths` — Escolhi porque trata de falha de energia em data center com camadas redundantes, sem relação com clima ou Paris.
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.666: ### Summary of the AWS Service Event in the Sydney Region  If utility power is interrupted, the DRUPS uses this stored energy to continue to provide power to the datacenter while the integrated genera
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.638: ### Summary of the AWS Service Event in the Sydney Region  We’d like to share more detail about the AWS service disruption that occurred this past weekend in the AWS Sydney Region. The service disrupt
  - DAN-062 (causa) [Summary of the AWS Service Event in the Sydney Region] 0.399: ### Summary of the AWS Service Event in the Sydney Region  A latent bug in our instance management software led to a slower than expected recovery of the remaining instances. The team worked over the 
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.388: ### Summary of the AWS Service Event in the Sydney Region  Additionally, we will be taking actions to improve our recovery systems. The first is to fix the latent issue that led to our recovery system
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.359: ### Summary of the AWS Service Event in the Sydney Region  During the initial part of this event, customers experienced errors when trying to launch new instances, or when trying to scale their auto-s
  - DAN-069 (llm) [Cascade] 0.626: ## Cascade  ## Timeline  The following is the blackout's sequence of events on August 14, 2003 (times in EDT):  - 12:15 p.m. Incorrect telemetry data renders the state estimator, a power flow monitori
  - DAN-069 (llm) [Outages in the Cleveland-Akron area] 0.577: ## Outages in the Cleveland-Akron area  Cleveland-Akron area transmission lines began failing shortly after 3:00 p.m. Three 345 kV transmission lines failed between 3:05 p.m. to 3:42 p.m. due to tree 
  - DAN-069 (causa) [Computer failure] 0.545: ## Computer failure  A software bug known as a race condition existed in General Electric Energy's Unix-based XA/21 energy management system. Once triggered, the bug stalled FirstEnergy's control room
  - DAN-069 (correcao) [Restoration of service] 0.437: ## Restoration of service  Preparations against the possible disruptions threatened by the Year 2000 problem have been credited for the installation of new electrical equipment and systems which allow
  - DAN-069 (correcao) [Investigation efforts] 0.397: ## Investigation efforts  A joint federal task force was formed by the governments of Canada and the U.S. to oversee the investigation and report directly to Ottawa and Washington. The task force was 
  - DAN-068 (llm) [What happened to the power in the data center?] 0.677: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.585: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is

## q-041 (esperado: nenhum)

- busca inicial: DAN-055, DAN-161, DAN-056, DAN-050, DAN-177, DAN-124, DAN-028, DAN-152, DAN-173, DAN-011
- justificativa: 
- novos incidentes nos achados: DAN-131, DAN-136, DAN-132, DAN-053, DAN-142, DAN-017, DAN-042, DAN-029, DAN-013, DAN-039

## q-042 (esperado: nenhum)

- busca inicial: DAN-124, DAN-173, DAN-131, DAN-177, DAN-152, DAN-215, DAN-157, DAN-175, DAN-140, DAN-055
- justificativa: 
- novos incidentes nos achados: DAN-056, DAN-141, DAN-136, DAN-132, DAN-015, DAN-184, DAN-028, DAN-053, DAN-058, DAN-050

## q-043 (esperado: nenhum)

- busca inicial: DAN-026, DAN-049, DAN-075, DAN-020, DAN-043, DAN-013, DAN-164, DAN-087, DAN-145, DAN-010
- justificativa: 
- aprofundar DAN-013: `automated cleanup task BYOIP prefixes pending deletion root cause fix` — ambos envolvem exclusão automatizada de recursos após interpretação incorreta de fonte externa; difere por ser prefixos BYOIP, não registros DNS.
- aprofundar DAN-075: `DNS Enactor race condition cleanup deleted regional endpoint fix` — ambos envolvem exclusão de registro DNS por processo automatizado de limpeza; difere por ser condição de corrida, não fonte de dados brevemente indisponível.
- aprofundar DAN-026: `Puppet manifest DNS zone file rebuild corrupt NXDOMAIN fix` — ambos envolvem automação de DNS a partir de API interna; difere por corrupção de zona, não exclusão por suposição de obsolescência.
  - DAN-013 (llm) [How did the incident occur?] 0.701: ## How did the incident occur?  The specific piece of configuration that broke was a modification attempting to automate the customer action of removing prefixes from Cloudflare’s BYOIP service, a reg
  - DAN-013 (llm) [How did the incident occur?] 0.656: ## How did the incident occur?  ``` 	if v := req.URL.Query().Get("pending_delete"); v != "" { 		// ignore other behavior and fetch pending objects from the ip_prefixes_deleted table 		prefixes, err :=
  - DAN-013 (causa) [Why did Cloudflare not catch the bug in our staging environment or testing?] 0.41: ### Why did Cloudflare not catch the bug in our staging environment or testing?  Our staging environment contains data that matches Production as closely as possible, but was not sufficient in this ca
  - DAN-013 (correcao) [Remediation and follow-up steps] 0.461: ## Remediation and follow-up steps  ### API schema standardization  One of the issues in this incident is that the pending\_delete flag was interpreted as a string, making it difficult for both client
  - DAN-013 (correcao) [Why was recovery not immediate?] 0.446: ### Why was recovery not immediate?  Affected BYOIP prefixes were not all impacted in the same way, necessitating more intensive data recovery steps. As a part of Code Orange: Fail Small, we are build
  - DAN-075 (llm) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.651: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  Second, one of the other DNS Enactors then began applying one of the newer plans and rapidly progresse
  - DAN-075 (llm) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.643: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  The race condition involves an unlikely interaction between two of the DNS Enactors. Under normal oper
  - DAN-075 (causa) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.365: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  At 2:25 AM PDT, with the recovery of the DynamoDB APIs, DWFM began to re-establish leases with droplet
  - DAN-075 (correcao) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.384: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. We have already disabled the Dyna
  - DAN-075 (correcao) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.347: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  When this issue occurred at 11:48 PM PDT, all systems needing to connect to the DynamoDB service in th
  - DAN-026 (llm) [What happened…] 0.708: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.588: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto

## q-044 (esperado: DAN-001)

- busca inicial: DAN-001, DAN-218, DAN-144, DAN-029, DAN-106, DAN-147, DAN-211, DAN-129, DAN-134, DAN-208
- justificativa: 
- aprofundar DAN-001: `cluster resource management configuration error prevented instances start hardware available fix` — O incidente atual tem o mesmo gatilho (pico de tráfego por campanha de marketing) e a mesma falha (gerenciador de recursos do cluster impede novas instâncias apesar de hardware livre), então DAN-001 é o mais parecido; difere apenas nos detalhes da plataforma.
  - DAN-001 (llm) [Outage timeline #] 0.626: ## Outage timeline #  Also just before noon, traffic peaked at 200%-300% of the traffic from previous day, depending on service. At this stage, traffic was at its highest but due to excessive resource
  - DAN-001 (llm) [Analysis #] 0.624: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa

## q-045 (esperado: DAN-001)

- busca inicial: DAN-001, DAN-218, DAN-211, DAN-208, DAN-134, DAN-029, DAN-106, DAN-129, DAN-135, DAN-144
- justificativa: 
- aprofundar DAN-001: `cluster resource manager configuration error spare hardware fix` — Bate exatamente: tráfego disparado por campanha de marketing, gerenciador de cluster não inicia mais instâncias mesmo com hardware disponível. Diferença: é um postmortem já concluído, enquanto o incidente atual está em andamento.
  - DAN-001 (llm) [Analysis #] 0.586: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (llm) [Outage timeline #] 0.571: ## Outage timeline #  The special offer was to start at noon sharp, and a direct link to its item page had been published before. At 11:15 we manually scaled out Listing service in order to be prepare
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa

## q-046 (esperado: DAN-003)

- busca inicial: DAN-003, DAN-092, DAN-195, DAN-180, DAN-080, DAN-103, DAN-164, DAN-048, DAN-055, DAN-102
- justificativa: 
- aprofundar DAN-003: `column type change schema validation old rows rollback recovery fix` — Corresponde quase exatamente: deploy alterou tipo de coluna no PostgreSQL do serviço de distribuição de jobs, validação de schema falhou em linhas antigas e o rollback não resolveu, exigindo build que ignorasse o campo.
  - DAN-003 (llm) [What happened] 0.533: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.456: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s

## q-047 (esperado: DAN-003)

- busca inicial: DAN-003, DAN-092, DAN-180, DAN-080, DAN-103, DAN-095, DAN-181, DAN-195, DAN-164, DAN-058
- justificativa: 
- aprofundar DAN-003: `column type change schema validation old rows rollback fix` — Mesmo cenário: deploy mudou tipo de coluna no banco do serviço de distribuição, validação de schema falhou em linhas antigas e o rollback não resolveu; os demais incidentes não envolvem esse gatilho ou sintoma.
  - DAN-003 (llm) [What happened] 0.525: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.459: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s

## q-048 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-050, DAN-042, DAN-013, DAN-116, DAN-220, DAN-049, DAN-035, DAN-008, DAN-015
- justificativa: 
- aprofundar DAN-017: `deployment tool staging production version 401 unauthorized cascade root cause fix` — Bate quase exatamente: deployment tool fez produção referenciar build de staging, endpoint não autorizado retornando 401, falhas em cascata em vários produtos — igual ao incidente atual.
- aprofundar DAN-015: `credentials wrong environment deployment authentication failure fix` — Semelhança parcial: deploy atingiu o ambiente errado (default em vez de production) e causou falha de autenticação, mas não envolve staging nem versão de build.
- aprofundar DAN-050: `deployment bug download URL generation broken fix` — Semelhança parcial: bug em deployment quebrou requisições em massa, mas não há staging, versão de build ou erro 401.
  - DAN-017 (llm) [Analysis] 0.574: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Analysis] 0.565: ### Analysis  Workers KV is a low-latency key-value store that allows users to store persistent data on Cloudflare's network, as close to the users as possible. This distributed key-value store is use
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Resolution] 0.424: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-015 (llm) [Incident timeline] 0.613: ## Incident timeline  **All timestamps referenced are in Coordinated Universal Time (UTC).**  | Time | Event | |---|---| | Mar 21, 2025 - 19:49 UTC | The R2 engineering team started the credential rot
  - DAN-015 (llm) [Next steps] 0.582: ## Next steps  This incident happened because of human error and lasted longer than it should have because we didn’t have proper visibility into which credentials were being used by the R2 Gateway Wor
  - DAN-015 (causa) [Next steps] 0.493: ## Next steps  The list above is not exhaustive: as we work through the above items, we will likely uncover other improvements to our systems, controls, and processes that we’ll be applying to improve
  - DAN-015 (correcao) [Resolution] 0.484: ## Resolution  Once we identified the root cause, we were able to resolve the incident quickly by deploying the new credentials to the production R2 Gateway Worker. This resulted in an immediate recov
  - DAN-015 (correcao) [sem seção] 0.434: We’re deeply sorry for this incident and the disruption it may have caused to you or your users. We hold ourselves to a high standard and this is not acceptable. This blog post exactly explains the im
  - DAN-050 (llm) [Recovery] 0.71: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Summary] 0.652: ## Summary  On 2023-07-20 between 12:17 and 12:30 UTC all crate downloads from crates.io were broken due to a deployment that contained a bug in the download URL generation.  During this time we had a
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi

## q-049 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-050, DAN-042, DAN-015, DAN-220, DAN-008, DAN-013, DAN-066, DAN-049, DAN-029
- justificativa: 
- aprofundar DAN-017: `deployment tool staging build production HTTP 401 root cause fix rollback` — Corresponde quase exatamente: deployment tool apontou produção para staging, erro HTTP 401 e falhas em cascata em serviços dependentes. Não há diferença relevante.
  - DAN-017 (llm) [Analysis] 0.577: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Timeline] 0.554: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.

## q-050 (esperado: DAN-018)

- busca inicial: DAN-144, DAN-066, DAN-018, DAN-116, DAN-220, DAN-216, DAN-129, DAN-029, DAN-017, DAN-183
- justificativa: 
- aprofundar DAN-018: `React dependency array excessive API calls dashboard outage root cause fix` — O incidente descreve um bug de componente React no dashboard gerando chamadas excessivas de API, derrubando API e painel, exatamente como o incidente atual.
  - DAN-018 (llm) [What Happened] 0.707: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.694: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 

## q-051 (esperado: DAN-018)

- busca inicial: DAN-066, DAN-018, DAN-144, DAN-029, DAN-129, DAN-220, DAN-116, DAN-133, DAN-183, DAN-067
- justificativa: 
- aprofundar DAN-018: `React component dashboard excessive API calls dependency array fix root cause` — O resumo descreve exatamente o mesmo padrão: um bug no componente React do dashboard gerou chamadas excessivas de API que sobrecarregaram o sistema e derrubaram API e dashboard, assim como no incidente atual.
  - DAN-018 (llm) [What Happened] 0.664: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.643: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 

## q-052 (esperado: DAN-020)

- busca inicial: DAN-020, DAN-220, DAN-222, DAN-066, DAN-145, DAN-219, DAN-109, DAN-211, DAN-144, DAN-032
- justificativa: 
- aprofundar DAN-020: `bad service discovery config dependent client global outage root cause fix` — Descrição idêntica ao incidente atual: configuração ruim de service discovery em um cliente derruba o service discovery global quando cliente dependente cai.
- aprofundar DAN-211: `Consul service discovery health check load degradation fix` — Envolve service discovery e health check de serviços internos causando degradação, mas foca em Consul streaming e BoltDB, não em configuração ruim de cliente.
- aprofundar DAN-032: `autogenerated bad config took down Google services root cause fix` — Má configuração causou queda global de serviços, mas não menciona service discovery nem cliente dependente.
  - DAN-020 (llm) [The failure of a core system] 0.688: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.668: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter
  - DAN-211 (llm) [Return to Service Attempt #1 (10/29 02:00 – 04:00)] 0.683: ### Return to Service Attempt #1 (10/29 02:00 – 04:00)  The reset went smoothly, and initially, the metrics looked good. When we removed the iptables block, the service discovery and health check load
  - DAN-211 (llm) [Early Triage (10/28 13:37 – 10/29 02:00)] 0.657: ### Early Triage (10/28 13:37 – 10/29 02:00)  The initial investigation suggested that the Consul cluster that Vault and many other services depend on was unhealthy.  Specifically, the Consul cluster 
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-032 (llm) [Today’s outage for several Google services] 0.71: # Today’s outage for several Google services  Earlier today, most Google users who use logged-in services like Gmail, Google+, Calendar and Documents found they were unable to access those services fo
  - DAN-032 (llm) [Today’s outage for several Google services] 0.675: # Today’s outage for several Google services  With services once again working normally, our work is now focused on (a) removing the source of failure that caused today’s outage, and (b) speeding up r

## q-053 (esperado: DAN-020)

- busca inicial: DAN-020, DAN-220, DAN-066, DAN-145, DAN-109, DAN-205, DAN-151, DAN-219, DAN-222, DAN-211
- justificativa: 
- aprofundar DAN-020: `service discovery config bad client global outage root cause fix` — O resumo é praticamente idêntico ao incidente atual: configuração ruim de descoberta de serviço em um cliente derrubou a descoberta global quando um cliente dependente caiu.
- aprofundar DAN-211: `Consul streaming BoltDB service discovery health check load outage fix` — Menciona problemas de streaming do Consul e carga de descoberta de serviço/health check, mas o contexto é uma interrupção de 73 horas, não uma configuração ruim de um único cliente.
- aprofundar DAN-109: `network disruption metadata service load timeout storage node fix` — Falha em cascata por carga excessiva e retry, mas é camada de armazenamento DynamoDB, não descoberta de serviço com configuração ruim de cliente.
  - DAN-020 (llm) [The failure of a core system] 0.691: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.677: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter
  - DAN-211 (llm) [Return to Service Attempt #1 (10/29 02:00 – 04:00)] 0.711: ### Return to Service Attempt #1 (10/29 02:00 – 04:00)  The reset went smoothly, and initially, the metrics looked good. When we removed the iptables block, the service discovery and health check load
  - DAN-211 (llm) [Outage Summary] 0.696: ### Outage Summary  The outage was unique in both duration and complexity. The team had to address a number of challenges in sequence to understand the root cause and bring the service back up.  - The
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.651: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.637: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-054 (esperado: DAN-022)

- busca inicial: DAN-022, DAN-159, DAN-068, DAN-005, DAN-006, DAN-113, DAN-065, DAN-066, DAN-001, DAN-106
- justificativa: 
- aprofundar DAN-022: `multicast switch configuration outage root cause fix` — O resumo descreve exatamente o mesmo gatilho (tráfego multicast sem configurar switches) e o mesmo impacto (outage global), embora o contexto seja replicação de índice Solr.
  - DAN-022 (llm) [Multicast Rsync?] 0.558: ### Multicast Rsync?  If we need to get the same bits to all of the boxes, why not send the index via multicast to the replicas? It sure would be nice to only send the data once. We found an implement
  - DAN-022 (llm) [The Index Replication Issue] 0.345: ### The Index Replication Issue  To keep all of the searches on our site working fast we optimize our indexes nightly. Index optimization creates a completely new copy of the index. As we added new bo
  - DAN-022 (causa) [Search at Etsy] 0.27: ### Search at Etsy  Search at Etsy has grown significantly over the years. In January of 2009 we started using Solr for search. We used the standard primary-replica configuration for our search server
  - DAN-022 (correcao) [Improvements] 0.279: ### Improvements  To better deal with the transfer lag we are looking at creating a Torrent file per index segment. Lucene indexes are made up of various segments. Each commit creates an index segment
  - DAN-022 (correcao) [How it Works] 0.273: ### How it Works  HTTP replication doesn’t allow for the transfer of older versions of a given index. This causes issues with some of our static indexes. When we bring up new replicas, Solr creates a 

## q-055 (esperado: DAN-022)

- busca inicial: DAN-022, DAN-159, DAN-077, DAN-001, DAN-006, DAN-066, DAN-068, DAN-007, DAN-113, DAN-005
- justificativa: 
- aprofundar DAN-022: `multicast traffic unconfigured switches global outage root cause fix` — É o único incidente que envolve tráfego multicast sem configuração de switches causando queda global — corresponde exatamente ao incidente atual; os outros tratam de falhas de switch, BGP, energia e bugs de SO, sem relação com multicast.
  - DAN-022 (llm) [Multicast Rsync?] 0.568: ### Multicast Rsync?  If we need to get the same bits to all of the boxes, why not send the index via multicast to the replicas? It sure would be nice to only send the data once. We found an implement
  - DAN-022 (llm) [The Index Replication Issue] 0.357: ### The Index Replication Issue  To keep all of the searches on our site working fast we optimize our indexes nightly. Index optimization creates a completely new copy of the index. As we added new bo
  - DAN-022 (causa) [Search at Etsy] 0.27: ### Search at Etsy  Search at Etsy has grown significantly over the years. In January of 2009 we started using Solr for search. We used the standard primary-replica configuration for our search server
  - DAN-022 (correcao) [Improvements] 0.279: ### Improvements  To better deal with the transfer lag we are looking at creating a Torrent file per index segment. Lucene indexes are made up of various segments. Each commit creates an index segment
  - DAN-022 (correcao) [How it Works] 0.273: ### How it Works  HTTP replication doesn’t allow for the transfer of older versions of a given index. This causes issues with some of our static indexes. When we bring up new replicas, Solr creates a 

## q-056 (esperado: DAN-026)

- busca inicial: DAN-026, DAN-010, DAN-162, DAN-020, DAN-087, DAN-066, DAN-002, DAN-164, DAN-049, DAN-075
- justificativa: 
- aprofundar DAN-026: `authoritative nameserver restart IP change corrupt zone NXDOMAIN fix remediation` — Bate exatamente: troca de IP reiniciou só o nameserver autoritativo e um deploy durante a resposta corrompeu a zona com NXDOMAIN, igual ao incidente atual. Difere só em detalhes (Puppet, memory exhaustion).
  - DAN-026 (llm) [What happened…] 0.751: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.669: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto

## q-057 (esperado: DAN-026)

- busca inicial: DAN-026, DAN-010, DAN-020, DAN-162, DAN-087, DAN-049, DAN-075, DAN-002, DAN-103, DAN-066
- justificativa: 
- aprofundar DAN-026: `authoritative nameserver restart IP change corrupt zone NXDOMAIN deploy fix` — Mesmo cenário exato: IP change reiniciou só o authoritative DNS, causou timeouts, e o deploy durante a resposta corrompeu a zona com NXDOMAIN; difere apenas pelo memory exhaustion nos fileservers.
- aprofundar DAN-162: `database migration broke DNS resolution recovery temporary resolvers fix` — Envolve DNS quebrado e recuperação em cascata, mas o gatilho é migração de banco, não change de IP, e não menciona zona corrompida com NXDOMAIN.
- aprofundar DAN-049: `deployment DNS record failed resolve certificates DNS recreated fix` — Envolve deploy e falha de DNS, mas não tem reinicialização seletiva do authoritative nem zona corrompida com NXDOMAIN.
  - DAN-026 (llm) [What happened…] 0.75: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.682: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-162 (llm) [sem seção] 0.538: In October, we experienced one incident that resulted in degraded performance across GitHub services.  **October 11 05:59 UTC (lasting 19 hours and 12 minutes)**  On October 11, 2024, starting at 05:5
  - DAN-049 (llm) [Postmortem] 0.665: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (llm) [Resolution] 0.66: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (causa) [Root Cause of the Outage] 0.422: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [sem seção] 0.341: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat

## q-058 (esperado: DAN-033)

- busca inicial: DAN-033, DAN-106, DAN-195, DAN-032, DAN-165, DAN-154, DAN-191, DAN-231, DAN-104, DAN-048
- justificativa: 
- aprofundar DAN-033: `quota service bad config misconfiguration dependent services gmail fix` — Corresponde quase exatamente: config ruim derruba serviço de cotas e serviços dependentes incluindo Gmail; o resumo não traz causa raiz detalhada nem correção.
- aprofundar DAN-032: `autogenerated bad config Google services outage Gmail root cause fix` — Config ruim derruba vários serviços Google incluindo Gmail, padrão semelhante, mas não menciona serviço de cotas especificamente.
- aprofundar DAN-104: `human error typo S3 cascading failure dependent systems restart fix` — Erro humano provoca falha em cascata em sistemas dependentes, semelhança no efeito cascata, mas componente é S3, não cotas.
  - DAN-033 (llm) [sem seção] 0.505: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fre
  - DAN-033 (llm) [sem seção] 0.455: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  - B
  - DAN-033 (causa) [sem seção] 0.294: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  .cc
  - DAN-033 (correcao) [sem seção] 0.262: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  enu
  - DAN-033 (correcao) [sem seção] 0.248: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fie
  - DAN-032 (llm) [Today’s outage for several Google services] 0.761: # Today’s outage for several Google services  Earlier today, most Google users who use logged-in services like Gmail, Google+, Calendar and Documents found they were unable to access those services fo
  - DAN-032 (llm) [Today’s outage for several Google services] 0.693: # Today’s outage for several Google services  With services once again working normally, our work is now focused on (a) removing the source of failure that caused today’s outage, and (b) speeding up r
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.576: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.574: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.32: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object

## q-059 (esperado: DAN-033)

- busca inicial: DAN-033, DAN-032, DAN-144, DAN-036, DAN-048, DAN-029, DAN-134, DAN-218, DAN-001, DAN-154
- justificativa: 
- aprofundar DAN-033: `quota service bad config root cause fix` — O resumo menciona exatamente bad config que derruba o serviço de quota e, com ele, vários serviços incluindo Gmail, igual ao incidente atual.
- aprofundar DAN-032: `autogenerated bad config outage root cause remediation` — Bad config autogenerated derrubou vários serviços do Google incluindo Gmail; o padrão de configuração ruim causando cascata é semelhante, mas não menciona serviço de quota.
- aprofundar DAN-036: `configuration change blob lookup cascade root cause fix` — Mudança de configuração sobrecarregou componente e causou falha em cascata afetando Gmail e outros serviços; padrão de cascata parecido, mas componente é blob lookup, não quota.
  - DAN-033 (llm) [sem seção] 0.454: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fre
  - DAN-033 (llm) [sem seção] 0.398: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  enu
  - DAN-033 (causa) [sem seção] 0.294: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  .cc
  - DAN-033 (correcao) [sem seção] 0.248: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fie
  - DAN-033 (correcao) [sem seção] 0.247: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  kno
  - DAN-032 (llm) [Today’s outage for several Google services] 0.566: # Today’s outage for several Google services  With services once again working normally, our work is now focused on (a) removing the source of failure that caused today’s outage, and (b) speeding up r
  - DAN-032 (llm) [Today’s outage for several Google services] 0.553: # Today’s outage for several Google services  Earlier today, most Google users who use logged-in services like Gmail, Google+, Calendar and Documents found they were unable to access those services fo
  - DAN-036 (llm) [Google Cloud Storage Incident #19002] 0.582: # Google Cloud Storage Incident #19002  All bucket locations and storage classes were impacted. GCP services that depend on Cloud Storage were also impacted. Stackdriver Monitoring experienced up to 5
  - DAN-036 (llm) [Google Cloud Storage Incident #19002] 0.549: # Google Cloud Storage Incident #19002  The Google Cloud Platform services that experienced the most significant customer impact were the following: Google Cloud Storage experienced elevated long tail
  - DAN-036 (causa) [Google Cloud Storage Incident #19002] 0.354: # Google Cloud Storage Incident #19002  We will be improving our ability to more quickly provision resources in order to recover from a cascading failure triggered by high load. We will make software 
  - DAN-036 (correcao) [Google Cloud Storage Incident #19002] 0.4: # Google Cloud Storage Incident #19002  We will conduct an internal investigation of this issue and make appropriate improvements to our systems to help prevent or minimize future recurrence. We will 
  - DAN-036 (correcao) [Google Cloud Storage Incident #19002] 0.392: # Google Cloud Storage Incident #19002  Our Engineering team understands the root cause and is working to implement the solution. We will provide another status update by Tuesday, 2019-03-12 22:45 US/

## q-060 (esperado: DAN-042)

- busca inicial: DAN-042, DAN-035, DAN-033, DAN-032, DAN-049, DAN-017, DAN-015, DAN-029, DAN-055, DAN-129
- justificativa: 
- aprofundar DAN-042: `new config variables required by code missing deployment root cause fix` — Corresponde diretamente: código exigia novas variáveis de configuração que não foram aplicadas no deploy, exatamente o incidente atual.
- aprofundar DAN-035: `configuration rollout load balancer missing config root cause fix` — Trata de falha no rollout de configuração para componentes, similar a instâncias não receberem a variável nova, embora o componente seja um load balancer.
- aprofundar DAN-015: `new credentials deployed wrong environment missing config root cause fix` — Envolve deploy de nova configuração (credenciais) para o ambiente errado, causando falha após remoção do antigo, paralelo ao deploy sem a variável nova.
  - DAN-042 (llm) [It was such a nice morning] 0.636: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Houston, we have a problem] 0.623: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Did I mess up?] 0.334: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.745: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.735: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.36: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration
  - DAN-015 (llm) [Incident timeline] 0.653: ## Incident timeline  **All timestamps referenced are in Coordinated Universal Time (UTC).**  | Time | Event | |---|---| | Mar 21, 2025 - 19:49 UTC | The R2 engineering team started the credential rot
  - DAN-015 (llm) [Incident timeline] 0.646: ## Incident timeline  Given gradual decline in availability metrics, R2 engineering team suspected a potential regression in propagation of new credentials in storage infrastructure. | | Mar 21, 2025 
  - DAN-015 (causa) [Next steps] 0.493: ## Next steps  The list above is not exhaustive: as we work through the above items, we will likely uncover other improvements to our systems, controls, and processes that we’ll be applying to improve
  - DAN-015 (correcao) [Resolution] 0.484: ## Resolution  Once we identified the root cause, we were able to resolve the incident quickly by deploying the new credentials to the production R2 Gateway Worker. This resulted in an immediate recov
  - DAN-015 (correcao) [Next steps] 0.468: ## Next steps  This incident happened because of human error and lasted longer than it should have because we didn’t have proper visibility into which credentials were being used by the R2 Gateway Wor

## q-061 (esperado: DAN-042)

- busca inicial: DAN-042, DAN-049, DAN-050, DAN-003, DAN-035, DAN-084, DAN-129, DAN-017, DAN-116, DAN-048
- justificativa: 
- aprofundar DAN-042: `new config variables not used code required deployment fix` — O resumo descreve exatamente o mesmo padrão: código implantado exigia novas variáveis de configuração que ainda não estavam disponíveis ou não foram usadas, quebrando o serviço.
- aprofundar DAN-003: `field type change PostgreSQL schema validation rollback fix` — O deploy alterou o tipo de um campo no banco e a validação estrita falhou, sendo semelhante ao problema de incompatibilidade entre nova versão do código e o que as instâncias já possuíam.
- aprofundar DAN-050: `download URL generation bug deployment fix rollback` — O deploy continha um bug na geração de URL que quebrou downloads, compartilhando a causa de falha no serviço provocada diretamente por uma implantação defeituosa.
  - DAN-042 (llm) [It was such a nice morning] 0.676: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Did I mess up?] 0.634: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Houston, we have a problem] 0.312: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-003 (llm) [What happened] 0.535: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.44: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s
  - DAN-050 (llm) [Recovery] 0.727: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Response] 0.658: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute 
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi

## q-062 (esperado: DAN-043)

- busca inicial: DAN-043, DAN-164, DAN-209, DAN-048, DAN-056, DAN-091, DAN-186, DAN-146, DAN-210, DAN-126
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion backup recovery data loss fix` — Corresponde exatamente: delete acidental de banco gerenciado com backup diário, restauração em 30 minutos e 7 horas de dados perdidas.
- aprofundar DAN-164: `wrong directory deletion data loss recovery postmortem` — Também envolve exclusão acidental e horas de dados perdidas, mas o gatilho inclui sobrecarga e diretório errado, não um delete direto de banco gerenciado.
- aprofundar DAN-056: `accidental truncate production database environment variable fix` — Envolve perda acidental de dados de produção, mas por variável de ambiente que truncou o banco, sem backup gerenciado nem restauração rápida.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.724: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.669: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [Timeline] 0.585: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (llm) [sem seção] 0.566: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (causa) [Root cause analysis] 0.567: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.723: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.69: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-063 (esperado: DAN-043)

- busca inicial: DAN-043, DAN-164, DAN-056, DAN-186, DAN-118, DAN-048, DAN-091, DAN-066, DAN-058, DAN-146
- justificativa: 
- aprofundar DAN-043: `accidental database deletion backup recovery data loss prevention fix` — Bate quase exatamente: exclusão acidental de banco gerenciado com backup diário, restauração em 30 minutos e 7 horas de dados perdidos; difere só na empresa.
- aprofundar DAN-164: `wrong directory deletion replication lag data loss fix` — Bate em exclusão acidental com perda de horas de dados, mas não bate em backup diário; envolve sobrecarga e replicação.
- aprofundar DAN-056: `environment variable truncate production database root cause fix` — Bate em perda acidental de dados do banco de produção, mas a causa é variável de ambiente em testes, não exclusão direta.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.696: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.614: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [Timeline] 0.661: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (llm) [Root cause analysis] 0.654: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.717: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.695: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-064 (esperado: DAN-048)

- busca inicial: DAN-048, DAN-058, DAN-056, DAN-164, DAN-043, DAN-126, DAN-190, DAN-181, DAN-078, DAN-195
- justificativa: 
- aprofundar DAN-048: `RDS hardware failure MySQL misconfiguration data loss root cause fix` — Bate com o incidente atual: falha de hardware em banco gerenciado (RDS), configuração incorreta do MySQL e perda de dados em sistema financeiro; não bate se o ambiente for diferente da AWS.
  - DAN-048 (llm) [Final thoughts] 0.76: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (llm) [Incorrect configuration variable] 0.734: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m

## q-065 (esperado: DAN-048)

- busca inicial: DAN-048, DAN-058, DAN-043, DAN-056, DAN-164, DAN-181, DAN-029, DAN-146, DAN-126, DAN-066
- justificativa: 
- aprofundar DAN-048: `RDS hardware failure incorrect MySQL configuration financial data loss root cause fix` — Bate exatamente: falha de hardware em banco gerenciado (RDS), configuração MySQL incorreta e perda de dados em sistema financeiro; não há diferença relevante.
- aprofundar DAN-029: `bad config database cluster failures outage root cause fix` — Bate parcialmente: configuração ruim e falhas incomuns em cluster de banco; não bate por ausência de falha de hardware, MySQL específico e dados financeiros.
- aprofundar DAN-043: `managed database accidental deletion backups data loss recovery fix` — Bate parcialmente: banco gerenciado e perda permanente de dados; não bate por ser exclusão acidental, não falha de hardware nem exposição de configuração MySQL.
  - DAN-048 (llm) [Final thoughts] 0.76: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (llm) [Incorrect configuration variable] 0.734: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-029 (llm) [The following weeks] 0.717: ## The following weeks  The day after the incident, the whole team sat down to discuss two issues:  - Why did our Pacemaker cluster fail to elect a new primary database node? - How do we move back to 
  - DAN-029 (llm) [Reproducing the failure] 0.694: ### Reproducing the failure  To be confident in a new cluster, we needed to understand why the existing one didn't promote a new primary, and make changes to fix that issue.  For the most part, we did
  - DAN-029 (causa) [Incident timeline] 0.513: ## Incident timeline  So, how did all this go wrong?  All times in this section are in British Summer Time (UTC+1).  - 15:09: Our monitoring detects the total outage of our API and Dashboard; engineer
  - DAN-029 (correcao) [Wrapping up the incident] 0.496: ## Wrapping up the incident  With a plan in place, and the confidence that we'd understood and fixed the issue which stopped our cluster from failing over on 10 October, we were ready to go. Even with
  - DAN-029 (correcao) [What's next?] 0.486: ## What's next?  There's no getting away from the size of this incident.  We feel an immense duty to everyone who trusts GoCardless as their payments provider. We took some time to think through what 
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.649: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.637: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo

## q-066 (esperado: DAN-049)

- busca inicial: DAN-026, DAN-049, DAN-162, DAN-020, DAN-010, DAN-066, DAN-087, DAN-075, DAN-129, DAN-126
- justificativa: 
- aprofundar DAN-049: `static.crates.io DNS certificate DNS record recreation deployment root cause fix` — É praticamente o mesmo incidente: deploy de infra, domínio estático parou 10-15 min por recriação de certificados e registros DNS.
- aprofundar DAN-026: `Puppet DNS nameserver zone file corrupt NXDOMAIN deploy fix` — Também é DNS fora durante deploy, mas a causa é bug do Puppet e zona corrompida, não recriação de certificado e DNS.
  - DAN-049 (llm) [Resolution] 0.748: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (llm) [Root Cause of the Outage] 0.738: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-049 (causa) [Postmortem] 0.443: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [sem seção] 0.341: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat
  - DAN-026 (llm) [What happened…] 0.721: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.619: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto

## q-067 (esperado: DAN-049)

- busca inicial: DAN-049, DAN-026, DAN-162, DAN-020, DAN-010, DAN-210, DAN-087, DAN-086, DAN-135, DAN-129
- justificativa: 
- aprofundar DAN-049: `certificates DNS records recreated static.crates.io deploy outage root cause fix` — Corresponde quase exatamente ao incidente atual: deploy de infraestrutura, domínio de arquivos estáticos fora do ar 10–15 minutos, causado pela recriação de certificados e registros DNS.
  - DAN-049 (llm) [Resolution] 0.769: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (llm) [Root Cause of the Outage] 0.737: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-049 (causa) [Postmortem] 0.443: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [sem seção] 0.341: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat

## q-068 (esperado: DAN-050)

- busca inicial: DAN-050, DAN-016, DAN-035, DAN-129, DAN-183, DAN-137, DAN-008, DAN-106, DAN-220, DAN-001
- justificativa: 
- aprofundar DAN-050: `download URL generation bug deployment fix rollback` — Corresponde exatamente: deploy com bug na geração da URL de download, duração de 13 minutos e milhões de requisições falhas incluindo retentativas do cargo.
- aprofundar DAN-035: `configuration roll-out load balancer bug fix root cause` — Semelhança: bug introduzido por roll-out de configuração que elevou taxas de erro por minutos, mas o componente é um load balancer, não geração de URL de download.
- aprofundar DAN-008: `tiered cache change request failure fix root cause` — Semelhança: mudança de produção causou falhas nas requisições, mas sem bug de geração de URL e sem a duração curta de 13 minutos.
  - DAN-050 (llm) [Recovery] 0.727: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Response] 0.658: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute 
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.761: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.746: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.36: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration
  - DAN-008 (llm) [sem seção] 0.763: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.692: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac

## q-069 (esperado: DAN-050)

- busca inicial: DAN-050, DAN-129, DAN-008, DAN-220, DAN-001, DAN-183, DAN-216, DAN-154, DAN-017, DAN-103
- justificativa: 
- aprofundar DAN-050: `download URL generation bug deployment fix root cause` — O incidente atual é praticamente idêntico: deploy com bug na geração de URL de download, falha em downloads de pacotes e milhões de requisições falhas com retentativas, enquanto DAN-050 descreve exatamente esse cenário no crates.io.
  - DAN-050 (llm) [Recovery] 0.663: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Root cause identification: The Five Whys] 0.639: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (causa) [Response] 0.457: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute 
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi

## q-070 (esperado: DAN-058)

- busca inicial: DAN-058, DAN-126, DAN-048, DAN-234, DAN-006, DAN-043, DAN-084, DAN-164, DAN-231, DAN-191
- justificativa: 
- aprofundar DAN-058: `backup identifier misconfiguration data leak fix data loss root cause` — Corresponde exatamente: identificadores de backup errados em bancos gratuitos causaram vazamento entre clientes e a correção causou perda de dados.
- aprofundar DAN-126: `bug fix data loss server misconfiguration hotfix root cause` — Semelha na correção causando perda de dados, mas contexto é Destiny 2 e timestamps incorretos, não identificadores de backup de banco.
  - DAN-058 (llm) [What happened?] 0.753: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.673: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-126 (llm) [Server Configurations] 0.653: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [Server Configurations] 0.627: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (causa) [Server Configurations] 0.378: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (correcao) [sem seção] 0.436: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’

## q-071 (esperado: DAN-058)

- busca inicial: DAN-058, DAN-126, DAN-048, DAN-164, DAN-056, DAN-043, DAN-234, DAN-186, DAN-155, DAN-118
- justificativa: 
- aprofundar DAN-058: `backup identifier misconfiguration data leak free tier fix data loss` — O resumo descreve exatamente o mesmo cenário do incidente atual: identificadores de backup incorretos em bancos de free tier, vazamento de dados entre clientes e perda de dados causada pela correção subsequente.
  - DAN-058 (llm) [What happened?] 0.787: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.737: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n

## q-072 (esperado: DAN-059)

- busca inicial: DAN-007, DAN-059, DAN-006, DAN-019, DAN-005, DAN-022, DAN-159, DAN-023, DAN-013, DAN-068
- justificativa: 
- aprofundar DAN-059: `BGP config error transit providers Level 3 Telia Zayo global outage` — Bate: configuração BGP errada cortou múltiplos provedores de trânsito e causou pane global, igual ao incidente atual. Não bate: resumo indica que não há post-mortem oficial.
- aprofundar DAN-007: `BGP advertised prefixes ordering malfunction datacenters root cause fix` — Bate: falha de configuração BGP envolvendo prefixos anunciados afetou vários datacenters. Não bate: trata-se de ordem incorreta de prefixos desabilitados, não de corte de conexão com provedores de trânsito.
- aprofundar DAN-023: `backbone router configuration BGP routes withdrawn global outage fix` — Bate: mudanças de configuração em roteadores de backbone causaram pane global de todos os serviços. Não bate: foco em rotas BGP retiradas, não especificamente em provedores de trânsito externos.
  - DAN-059 (llm) [Only Some Roads Lead to Seattle] 0.556: ### Only Some Roads Lead to Seattle  When traffic from some networks completely terminates, while traffic from others is properly delivered, its usually a physical network failure (broken link or rout
  - DAN-059 (llm) [Troubles in the Data Center] 0.449: ### Troubles in the Data Center  So we have a situation with high levels of packet loss from many locations around the world. Let’s take a look at a Path Visualization to see where the network instabi
  - DAN-059 (causa) [sem seção] 0.384: Data centers are the factories of the Internet, churning out computation and services that customers demand. Apple is currently converting a 1.3M sq ft factory into a data center. And like factories, 
  - DAN-059 (correcao) [A (Nearly) Global Outage] 0.255: ### A (Nearly) Global Outage  We were monitoring the Steam API at the time of the outage. You can follow the interactive data here. The first thing we noticed was a dramatic drop in API availability, 
  - DAN-059 (correcao) [Steam Outage on May 7th] 0.254: ### Steam Outage on May 7th  Starting at 11:45 Pacific on May 7th and lasting for 2 hours, the popular online gaming service Steam suffered a widespread outage. Steam regularly has more than 8 million
  - DAN-007 (llm) [Incident timeline and impact] 0.703: ### Incident timeline and impact  In order to be reachable on the Internet, networks like Cloudflare make use of a protocol called BGP. As part of this protocol, operators define policies which decide
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.675: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We
  - DAN-023 (llm) [sem seção] 0.626: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.563: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da

## q-073 (esperado: DAN-059)

- busca inicial: DAN-007, DAN-059, DAN-006, DAN-019, DAN-023, DAN-013, DAN-005, DAN-022, DAN-159, DAN-205
- justificativa: 
- aprofundar DAN-059: `bad BGP config severed transit providers global outage root cause fix` — Bate por envolver configuração BGP ruim que cortou provedores de trânsito e causou pane global; não bate por ser da Valve/Steam e não ter post-mortem oficial.
- aprofundar DAN-023: `backbone router configuration changes global outage BGP root cause fix` — Bate por alterações de configuração em roteadores backbone causarem pane global; não bate por ser do Facebook e focar em roteadores backbone internos.
- aprofundar DAN-007: `incorrect ordering disabled BGP advertised prefixes root cause fix` — Bate por envolver ordem incorreta de prefixos BGP anunciados afetando vários datacenters; não bate por ser sobre ordenação de prefixos desabilitados, não provedores de trânsito.
  - DAN-059 (llm) [Only Some Roads Lead to Seattle] 0.631: ### Only Some Roads Lead to Seattle  When traffic from some networks completely terminates, while traffic from others is properly delivered, its usually a physical network failure (broken link or rout
  - DAN-059 (llm) [Troubles in the Data Center] 0.471: ### Troubles in the Data Center  So we have a situation with high levels of packet loss from many locations around the world. Let’s take a look at a Path Visualization to see where the network instabi
  - DAN-059 (causa) [sem seção] 0.384: Data centers are the factories of the Internet, churning out computation and services that customers demand. Apple is currently converting a 1.3M sq ft factory into a data center. And like factories, 
  - DAN-059 (correcao) [A (Nearly) Global Outage] 0.255: ### A (Nearly) Global Outage  We were monitoring the Steam API at the time of the outage. You can follow the interactive data here. The first thing we noticed was a dramatic drop in API availability, 
  - DAN-059 (correcao) [Steam Outage on May 7th] 0.254: ### Steam Outage on May 7th  Starting at 11:45 Pacific on May 7th and lasting for 2 hours, the popular online gaming service Steam suffered a widespread outage. Steam regularly has more than 8 million
  - DAN-023 (llm) [sem seção] 0.626: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.556: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da
  - DAN-007 (llm) [Incident timeline and impact] 0.678: ### Incident timeline and impact  In order to be reachable on the Internet, networks like Cloudflare make use of a protocol called BGP. As part of this protocol, operators define policies which decide
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.662: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We

## q-074 (esperado: DAN-060)

- busca inicial: DAN-060, DAN-063, DAN-069, DAN-068, DAN-067, DAN-191, DAN-062, DAN-064, DAN-061, DAN-209
- justificativa: 
- aprofundar DAN-060: `transformer failure PLC phase check backup generators root cause fix` — O resumo menciona transformador com falha e PLC que confere fase dos geradores impedindo geradores de reserva, igual ao incidente atual, afetando EC2, EBS e RDS.
- aprofundar DAN-063: `generator breaker mechanical failure power control malfunction root cause fix` — É um evento de perda de energia em região da Amazon com falha de geradores e mau funcionamento do sistema automatizado de controle de energia, mas envolve disjuntor e rota inválida que não estão no atual.
- aprofundar DAN-062: `power loss backup generators breakers engage root cause recovery fix` — É uma perda de energia em região da Amazon com reservas de backup e disjuntores, mas causada por clima severo e sem menção ao controlador de fase.
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.538: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  Normally, when utility power fails, electrical load is seamlessly picked up by backup generators. Program
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.459: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  By Sunday morning, August 7th, we had completed the work to fully understand root cause, prevent the prob
  - DAN-060 (causa) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.442: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  In one of the days leading up to the Friday, August 5th deletion run, there was a hardware failure that t
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.417: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  We learned a number of lessons from this event that we will use to continually improve the reliability of
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.39: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  There are several places we can improve on the communication front. First, we can accelerate the pace wit
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.603: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.476: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.593: ### Summary of the AWS Service Event in the Sydney Region  If utility power is interrupted, the DRUPS uses this stored energy to continue to provide power to the datacenter while the integrated genera
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.518: ### Summary of the AWS Service Event in the Sydney Region  We’d like to share more detail about the AWS service disruption that occurred this past weekend in the AWS Sydney Region. The service disrupt
  - DAN-062 (causa) [Summary of the AWS Service Event in the Sydney Region] 0.399: ### Summary of the AWS Service Event in the Sydney Region  A latent bug in our instance management software led to a slower than expected recovery of the remaining instances. The team worked over the 
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.388: ### Summary of the AWS Service Event in the Sydney Region  Additionally, we will be taking actions to improve our recovery systems. The first is to fix the latent issue that led to our recovery system
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.359: ### Summary of the AWS Service Event in the Sydney Region  During the initial part of this event, customers experienced errors when trying to launch new instances, or when trying to scale their auto-s

## q-075 (esperado: DAN-060)

- busca inicial: DAN-060, DAN-063, DAN-068, DAN-061, DAN-067, DAN-064, DAN-062, DAN-191, DAN-069, DAN-209
- justificativa: 
- aprofundar DAN-060: `transformer failure PLC generator phase backup generators root cause fix` — O resumo é quase idêntico ao incidente atual: transformer falhou, o controlador/PLC que verifica a fase da energia do gerador falhou, os geradores de backup não entraram online e EC2/EBS/RDS na região caíram; não há diferença aparente na descrição de alto nível.
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.531: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  Normally, when utility power fails, electrical load is seamlessly picked up by backup generators. Program
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.457: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  By Sunday morning, August 7th, we had completed the work to fully understand root cause, prevent the prob
  - DAN-060 (causa) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.442: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  In one of the days leading up to the Friday, August 5th deletion run, there was a hardware failure that t
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.417: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  We learned a number of lessons from this event that we will use to continually improve the reliability of
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.39: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  There are several places we can improve on the communication front. First, we can accelerate the pace wit

## q-076 (esperado: DAN-065)

- busca inicial: DAN-065, DAN-006, DAN-113, DAN-022, DAN-106, DAN-159, DAN-068, DAN-231, DAN-007, DAN-048
- justificativa: 
- aprofundar DAN-065: `malfunctioning IMP corrupted routing data checksums recomputed bad data nodes off network` — Bate exatamente: nó com defeito corrompe dados de roteamento, software recalcula checksums e propaga dados ruins como válidos, e nós saem da rede; difere apenas por ser da ARPANET de 1980.
  - DAN-065 (llm) [sem seção] 0.745: our own building (after taking dumps, of course).  This procedure initializes  all  of  the IMPs' dynamic data structures, and will                               - 2 - RFC 789                         
  - DAN-065 (llm) [sem seção] 0.702: require  either  a  large  number  of  CPU  cycles  (for frequent checksumming of a large area of memory)  or  a  large  amount  of memory  (to store the checksums for a lot of small areas).  Since CP
  - DAN-065 (causa) [sem seção] 0.485: ```                                                           RFC 789     Vulnerabilities of Network Control Protocols: An Example                           Eric C. Rosen                   Bolt Berane
  - DAN-065 (correcao) [sem seção] 0.395: loader/dumper.  In the case under discussion, we would have liked to  have  all  the  IMPs  go  into  their loader/dumpers when the problem arose.  This would have enabled us to  re-initialize  and re
  - DAN-065 (correcao) [sem seção] 0.389: possible  for so  many updates from one IMP to be extant simultaneously, we did understand enough to be able to get the network to recover.   All that was necessary was to patch the IMPs to disregard 

## q-077 (esperado: DAN-065)

- busca inicial: DAN-065, DAN-006, DAN-113, DAN-109, DAN-238, DAN-022, DAN-159, DAN-143, DAN-026, DAN-106
- justificativa: 
- aprofundar DAN-065: `IMP corrupted routing data checksums recomputed bad data fix recovery` — O resumo descreve exatamente o mesmo cenário: nó com falha corrompe dados de roteamento, software recomputa checksums e espalha dados ruins como válidos, fazendo nós saírem da rede.
- aprofundar DAN-109: `network disruption metadata load timeout storage nodes take themselves down fix` — Também envolve nós que se retiram da rede, embora a causa seja carga e timeout, não corrupção de dados de roteamento com checksums.
  - DAN-065 (llm) [sem seção] 0.696: our own building (after taking dumps, of course).  This procedure initializes  all  of  the IMPs' dynamic data structures, and will                               - 2 - RFC 789                         
  - DAN-065 (llm) [sem seção] 0.677: require  either  a  large  number  of  CPU  cycles  (for frequent checksumming of a large area of memory)  or  a  large  amount  of memory  (to store the checksums for a lot of small areas).  Since CP
  - DAN-065 (causa) [sem seção] 0.485: ```                                                           RFC 789     Vulnerabilities of Network Control Protocols: An Example                           Eric C. Rosen                   Bolt Berane
  - DAN-065 (correcao) [sem seção] 0.395: loader/dumper.  In the case under discussion, we would have liked to  have  all  the  IMPs  go  into  their loader/dumpers when the problem arose.  This would have enabled us to  re-initialize  and re
  - DAN-065 (correcao) [sem seção] 0.389: possible  for so  many updates from one IMP to be extant simultaneously, we did understand enough to be able to get the network to recover.   All that was necessary was to patch the IMPs to disregard 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.634: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.588: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-078 (esperado: DAN-069)

- busca inicial: DAN-069, DAN-068, DAN-063, DAN-191, DAN-205, DAN-209, DAN-106, DAN-067, DAN-060, DAN-154
- justificativa: 
- aprofundar DAN-069: `alarm bug transmission lines foliage cascading failure root cause fix` — É o único incidente que corresponde exatamente ao atual: linhas de transmissão atingiram folhagem, o alarme da sala de controle não disparou por bug, os operadores não redistribuíram a carga, houve falha em cascata e dezenas de milhões ficaram sem energia. Não há diferença relevante.
  - DAN-069 (llm) [Cascade] 0.587: ## Cascade  ## Timeline  The following is the blackout's sequence of events on August 14, 2003 (times in EDT):  - 12:15 p.m. Incorrect telemetry data renders the state estimator, a power flow monitori
  - DAN-069 (llm) [Computer failure] 0.553: ## Computer failure  A software bug known as a race condition existed in General Electric Energy's Unix-based XA/21 energy management system. Once triggered, the bug stalled FirstEnergy's control room
  - DAN-069 (causa) [Findings] 0.529: ## Findings  In April 2004, the U.S.-Canada Power System Outage Task Force released their final report, placing the causes of the blackout into four groups:  - FirstEnergy (FE) and its reliability cou
  - DAN-069 (correcao) [Restoration of service] 0.437: ## Restoration of service  Preparations against the possible disruptions threatened by the Year 2000 problem have been credited for the installation of new electrical equipment and systems which allow
  - DAN-069 (correcao) [Investigation efforts] 0.397: ## Investigation efforts  A joint federal task force was formed by the governments of Canada and the U.S. to oversee the investigation and report directly to Ottawa and Washington. The task force was 

## q-079 (esperado: DAN-069)

- busca inicial: DAN-069, DAN-068, DAN-191, DAN-063, DAN-067, DAN-205, DAN-064, DAN-209, DAN-106, DAN-060
- justificativa: 
- aprofundar DAN-069: `alarm bug transmission lines foliage cascading failure fix` — O que bate: linhas atingiram vegetação, bug impediu alarme, operadores não redistribuíram carga, cascata afetou milhões; o que não bate: nada relevante.
- aprofundar DAN-063: `automated power control system malfunction generator overload fix` — O que bate: sistema automatizado de controle falhou e operadores atuaram manualmente com cascata de geradores; o que não bate: não envolve linhas de transmissão ou árvores.
- aprofundar DAN-068: `breaker coordination cascade safety breakers power loss fix` — O que bate: falha em coordenação de proteção causou perda total em cascata; o que não bate: não envolve árvores, alarme de sala de controle ou bug de alarme.
  - DAN-069 (llm) [Cascade] 0.585: ## Cascade  ## Timeline  The following is the blackout's sequence of events on August 14, 2003 (times in EDT):  - 12:15 p.m. Incorrect telemetry data renders the state estimator, a power flow monitori
  - DAN-069 (llm) [Computer failure] 0.562: ## Computer failure  A software bug known as a race condition existed in General Electric Energy's Unix-based XA/21 energy management system. Once triggered, the bug stalled FirstEnergy's control room
  - DAN-069 (causa) [Findings] 0.529: ## Findings  In April 2004, the U.S.-Canada Power System Outage Task Force released their final report, placing the causes of the blackout into four groups:  - FirstEnergy (FE) and its reliability cou
  - DAN-069 (correcao) [Restoration of service] 0.437: ## Restoration of service  Preparations against the possible disruptions threatened by the Year 2000 problem have been credited for the installation of new electrical equipment and systems which allow
  - DAN-069 (correcao) [Investigation efforts] 0.397: ## Investigation efforts  A joint federal task force was formed by the governments of Canada and the U.S. to oversee the investigation and report directly to Ottawa and Washington. The task force was 
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.645: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.524: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-068 (llm) [What happened to the power in the data center?] 0.657: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.546: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is

## q-080 (esperado: DAN-073)

- busca inicial: DAN-073, DAN-048, DAN-164, DAN-209, DAN-109, DAN-043, DAN-222, DAN-226, DAN-071, DAN-067
- justificativa: 
- aprofundar DAN-073: `storage volume failure root cause fix remediation` — Bate exatamente: falha de volume de storage em um servidor de armazenamento que derrubou o site e programas/sites de usuários dependentes desse volume, mesma descrição do incidente atual. Não há diferença relevante no cenário descrito.
  - DAN-073 (llm) [Next steps¶] 0.688: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (llm) [17:04¶] 0.671: #### 17:04¶  By this point we had become sure that the system was getting blocked on storage IO, but the problem did not seem to be the machine itself like the original indications had suggested. Howe
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi

## q-081 (esperado: DAN-073)

- busca inicial: DAN-073, DAN-109, DAN-191, DAN-048, DAN-067, DAN-209, DAN-164, DAN-106, DAN-139, DAN-208
- justificativa: 
- aprofundar DAN-073: `storage volume failure root cause remediation fix` — O resumo é praticamente idêntico ao incidente atual: falha de volume de storage em um storage server que derruba o site e programas/sites dependentes.
  - DAN-073 (llm) [Next steps¶] 0.685: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (llm) [17:04¶] 0.656: #### 17:04¶  By this point we had become sure that the system was getting blocked on storage IO, but the problem did not seem to be the machine itself like the original indications had suggested. Howe
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi

## q-082 (esperado: DAN-076)

- busca inicial: DAN-076, DAN-103, DAN-146, DAN-189, DAN-200, DAN-084, DAN-058, DAN-198, DAN-126, DAN-142
- justificativa: 
- aprofundar DAN-076: `typo name conflict installer delete boot.ini expansion fix root cause` — Corresponde exatamente: erro de digitação, conflito de nomes, instalador de expansão e arquivo boot.ini apagado. Não há outro incidente com esse componente e gatilho.
  - DAN-076 (llm) [About the boot.ini issue] 0.705: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.691: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (causa) [About the boot.ini issue] 0.344: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 
  - DAN-076 (correcao) [About the boot.ini issue] 0.317: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h

## q-083 (esperado: DAN-076)

- busca inicial: DAN-076, DAN-142, DAN-146, DAN-189, DAN-173, DAN-058, DAN-126, DAN-103, DAN-013, DAN-116
- justificativa: 
- aprofundar DAN-076: `typo name conflict installer deleted boot.ini root cause fix` — Corresponde exatamente ao incidente atual: instalador de expansão de jogo, erro de digitação e conflito de nome que apagam um arquivo de inicialização do sistema operacional.
  - DAN-076 (llm) [About the boot.ini issue] 0.708: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.707: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (causa) [About the boot.ini issue] 0.344: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 
  - DAN-076 (correcao) [About the boot.ini issue] 0.317: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h

## q-084 (esperado: DAN-083)

- busca inicial: DAN-083, DAN-195, DAN-190, DAN-048, DAN-164, DAN-102, DAN-092, DAN-003, DAN-066, DAN-058
- justificativa: 
- aprofundar DAN-083: `Postgres nextval sequence cache 32 WAL promotion jump fix` — Corresponde exatamente: pós-upgrade HA do Postgres, réplica promovida a primária, salto de exatamente 32 em IDs sequenciais.
  - DAN-083 (llm) [sem seção] 0.713: ``` /*  * We don't want to log each fetching of a value from a sequence,  * so we pre-log a few fetches in advance. In the event of  * crash we can lose (skip over) as many values as we pre-logged.  *
  - DAN-083 (llm) [sem seção] 0.594: As part of this promotion, the follower (which in many cases had a sequence value up to 32 ahead) became the new primary, at which point all sequences essentially jumped 32 values forward.  Something 
  - DAN-083 (causa) [sem seção] 0.401: 1. We go to great lengths to ensure that if someone asks us to create an incident, we do so (!). We hadn't seen any issues and had no reports from customers, either. 2. For failed incident creation to
  - DAN-083 (correcao) [See related articles] 0.426: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-083 (correcao) [sem seção] 0.318: The other day, we started getting strange reports from some customers of incident.io.  Their incident identifiers — unique numbers to identify each incident — appeared to have jumped unexpectedly. One

## q-085 (esperado: DAN-083)

- busca inicial: DAN-083, DAN-195, DAN-190, DAN-188, DAN-048, DAN-102, DAN-092, DAN-003, DAN-164, DAN-080
- justificativa: 
- aprofundar DAN-083: `postgres nextval sequence jump 32 replica promoted primary WAL pre-allocation fix` — Este incidente é virtualmente idêntico ao atual: atualização HA do Postgres, promoção de réplica para primário e salto de IDs sequenciais em exatamente 32, com causa e correção descritas.
  - DAN-083 (llm) [sem seção] 0.773: ``` /*  * We don't want to log each fetching of a value from a sequence,  * so we pre-log a few fetches in advance. In the event of  * crash we can lose (skip over) as many values as we pre-logged.  *
  - DAN-083 (llm) [sem seção] 0.602: As part of this promotion, the follower (which in many cases had a sequence value up to 32 ahead) became the new primary, at which point all sequences essentially jumped 32 values forward.  Something 
  - DAN-083 (causa) [sem seção] 0.401: 1. We go to great lengths to ensure that if someone asks us to create an incident, we do so (!). We hadn't seen any issues and had no reports from customers, either. 2. For failed incident creation to
  - DAN-083 (correcao) [See related articles] 0.426: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-083 (correcao) [sem seção] 0.318: The other day, we started getting strange reports from some customers of incident.io.  Their incident identifiers — unique numbers to identify each incident — appeared to have jumped unexpectedly. One

## q-086 (esperado: DAN-085)

- busca inicial: DAN-085, DAN-084, DAN-164, DAN-050, DAN-130, DAN-173, DAN-078, DAN-157, DAN-219, DAN-097
- justificativa: 
- aprofundar DAN-085: `SHA1 collision Subversion repository dedup checkout consistency fix remediation` — Bate exatamente: repositório indisponível por dois arquivos com mesmo SHA-1, checkout falha na consistência. Não bate apenas se o VCS atual for Git e não Subversion.
  - DAN-085 (llm) [Problem Statement] 0.815: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options] 0.8: # Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options  You probably saw the news last week that researchers at Google had found a scenario where they were able to break th
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-087 (esperado: DAN-085)

- busca inicial: DAN-085, DAN-078, DAN-077, DAN-084, DAN-219, DAN-173, DAN-157, DAN-050, DAN-190, DAN-130
- justificativa: 
- aprofundar DAN-085: `SHA-1 collision deduplication repository checkout consistency check remediation prevention` — É exatamente o mesmo cenário: repositório de código indisponível após commit de dois arquivos com mesmo SHA-1, falha na consistência do checkout, com deduplicação envolvida.
  - DAN-085 (llm) [Problem Statement] 0.748: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options] 0.738: # Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options  You probably saw the news last week that researchers at Google had found a scenario where they were able to break th
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-088 (esperado: DAN-086)

- busca inicial: DAN-086, DAN-090, DAN-154, DAN-009, DAN-120, DAN-221, DAN-210, DAN-126, DAN-066, DAN-029
- justificativa: 
- aprofundar DAN-086: `leap year certificate expiration date calculation one year fix` — É o único incidente que corresponde exatamente: ano bissexto, certificados de um ano, código soma um ano à data atual, expiração inválida em 29/02/2013 e interrupção de quase um dia; difere apenas na plataforma (Azure).
  - DAN-086 (llm) [The Leap Day Bug] 0.59: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.471: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-089 (esperado: DAN-086)

- busca inicial: DAN-086, DAN-090, DAN-087, DAN-154, DAN-195, DAN-216, DAN-066, DAN-129, DAN-016, DAN-189
- justificativa: 
- aprofundar DAN-086: `leap year certificate expiration date root cause fix` — Mesmo cenário: código somou um ano na data atual em ano bissexto, gerou certificado expirando em 29/02/2013 (data inválida), certificados rejeitados e plataforma fora por quase um dia — idêntico ao incidente atual.
  - DAN-086 (llm) [The Leap Day Bug] 0.613: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.534: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-090 (esperado: DAN-088)

- busca inicial: DAN-088, DAN-089, DAN-116, DAN-087, DAN-216, DAN-181, DAN-200, DAN-144, DAN-127, DAN-188
- justificativa: 
- aprofundar DAN-088: `leap second printk xtime_lock deadlock kernel fix` — Mesmo gatilho (leap second), mesmo componente (kernel Linux) e mesma falha: código do leap second grava log e espera pelo mesmo lock, causando deadlock.
- aprofundar DAN-089: `leap second CLOCK_REALTIME hrtimer fix patch` — Mesmo gatilho e componente (leap second no kernel Linux), embora a falha seja timers/futex e não deadlock por log.
- aprofundar DAN-087: `leap second Cloudflare DNS panic monotonic time fix` — Mesmo gatilho (leap second), mas componente diferente (DNS em userspace/Go) e falha diferente (pânico por tempo negativo).
  - DAN-088 (llm) [sem seção] 0.829: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.793: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.785: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.724: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.239: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-087 (llm) [sem seção] 0.784: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (llm) [Timeline] 0.767: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is
  - DAN-087 (causa) [A little bit about Cloudflare DNS] 0.331: ### A little bit about Cloudflare DNS  Cloudflare customers use our DNS service to serve the authoritative answers for DNS queries for their domains. They need to tell us the IP address of their origi
  - DAN-087 (correcao) [The one character fix] 0.332: ### The one character fix  One precaution when using a non-monotonic clock source is to always check whether the difference between two timestamps is negative. Should this happen, it’s not possible to
  - DAN-087 (correcao) [A falsehood programmers believe about time] 0.251: ### A falsehood programmers believe about time  The root cause of the bug that affected our DNS service was the belief that *time cannot go backwards*. In our case, some code assumed that the *differe

## q-091 (esperado: DAN-088)

- busca inicial: DAN-088, DAN-116, DAN-181, DAN-089, DAN-226, DAN-188, DAN-127, DAN-129, DAN-103, DAN-180
- justificativa: 
- aprofundar DAN-088: `leap second printk xtime_lock deadlock fix` — Descreve exatamente deadlock no kernel durante leap second causado por printk enquanto xtime_lock está segurado, igual ao incidente atual.
- aprofundar DAN-089: `leap second CLOCK_REALTIME hrtimer offset fix` — Também envolve leap second no kernel, mas o mecanismo é rewind de timer/futex, não deadlock por log.
  - DAN-088 (llm) [sem seção] 0.801: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.761: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.778: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.701: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.239: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti

## q-092 (esperado: DAN-092)

- busca inicial: DAN-092, DAN-164, DAN-080, DAN-186, DAN-133, DAN-195, DAN-066, DAN-221, DAN-209, DAN-134
- justificativa: 
- aprofundar DAN-092: `stale statistics planner disk reads ANALYZE rollback blue green database` — Mesmo cenário: blue/green no banco de workflows, estatísticas do planejador desatualizadas após a migração, consultas lendo do disco, latência alta e retorno ao banco antigo (blue). Diferente apenas nos detalhes da plataforma.
  - DAN-092 (llm) [What Happened] 0.666: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.613: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers

## q-093 (esperado: DAN-092)

- busca inicial: DAN-092, DAN-164, DAN-080, DAN-190, DAN-133, DAN-096, DAN-101, DAN-130, DAN-186, DAN-102
- justificativa: 
- aprofundar DAN-092: `stale planner statistics ANALYZE blue green upgrade rollback old database fix` — É o único incidente que descreve exatamente o mesmo cenário: upgrade blue/green do banco de workflows, estatísticas do planner desatualizadas após upgrade de versão major, queries indo para disco, latência disparando e re‑promoção do banco antigo (blue) para recuperar. Não há diferença relevante no resumo.
  - DAN-092 (llm) [What Happened] 0.667: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.646: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers

## q-094 (esperado: DAN-093)

- busca inicial: DAN-093, DAN-078, DAN-048, DAN-094, DAN-066, DAN-190, DAN-164, DAN-145, DAN-079, DAN-029
- justificativa: 
- aprofundar DAN-093: `schema migration load replication manager failover cold buffer pool pacemaker segfault partition stale master election data drift fix` — O incidente atual é praticamente o mesmo cenário: migração de schema gerou carga, failover do gerenciador de replicação, partição no cluster e primário desatualizado eleito, causando divergência de dados por alguns minutos.
  - DAN-093 (llm) [Monday, September 10th] 0.655: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.631: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member

## q-095 (esperado: DAN-093)

- busca inicial: DAN-093, DAN-078, DAN-048, DAN-164, DAN-190, DAN-066, DAN-029, DAN-234, DAN-099, DAN-194
- justificativa: 
- aprofundar DAN-093: `schema migration replication manager failover Pacemaker partition stale primary data drift fix` — Mesmo padrão exato: schema migration gera load, failover do MySQL primary, partition no cluster, eleição de primary stale e data drift por minutos; é o mais parecido com o incidente atual.
- aprofundar DAN-099: `schema migration MySQL semaphore deadlock replica crash recovery fix` — Também envolve schema migration pesada no MySQL afetando replicas, mas sem failover nem eleição de primary stale, então o desfecho difere do incidente atual.
- aprofundar DAN-078: `network partition MySQL failover new master missing writes latency fix` — Envolve failover e partition do MySQL, mas o gatilho é uma network partition durante maintenance, não uma schema migration, então é menos parecido.
  - DAN-093 (llm) [Tuesday, September 11th] 0.655: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (llm) [Monday, September 10th] 0.653: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member
  - DAN-099 (llm) [sem seção] 0.645: In November, we experienced one incident resulting in significant impact and degraded state of availability for core GitHub services, including GitHub Actions, API Requests, Codespaces, Git Operations
  - DAN-099 (llm) [sem seção] 0.571: Throughout the incident, write operations remained healthy and we have verified there was no data corruption.  To address this class of failure and reduce time to recover in the future, we continue to
  - DAN-078 (llm) [Incident timeline] 0.677: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [2018 October 22 11:12 UTC] 0.626: ## 2018 October 22 11:12 UTC  All database primaries established in US East Coast again. This resulted in the site becoming far more responsive as writes were now directed to a database server that wa
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa

## q-096 (esperado: DAN-106)

- busca inicial: DAN-106, DAN-048, DAN-191, DAN-104, DAN-209, DAN-006, DAN-073, DAN-164, DAN-126, DAN-154
- justificativa: 
- aprofundar DAN-106: `human error routine networking upgrade resource crunch software bugs volume loss outage fix` — O resumo é praticamente idêntico ao incidente atual: erro humano em atualização de rede de rotina, falta de recursos, bugs agravando, outage regional e perda de volumes.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.477: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.461: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  The team faced two challenges which delayed getting capacity online. First, when a node fails, the EBS cluster do
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.353: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di

## q-097 (esperado: DAN-106)

- busca inicial: DAN-106, DAN-104, DAN-209, DAN-073, DAN-109, DAN-048, DAN-191, DAN-164, DAN-006, DAN-189
- justificativa: 
- aprofundar DAN-106: `human error network upgrade storage resource crunch software bug volume loss root cause fix` — O resumo descreve exatamente o mesmo cenário do incidente atual: erro humano durante upgrade de rede, crunch de recursos de armazenamento agravado por bugs, queda de toda a região e pequena fração de volumes perdida.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.5: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  When this network connectivity issue occurred, a large number of EBS nodes in a single EBS cluster lost connectio
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.499: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  The team faced two challenges which delayed getting capacity online. First, when a node fails, the EBS cluster do
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 

## q-098 (esperado: DAN-116)

- busca inicial: DAN-116, DAN-126, DAN-154, DAN-103, DAN-144, DAN-209, DAN-066, DAN-173, DAN-129, DAN-106
- justificativa: 
- aprofundar DAN-116: `double free root cause fix database update servers crash staging delay` — O resumo descreve exatamente o mesmo padrão: double free revelado por atualização de banco de dados, queda simultânea de todos os servidores e não detecção no staging por exigir atraso de tempo para disparar o bug.
  - DAN-116 (llm) [sem seção] 0.686: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.678: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b

## q-099 (esperado: DAN-116)

- busca inicial: DAN-116, DAN-126, DAN-103, DAN-154, DAN-066, DAN-142, DAN-209, DAN-129, DAN-208, DAN-217
- justificativa: 
- aprofundar DAN-116: `double free database update delay staging root cause fix` — O resumo menciona double free causado por atualização de banco de dados, queda simultânea de todos os servidores e passagem pelo staging devido a atraso necessário, correspondendo exatamente ao incidente atual.
  - DAN-116 (llm) [sem seção] 0.729: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.638: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b

## q-100 (esperado: DAN-118)

- busca inicial: DAN-067, DAN-209, DAN-148, DAN-118, DAN-066, DAN-109, DAN-221, DAN-217, DAN-238, DAN-220
- justificativa: 
- aprofundar DAN-118: `root cause fix customer product access outage restoration two weeks` — O único incidente com centenas de clientes sem acesso a produtos e restauração em até duas semanas (14 dias), exatamente como o atual.
  - DAN-118 (llm) [Executive summary] 0.631: ## Executive summary  On Tuesday, April 5th, 2022, starting at 7:38 UTC, 775 Atlassian customers lost access to their Atlassian products. The outage spanned up to 14 days for a subset of these custome
  - DAN-118 (llm) [What happened] 0.62: ### What happened  On April 12th, Atlassian published an update from CTO, Sri Viswanath, providing more technical details of what happened, who was affected, whether there was data loss, our progress 
  - DAN-118 (causa) [How will we improve?] 0.465: ## How will we improve?  We have immediately blocked bulk sites deletes until appropriate changes can be made.  As we move forward from this incident and re-evaluate our internal processes, we want to
  - DAN-118 (correcao) [Workstream 3: Accelerated recovery and the Restoration 2 approach] 0.479: #### Workstream 3: Accelerated recovery and the Restoration 2 approach  **Timestamp: Days 4 – 13 (April 9th – 17th)**  With the Restoration 1 approach, it would have taken us three weeks to restore al
  - DAN-118 (correcao) [Learning 4: Improve our communications processes] 0.473: ### Learning 4: Improve our communications processes  **a) We deleted critical customer identifiers, impacting communications and actions to those affected**  The same script which deleted customer si

## q-101 (esperado: DAN-118)

- busca inicial: DAN-209, DAN-067, DAN-148, DAN-118, DAN-066, DAN-154, DAN-026, DAN-109, DAN-221, DAN-217
- justificativa: 
- aprofundar DAN-118: `customer access loss root cause fix two weeks restoration` — Mesma perda massiva de acesso a produtos e restauração que levou até duas semanas para parte dos clientes, como no incidente atual.
  - DAN-118 (llm) [Executive summary] 0.641: ## Executive summary  On Tuesday, April 5th, 2022, starting at 7:38 UTC, 775 Atlassian customers lost access to their Atlassian products. The outage spanned up to 14 days for a subset of these custome
  - DAN-118 (llm) [Executive summary] 0.612: ## Executive summary  At the start of the incident, we knew exactly which sites were affected and our priority was to establish communication with the approved owner for each impacted site to inform t
  - DAN-118 (causa) [How will we improve?] 0.465: ## How will we improve?  We have immediately blocked bulk sites deletes until appropriate changes can be made.  As we move forward from this incident and re-evaluate our internal processes, we want to
  - DAN-118 (correcao) [Workstream 3: Accelerated recovery and the Restoration 2 approach] 0.479: #### Workstream 3: Accelerated recovery and the Restoration 2 approach  **Timestamp: Days 4 – 13 (April 9th – 17th)**  With the Restoration 1 approach, it would have taken us three weeks to restore al
  - DAN-118 (correcao) [Learning 4: Improve our communications processes] 0.473: ### Learning 4: Improve our communications processes  **a) We deleted critical customer identifiers, impacting communications and actions to those affected**  The same script which deleted customer si

## q-102 (esperado: DAN-121)

- busca inicial: DAN-129, DAN-008, DAN-144, DAN-147, DAN-164, DAN-121, DAN-109, DAN-204, DAN-156, DAN-016
- justificativa: 
- aprofundar DAN-121: `database overload throttle requests services no local cache timeout fix` — O resumo descreve exatamente o mesmo padrão: banco de dados sobrecarregado fazendo throttle, serviços sem cache local dando timeout e caindo, incluindo serviço de vídeo (iPlayer).
- aprofundar DAN-147: `request queue overload database capacity cascading failure fix` — Também envolve banco de dados sobrecarregado por filas de requisições causando falha em cascata, embora não mencione explicitamente cache local dos serviços.
- aprofundar DAN-164: `database overloaded influx requests replication lag recovery fix` — Envolve influxo de requisições sobrecarregando o banco de dados, embora a correção inclua erro humano ao deletar diretório, não exatamente o mesmo gatilho.
  - DAN-121 (llm) [sem seção] 0.524: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (llm) [sem seção] 0.473: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.597: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.578: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-164 (llm) [Timeline] 0.706: ## Timeline  **± 23:00 UTC:** Due to the increased load, our PostgreSQL secondary's replication process started to lag behind. The replication failed as WAL segments needed by the secondary were alrea
  - DAN-164 (llm) [Root cause analysis] 0.675: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-103 (esperado: DAN-121)

- busca inicial: DAN-147, DAN-129, DAN-219, DAN-121, DAN-148, DAN-008, DAN-101, DAN-220, DAN-164, DAN-144
- justificativa: 
- aprofundar DAN-121: `database overload throttle requests local caching timeout fix` — Corresponde quase exatamente: banco de dados sobrecarregado throttling requisições, serviços sem cache local timeoutando e falhando, incluindo vídeo (iPlayer).
- aprofundar DAN-147: `database capacity overload cascading failure remediation` — Semelhança: falha em cascata por fila de requisições sobrecarregando capacidade insuficiente do banco. Diferença: não menciona cache local.
- aprofundar DAN-219: `cache node removal workload outage resolution` — Semelhança: problema relacionado a cache causando sobrecarga. Diferença: remoção de nós de cache causou sobrecarga, não falta de cache local nos serviços.
  - DAN-121 (llm) [sem seção] 0.501: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (llm) [sem seção] 0.461: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.554: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.523: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-219 (llm) [Cascading failure in the cache and datastore tiers] 0.593: ## Cascading failure in the cache and datastore tiers  Once the system is in either a healthy state or a cascading failure state it will tend to stay there, unless there is an external intervention th
  - DAN-219 (llm) [Cascading failure in the cache and datastore tiers] 0.581: ## Cascading failure in the cache and datastore tiers  Early in the incident we had paused the Consul agent restart operation that had triggered the problem, even though at that point we had not suspe
  - DAN-219 (causa) [Learnings] 0.551: ## Learnings  The incident has also highlighted some other risks. A brief network outage or partition affecting the cache nodes might trigger the same kind of cascading failure scenario as the Consul 
  - DAN-219 (correcao) [Learnings] 0.467: ## Learnings  We see familiar patterns here which often arise in incidents: performance bottlenecks, cascading failures, dependency on a warm cache, and changes as triggering events. Reading an incide
  - DAN-219 (correcao) [What triggered the incident?] 0.429: ## What triggered the incident?  The PBR step on February 22 updated Consul on 25% of the fleet. It followed two previous 25% steps the prior week, both of which had occurred without any incident. How

## q-104 (esperado: DAN-122)

- busca inicial: DAN-152, DAN-122, DAN-136, DAN-050, DAN-157, DAN-216, DAN-177, DAN-043, DAN-124, DAN-160
- justificativa: 
- aprofundar DAN-122: `malicious packages impersonation JCenter root cause fix removal` — Ataque por personificação, pacotes maliciosos ficaram mais de um ano no JCenter e afetaram apps Android — corresponde closely ao incidente atual. Difere pelo ecossistema (Maven/Android vs biblioteca genérica).
- aprofundar DAN-152: `npm malicious packages compromised maintainer account root cause fix` — Pacotes maliciosos publicados no registro npm por conta de mantenedor comprometida — semelhança com pacotes maliciosos em repositório público, mas difere no vetor (comprometimento vs personificação) e não menciona permanência de mais de um ano.
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.777: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.717: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Summary] 0.728: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.712: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-105 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-131, DAN-216, DAN-124, DAN-203, DAN-177, DAN-050, DAN-136, DAN-157
- justificativa: 
- aprofundar DAN-122: `malicious packages impersonation JCenter root cause fix removal` — Bate: ataque por personificação, pacotes maliciosos em repositório público (JCenter/Maven) que ficaram mais de um ano e injetaram malware em apps Android. Não bate: ecossistema Maven/Android, não npm.
- aprofundar DAN-152: `malicious packages npm compromised maintainer account root cause fix` — Bate: pacotes maliciosos publicados em registro público usando identidade de desenvolvedor/mantenedor e chegando a apps. Não bate: conta comprometida, não personificação direta, e não menciona permanência de mais de um ano.
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.777: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.717: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Summary] 0.727: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.718: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-106 (esperado: DAN-124)

- busca inicial: DAN-124, DAN-215, DAN-131, DAN-157, DAN-203, DAN-015, DAN-140, DAN-207, DAN-053, DAN-200
- justificativa: 
- aprofundar DAN-124: `Shellshock prototype machine secret keys production breach root cause fix remediation` — Corresponde exatamente: máquina antiga/protótipo, vulnerabilidade Shellshock no bash, chaves secretas, invasão à produção. Os outros incidentes não envolvem Shellshock nem máquina de protótipo.
  - DAN-124 (llm) [Where did we go wrong?] 0.59: ## Where did we go wrong?  All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover,
  - DAN-124 (llm) [What happened?] 0.57: ## What happened?  BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was t
  - DAN-124 (causa) [BrowserStack Security Incident Report — November 2014 (Resolved)] 0.331: # BrowserStack Security Incident Report — November 2014 (Resolved)  Original Incident Statement — Published November 10, 2014  As you may already know, BrowserStack experienced an attack on 9th Novemb
  - DAN-124 (correcao) [Security measures taken to mitigate and prevent further incidents] 0.556: ## Security measures taken to mitigate and prevent further incidents  - After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an add
  - DAN-124 (correcao) [Security Evolution: 2014 → 2026] 0.407: ## Security Evolution: 2014 → 2026  This incident catalyzed a complete transformation of our security infrastructure. Here is what BrowserStack looks like today.  | Area | 2014 Status | 2026 Status (C

## q-107 (esperado: DAN-124)

- busca inicial: DAN-124, DAN-215, DAN-131, DAN-157, DAN-136, DAN-207, DAN-140, DAN-203, DAN-175, DAN-187
- justificativa: 
- aprofundar DAN-124: `Shellshock bash vulnerability prototype machine secret keys production fix` — Bate em tudo: máquina protótipo antiga, falha bash conhecida (Shellshock), chaves secretas e violação da produção; não há diferença essencial.
- aprofundar DAN-131: `engineer laptop malware session theft production access fix` — Semelha por envolver máquina comprometida que leva à produção, mas não é falha bash nem protótipo com chaves secretas.
- aprofundar DAN-203: `support engineer laptop remote access RDP compromise fix` — Semelha por máquina de terceiros comprometida acessando ambientes internos, mas não envolve Shellshock nem chaves secretas.
  - DAN-124 (llm) [Where did we go wrong?] 0.591: ## Where did we go wrong?  All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover,
  - DAN-124 (llm) [What happened?] 0.575: ## What happened?  BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was t
  - DAN-124 (causa) [BrowserStack Security Incident Report — November 2014 (Resolved)] 0.331: # BrowserStack Security Incident Report — November 2014 (Resolved)  Original Incident Statement — Published November 10, 2014  As you may already know, BrowserStack experienced an attack on 9th Novemb
  - DAN-124 (correcao) [Security measures taken to mitigate and prevent further incidents] 0.556: ## Security measures taken to mitigate and prevent further incidents  - After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an add
  - DAN-124 (correcao) [Security Evolution: 2014 → 2026] 0.407: ## Security Evolution: 2014 → 2026  This incident catalyzed a complete transformation of our security infrastructure. Here is what BrowserStack looks like today.  | Area | 2014 Status | 2026 Status (C
  - DAN-131 (llm) [What happened?] 0.524: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.508: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi
  - DAN-203 (llm) [Timeline (times in UTC)] 0.678: ## Timeline (times in UTC)  Our investigation determined that the screenshots, which were not contained in the Sitel summary report, were taken from a Sitel support engineer’s computer upon which an a
  - DAN-203 (llm) [sem seção] 0.478: *This update was posted at 8:50 AM, Pacific Time.*  ++  On March 22, 2022, nearly 24 hours ago, a number of screenshots were published online that were taken from a computer used by one of Okta’s thir
  - DAN-203 (causa) [Timeline (times in UTC)] 0.385: ## Timeline (times in UTC)  In trying to scope the blast radius for this incident, our team assumed the worst-case scenario and examined all of the access performed by all Sitel employees to the Super
  - DAN-203 (correcao) [Timeline (times in UTC)] 0.44: ## Timeline (times in UTC)  - January 20, 2022, 23:18 - Okta Security received an alert that a new factor was added to a Sitel employee’s Okta account from a new location. The target did not accept an

## q-108 (esperado: DAN-125)

- busca inicial: DAN-147, DAN-125, DAN-156, DAN-109, DAN-048, DAN-164, DAN-209, DAN-222, DAN-094, DAN-066
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade AWS spend root cause fix cascading collapse` — Corresponde exatamente ao incidente atual: downgrade da capacidade do banco para reduzir custos na nuvem (AWS), falta de capacidade no horário de pico e colapso em cascata de servidores dependentes.
- aprofundar DAN-147: `insufficient database capacity cascading failure root cause fix monitoring` — Semelha pelo tema de falha em cascata devido à capacidade insuficiente do banco de dados, mas não menciona redução intencional para economizar com nuvem.
  - DAN-125 (llm) [Trying to reduce our AWS bill] 0.699: ## Trying to reduce our AWS bill  About a year ago we were accepted into the AWS Activate program and awarded a bunch of credits to spend on AWS infrastructure. Since then we’ve been growing fast and 
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.678: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.564: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.518: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we

## q-109 (esperado: DAN-125)

- busca inicial: DAN-125, DAN-147, DAN-094, DAN-164, DAN-156, DAN-091, DAN-048, DAN-029, DAN-130, DAN-096
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade peak load cascading collapse fix` — Menciona downgrade explícito do banco para reduzir AWS spend, falta de capacidade no pico e colapso em cascata de servidores dependentes, idêntico ao incidente atual.
- aprofundar DAN-147: `insufficient database capacity cascading failure capacity planning remediation` — Descreve falha em cascata por capacidade insuficiente do banco sob fila de requisições, embora não mencione downsizing específico.
  - DAN-125 (llm) [Database performance issues] 0.652: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.555: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.58: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.559: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we

## q-110 (esperado: DAN-126)

- busca inicial: DAN-126, DAN-116, DAN-058, DAN-103, DAN-170, DAN-154, DAN-164, DAN-043, DAN-048, DAN-026
- justificativa: 
- aprofundar DAN-126: `wrong timestamp bug fix player data loss hotfix misconfiguration rollback` — O título e o resumo coincidem exatamente com o incidente atual: correção de bug de timestamps errados causou perda de dados dos jogadores, e uma configuração errada do hotfix fez a perda voltar em servidores na atualização seguinte.
  - DAN-126 (llm) [Server Configurations] 0.64: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [sem seção] 0.61: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’
  - DAN-126 (correcao) [Server Configurations] 0.372: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th

## q-111 (esperado: DAN-126)

- busca inicial: DAN-126, DAN-058, DAN-103, DAN-116, DAN-170, DAN-164, DAN-048, DAN-154, DAN-043, DAN-127
- justificativa: 
- aprofundar DAN-126: `wrong timestamps bug fix data loss hotfix misconfiguration servers reappear` — O resumo é praticamente idêntico ao incidente atual: correção de bug de timestamps causou perda de dados e uma má configuração no hotfix fez a perda voltar em servidores na atualização seguinte.
  - DAN-126 (llm) [Server Configurations] 0.645: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [Server Configurations] 0.617: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [sem seção] 0.436: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’

## q-112 (esperado: DAN-127)

- busca inicial: DAN-127, DAN-210, DAN-205, DAN-211, DAN-191, DAN-029, DAN-222, DAN-145, DAN-154, DAN-151
- justificativa: 
- aprofundar DAN-127: `logging channel cluster nodes dying startup game patch root cause fix` — O resumo é praticamente idêntico ao incidente atual: mesmo componente (canal de log), mesmo gatilho (novo patch do jogo) e mesma falha (nós morrem na sequência de inicialização do cluster). Os outros incidentes envolvem componentes totalmente diferentes (Kubernetes, rede, storage, Redis, Cassandra, etc.).
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.692: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.679: # Behind the Scenes of a long EVE Online downtime  Via the console we modified the campaign loading functions so that they performed the load-from-DB operations normally, but all their logging operati
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan

## q-113 (esperado: DAN-127)

- busca inicial: DAN-127, DAN-210, DAN-205, DAN-211, DAN-208, DAN-145, DAN-029, DAN-222, DAN-148, DAN-094
- justificativa: 
- aprofundar DAN-127: `logging channel cluster nodes startup patch root cause fix` — O resumo é praticamente idêntico ao incidente atual: mesma falha (logging channel), mesmo gatilho (novo game patch) e mesmo sintoma (nós do cluster morrem na sequência de inicialização).
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.653: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.638: # Behind the Scenes of a long EVE Online downtime  Via the console we modified the campaign loading functions so that they performed the load-from-DB operations normally, but all their logging operati
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan

## q-114 (esperado: DAN-129)

- busca inicial: DAN-129, DAN-224, DAN-209, DAN-035, DAN-073, DAN-027, DAN-066, DAN-205, DAN-194, DAN-008
- justificativa: 
- aprofundar DAN-129: `health check timeout low crash launch latency fix root cause` — O resumo é quase idêntico ao atual: site novo, travou duas horas após o lançamento, latência subindo, respostas intermitentes e health check timeouts muito baixos; não aparece diferença relevante no resumo.
  - DAN-129 (llm) [Health Check Timeouts] 0.668: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [Conclusion] 0.528: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (causa) [Contributing Factors] 0.456: ## Contributing Factors  The supermarket application runs in an AWS account. At launch, it was hosted on three m3.medium instances, with an RDS database, ElasticCache Redis cache, with an Elastic Load
  - DAN-129 (correcao) [Corrective Actions] 0.447: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 

## q-115 (esperado: DAN-129)

- busca inicial: DAN-129, DAN-073, DAN-224, DAN-205, DAN-209, DAN-218, DAN-035, DAN-125, DAN-211, DAN-011
- justificativa: 
- aprofundar DAN-129: `health check timeout too low root cause fix` — O incidente descreve o mesmo cenário: site travado duas horas após o lançamento, latência crescente, respostas intermitentes e timeouts de health check muito baixos, correspondendo praticamente em todos os pontos ao incidente atual.
  - DAN-129 (llm) [Health Check Timeouts] 0.76: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [App Servers Undersized] 0.549: ### App Servers Undersized  The application servers were woefully undersized for the traffic we needed to be able to handle. The single CPU core of an m3.medium was just not enough CPU to keep up with
  - DAN-129 (causa) [Conclusion] 0.457: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (correcao) [Corrective Actions] 0.447: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 

## q-116 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048, DAN-070, DAN-078, DAN-210, DAN-211, DAN-221
- justificativa: 
- aprofundar DAN-145: `Redis primary node migration cloud failover cluster rebalance restart root cause fix` — Bate quase exatamente: migração automática de nó primário Redis por provedor de nuvem, nó cai, cluster rebalanceia, falha no failover e reinício total do serviço; difere apenas na empresa e nos serviços afetados.
- aprofundar DAN-234: `Redis cluster network partition master crash read-only mode restart root cause fix` — Envolve falha de cluster Redis com master crash e reinício, mas o gatilho é partição de rede, não migração automática de nó por provedor de nuvem.
- aprofundar DAN-070: `Redis cluster power outage restart application processes root cause fix` — Envolve Redis clusters e reinício de processos da aplicação, mas o gatilho é perda de energia no datacenter, não migração automática de nó primário.
  - DAN-145 (llm) [Sequence of Events] 0.707: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Summary] 0.651: ## Summary  At approximately 14:01, a Redis instance acting as the primary for a highly-available cluster used by our API services was migrated automatically by Google’s Cloud Platform. This migration
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Action Items / Response] 0.404: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-234 (llm) [Root Cause] 0.619: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (llm) [What We’re Doing About It] 0.602: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn
  - DAN-070 (llm) [The Event] 0.742: ## The Event  By this point, we had a fairly clear picture of what was required to restore service and began working towards that end. We needed to repair our servers that were not booting, and we nee
  - DAN-070 (llm) [The Event] 0.675: ## The Event  Initial notifications for unreachable servers and a spike in exceptions related to Redis connectivity directed our team to investigate a possible outage in our internal network. We also 
  - DAN-070 (causa) [Future Work] 0.507: ## Future Work  Complex systems are defined by the interaction of many discrete components working together to achieve an end result. Understanding the dependencies for each component in a complex sys
  - DAN-070 (correcao) [Future Work] 0.534: ## Future Work  A number of less technical improvements are also being implemented. Strengthening our cross-team communications would have shaved minutes off the recovery time. Predefining escalation 
  - DAN-070 (correcao) [In Conclusion] 0.461: ## In Conclusion  We realize how important GitHub is to the workflows that enable your projects and businesses to succeed. All of us at GitHub would like to apologize for the impact of this outage. We

## q-117 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-066, DAN-029, DAN-234, DAN-078, DAN-048, DAN-210, DAN-070, DAN-211, DAN-093
- justificativa: 
- aprofundar DAN-145: `Redis primary automatic migration failover cascade restart root cause fix` — O incidente atual é praticamente idêntico: migração automática de nó primário Redis por provedor de nuvem, queda offline, rebalanceamento, falha no failover e reinício completo do sistema.
- aprofundar DAN-234: `Redis cluster network partition master crash failover fix` — Também envolve falha de cluster Redis com queda do master e problemas de failover, embora o gatilho seja partição de rede e não migração de nuvem.
  - DAN-145 (llm) [Sequence of Events] 0.71: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Summary] 0.664: ## Summary  At approximately 14:01, a Redis instance acting as the primary for a highly-available cluster used by our API services was migrated automatically by Google’s Cloud Platform. This migration
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Action Items / Response] 0.404: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-234 (llm) [What We’re Doing About It] 0.615: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.603: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn

## q-118 (esperado: DAN-148)

- busca inicial: DAN-148, DAN-217, DAN-106, DAN-066, DAN-205, DAN-067, DAN-109, DAN-221, DAN-068, DAN-191
- justificativa: 
- aprofundar DAN-148: `record concurrent users peak service outage root cause fix` — Bate exatamente: pico recorde de milhões de usuários simultâneos causando falhas parciais e totais em vários serviços, igual ao incidente atual. Não bate: plataforma é jogos (Epic Games), não especificada no atual.
- aprofundar DAN-217: `massive disconnection reconnection database capacity cascading failure fix` — Bate parcialmente: falha em cadeia sob carga comImpacto parcial de usuários. Não bate: gatilho é reconexão em massa após desconexão, não pico recorde de CCU.
- aprofundar DAN-109: `load timeout metadata service cascading node failure fix` — Bate parcialmente: carga provoca timeouts e falha em cadeia de nós. Não bate: causa é disrupção de rede, não pico de usuários simultâneos.
  - DAN-148 (llm) [**Account Service outage**] 0.643: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (llm) [**XMPP outage**] 0.632: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme
  - DAN-217 (llm) [TUESDAY] 0.756: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [WEDNESDAY] 0.539: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [sem seção] 0.375: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.565: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.534: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-119 (esperado: DAN-148)

- busca inicial: DAN-148, DAN-209, DAN-205, DAN-066, DAN-067, DAN-106, DAN-191, DAN-154, DAN-001, DAN-223
- justificativa: 
- aprofundar DAN-148: `3.4 million concurrent users outage cause fix service disruption` — Bate por pico recorde de milhões de usuários simultâneos e interrupções parciais e totais em vários serviços, igual ao incidente atual; não bate por ser plataforma de jogos.
- aprofundar DAN-001: `traffic spike cluster resource management configuration error outage fix` — Bate por pico de tráfego repentino causando queda de serviço; não bate porque a causa foi erro de configuração que impediu escalar instâncias, não somente a carga.
- aprofundar DAN-223: `load balancer heavy load outage postmortem fix StackEgg` — Bate por carga pesada em balanceadores causando indisponibilidade; não bate porque foi desencadeado por ativação de funcionalidade, não por pico orgânico de usuários.
  - DAN-148 (llm) [**XMPP outage**] 0.655: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (llm) [**Account Service outage**] 0.642: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme
  - DAN-001 (llm) [Outage timeline #] 0.705: ## Outage timeline #  Also just before noon, traffic peaked at 200%-300% of the traffic from previous day, depending on service. At this stage, traffic was at its highest but due to excessive resource
  - DAN-001 (llm) [Analysis #] 0.694: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa
  - DAN-223 (llm) [sem seção] 0.731: On 2015-03-31 at 10:00:00 UTC, it was Midnight, April 1st in Samoa (GMT+14). At 10:23:14 UTC, we enabled StackEgg for all logged-in users across all sites the Stack Exchange network. This resulted in 
  - DAN-223 (llm) [sem seção] 0.681: 10:23:14 StackEgg enabled on all sites for everyone  13:42:19 StackEgg disabled on Stack Overflow externally due to load  13:44:30 Flipping StackEgg into Employee overloads the web tier  13:46:13 Stac
  - DAN-223 (causa) [sem seção] 0.322: Once we reached the 40,000 session capacity on the frontend, subsequent sessions are queued and waiting to finish their TCP connect. In the short-term where a batch of requests finishing results in go

## q-120 (esperado: DAN-152)

- busca inicial: DAN-203, DAN-140, DAN-152, DAN-175, DAN-157, DAN-131, DAN-215, DAN-124, DAN-122, DAN-177
- justificativa: 
- aprofundar DAN-152: `npm account compromise malicious package publication root cause fix` — Bate com o atual: conta de mantenedor comprometida no registro de pacotes e pacotes maliciosos publicados. Não bate: é o npm, não o registro do incidente atual.
- aprofundar DAN-122: `malicious Maven packages impersonation attack JCenter root cause fix` — Bate parcialmente: pacotes maliciosos publicados em registro de pacotes (JCenter/Maven). Não bate: mecanismo é impersonation, não tomada de conta do mantenedor.
  - DAN-152 (llm) [Summary] 0.749: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.746: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.728: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.665: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-121 (esperado: DAN-152)

- busca inicial: DAN-152, DAN-177, DAN-140, DAN-131, DAN-157, DAN-122, DAN-175, DAN-124, DAN-132, DAN-203
- justificativa: 
- aprofundar DAN-152: `maintainer account compromised malicious npm package published root cause fix` — O atacante comprometeu a conta do mantenedor no npm e publicou pacotes maliciosos, igual ao incidente atual; difere no ecossistema (npm) e no detalhe de roubar tokens de instaladores.
- aprofundar DAN-122: `malicious packages JCenter impersonation attack root cause fix` — Envolve pacotes maliciosos publicados em um registro de pacotes que afetaram usuários, mas o mecanismo é sequestro de identidade e não comprometimento da conta de um mantenedor.
  - DAN-152 (llm) [Timeline] 0.739: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (llm) [Summary] 0.722: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.777: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.688: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-122 (esperado: DAN-154)

- busca inicial: DAN-154, DAN-011, DAN-037, DAN-018, DAN-023, DAN-005, DAN-008, DAN-106, DAN-016, DAN-020
- justificativa: 
- aprofundar DAN-154: `undiscovered software bug valid customer configuration change global outage root cause fix` — Corresponde exatamente: mudança de configuração válida por cliente acionando bug desconhecido e queda global de CDN; não há diferença aparente no gatilho.
- aprofundar DAN-016: `latent bug rate limiting flawed cookie validation infinite loop fix` — Semelhança: regra recém implantada expôs bug latente; diferença: não é mudança de configuração do cliente nem queda mundial de CDN.
- aprofundar DAN-011: `permissions change file size limit exceeded software outage root cause fix` — Semelhança: mudança de permissões/configuração causou pane propagada por toda rede; diferença: não envolve CDN nem bug desconhecido acionado por cliente.
  - DAN-154 (llm) [sem seção] 0.693: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (llm) [**What happened?**] 0.685: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.724: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.713: ## Technical description of the error and how it happened  ``` for (rule in active_mitigations) {    // ... (ignore other rule types)    if (rule.match_current_request()) {        if (!has_valid_cooki
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Remediation and follow-up steps] 0.472: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-011 (llm) [sem seção] 0.573: On 18 November 2025 at 11:20 UTC (all times in this blog are UTC), Cloudflare's network began experiencing significant failures to deliver core network traffic. This showed up to Internet users trying
  - DAN-011 (llm) [Memory preallocation] 0.558: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic

## q-123 (esperado: DAN-154)

- busca inicial: DAN-154, DAN-011, DAN-008, DAN-005, DAN-020, DAN-037, DAN-007, DAN-023, DAN-029, DAN-018
- justificativa: 
- aprofundar DAN-154: `undiscovered software bug valid customer configuration change global outage root cause fix` — Corresponde quase exatamente: mudança de configuração válida feita por cliente, bug desconhecido no software, CDN derrubado globalmente.
- aprofundar DAN-023: `configuration changes backbone routers global outage root cause fix` — Mudança de configuração causou pane global, mas foi interna (backbone), não por cliente, e não envolve CDN.
- aprofundar DAN-005: `bad config router rule edge routers crash global outage root cause fix` — Configuração ruim derrubou edge globalmente, mas não foi alteração de cliente nem bug desconhecido.
  - DAN-154 (llm) [sem seção] 0.693: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (llm) [**What happened?**] 0.685: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s
  - DAN-023 (llm) [sem seção] 0.633: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.614: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da
  - DAN-005 (llm) [Bad Rule] 0.699: ### Bad Rule  Someone from our operations team is monitoring our network 24/7. As is normal practice for us, one of our ops team members took the output from the profiler and added a rule based on its
  - DAN-005 (llm) [Incident Response] 0.66: ### Incident Response  CloudFlare's ops and network teams were aware of the incident immediately because of both internal and external monitors we run on our network. While it wasn't initially clear t
  - DAN-005 (causa) [sem seção] 0.406: This morning at 09:47 UTC CloudFlare effectively dropped off the Internet. The outage affected all of CloudFlare's services including DNS and any services that rely on our web proxy. During the outage
  - DAN-005 (correcao) [Parallels to Syria] 0.378: ### Parallels to Syria  In writing this up, I was reminded of the parallels to the Syrian Internet outage we reported on earlier this year. In that case, we were able to detect as the Syrian governmen
  - DAN-005 (correcao) [Flowspec] 0.291: ### Flowspec  We are largely a Juniper shop at CloudFlare and all the edge routers that were affected were from Juniper. One of the reasons we like Juniper is their support of a protocol called Flowsp

## q-124 (esperado: DAN-165)

- busca inicial: DAN-165, DAN-221, DAN-103, DAN-184, DAN-231, DAN-195, DAN-033, DAN-003, DAN-084, DAN-078
- justificativa: 
- aprofundar DAN-165: `batch cron job repeated emails non-atomic mark sent root cause fix` — Mesmo tipo de falha (e-mails duplicados >20×), mesmo componente (sistema de e-mail via job em lote) e mesmo gatilho (marcação não atômica só após envio em massa). Pode diferir no contexto (Code Jam vs. sistema atual).
  - DAN-165 (llm) [So what was the bug?] 0.727: ## So what was the bug?  In the App Engine datastore, we have an object called a "notification". That notification has a "status" property, which takes on the following values: "Waiting", "Sending", a
  - DAN-165 (llm) [sem seção] 0.604: A few hours ago, the automated email system for Code Jam went a little bit crazy. I'll write about the technical details below, but the short version is that it sent an email titled "Registration Now 
  - DAN-165 (causa) [Why did I get the repeated email at all?] 0.284: ## Why did I get the repeated email at all?  We sent the notification email to users who registered for Code Jam 2013, checked the box saying "I would like to receive email notifying me about the next
  - DAN-165 (correcao) [Why does Code Jam have its own email system?] 0.272: ## Why does Code Jam have its own email system?  To automatically identify the users who should get an email based on Code Jam-specific properties (such as scores, booleans in user profiles, and regis

## q-125 (esperado: DAN-165)

- busca inicial: DAN-165, DAN-184, DAN-103, DAN-221, DAN-078, DAN-003, DAN-231, DAN-195, DAN-183, DAN-164
- justificativa: 
- aprofundar DAN-165: `batch cron job repeated email root cause fix marking recipients sent` — O DAN-165 é o único incidente com o mesmo sintoma (mesmo email enviado mais de 20 vezes) e a mesma causa raiz (batch job que não marca os destinatários como atendidos até terminar o envio a todos). É o candidato direto para buscar causa raiz e correção.
  - DAN-165 (llm) [So what was the bug?] 0.719: ## So what was the bug?  In the App Engine datastore, we have an object called a "notification". That notification has a "status" property, which takes on the following values: "Waiting", "Sending", a
  - DAN-165 (llm) [sem seção] 0.606: A few hours ago, the automated email system for Code Jam went a little bit crazy. I'll write about the technical details below, but the short version is that it sent an email titled "Registration Now 
  - DAN-165 (causa) [Why did I get the repeated email at all?] 0.284: ## Why did I get the repeated email at all?  We sent the notification email to users who registered for Code Jam 2013, checked the box saying "I would like to receive email notifying me about the next
  - DAN-165 (correcao) [Why does Code Jam have its own email system?] 0.272: ## Why does Code Jam have its own email system?  To automatically identify the users who should get an email based on Code Jam-specific properties (such as scores, booleans in user profiles, and regis

## q-126 (esperado: DAN-170)

- busca inicial: DAN-170, DAN-198, DAN-126, DAN-103, DAN-200, DAN-087, DAN-089, DAN-191, DAN-137, DAN-035
- justificativa: 
- aprofundar DAN-170: `incorrect orbital mechanics calculations satellite positions rollback did not fix root cause` — O título e resumo descrevem exatamente uma atualização ruim com cálculos orbitais errados que fez satélites GPS/GLONASS transmitirem posições incorretas por 10 horas, e o rollback não resolveu imediatamente — idêntico ao incidente atual.
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.583: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  From CODE Analysis protocol: Number of GLONASS observations    reduced by about 10% on April 2nd.  this is why the IGS post
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.576: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Bad Broadcast Messages (resulting in position errors up to about ±200km) were sent out     starting April 1, 2014, 21:00; Fi
  - DAN-170 (causa) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.358: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Understood:    The GNONASS April 1st event was not a joke.    The failure was caused by wrong Broadcast Ephemerides   … p
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.318: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol of April 1). Some receivers unaffected, some stopped tracking GLONASS after 9h p.m. (red line), some even stopped GPS trackin
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.307: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Real-time GNSS Service   -timeIGSOpen Data       •   Observations & derived products freely available       •   Streaming da

## q-127 (esperado: DAN-170)

- busca inicial: DAN-170, DAN-126, DAN-103, DAN-198, DAN-035, DAN-065, DAN-116, DAN-209, DAN-154, DAN-137
- justificativa: 
- aprofundar DAN-170: `satellite wrong calculations incorrect positions update rollback didn't fix root cause` — É o único que envolve satélites com atualização contendo cálculos errados transmitindo posições incorretas por horas, onde o rollback não resolveu de imediato — correspondendo ao incidente atual; os outros não tratam de satélites nem de cálculos orbitais.
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.62: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  From CODE Analysis protocol: Number of GLONASS observations    reduced by about 10% on April 2nd.  this is why the IGS post
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.615: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Bad Broadcast Messages (resulting in position errors up to about ±200km) were sent out     starting April 1, 2014, 21:00; Fi
  - DAN-170 (causa) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.358: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Understood:    The GNONASS April 1st event was not a joke.    The failure was caused by wrong Broadcast Ephemerides   … p
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.318: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol of April 1). Some receivers unaffected, some stopped tracking GLONASS after 9h p.m. (red line), some even stopped GPS trackin
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.307: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Real-time GNSS Service   -timeIGSOpen Data       •   Observations & derived products freely available       •   Streaming da

## q-128 (esperado: DAN-180)

- busca inicial: DAN-180, DAN-209, DAN-048, DAN-191, DAN-222, DAN-164, DAN-129, DAN-066, DAN-067, DAN-107
- justificativa: 
- aprofundar DAN-180: `ingest system repeatedly down cache delay root cause fix` — O resumo menciona exatamente um ingest system que caiu repetidamente por mais de oito horas, mesmo componente e sintoma do incidente atual, embora a causa seja cache Shepherd.
- aprofundar DAN-222: `Cassandra cluster crash message bus ingest blocking fix` — Envolve ingestão de dados em um cluster com falha em cascata que derruba produtores, mas difere por ser um crash do Cassandra e não quedas repetidas do sistema de ingestão.
- aprofundar DAN-107: `data collection server memory leak outage remediation` — Cita um data collection server e uma interrupção prolongada, mas o gatilho é vazamento de memória em servidores de armazenamento, não ingestão repetida instável.
  - DAN-180 (llm) [The events] 0.654: ## The events  We then forced a scale-down of Shepherds to disrupt the pattern, but the autoscaler decided we had too few Shepherds—crashlooping demands a lot of CPU—and instead added more of them. We
  - DAN-180 (llm) [The events] 0.639: ## The events  We decided to do more aggressive sampling in an attempt to stabilize the Refinery cluster by keeping less data. This seemed to work, but sampling aggressively was impacting our ability 
  - DAN-180 (causa) [On causal confusion] 0.541: ### On causal confusion  At one point, our understanding of the situation looked like the following diagram, where orange denotes places where we observed unusual behavior:  Ingestion volume was highe
  - DAN-180 (correcao) [Analysis] 0.509: ## Analysis  This incident revealed areas where we had built mental models of components that proved inaccurate during incidents, and could even clash with each other. This was an opportunity to contr
  - DAN-180 (correcao) [On the solution found] 0.457: ### On the solution found  We still don’t know what triggered all of this, we just know that it was fixed by the cache pre-fill. We are confident the fix worked and is effective because it’s been thro
  - DAN-222 (llm) [sem seção] 0.671: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (llm) [sem seção] 0.646: The Stackdriver Cassandra cluster leaked memory for several days preceding the outage.  We record measurements for many of the metrics relevant to the issue, and the Stackdriver service, which we use 
  - DAN-222 (causa) [sem seção] 0.457: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (correcao) [sem seção] 0.405: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-107 (llm) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.667: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  Last week, one of the data collection servers in the affected Availability Zone had a hardware failure and was replaced. As
  - DAN-107 (llm) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.597: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  We have deployed monitoring that will alarm if we see this specific memory leak again in any of our production EBS servers,
  - DAN-107 (causa) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.433: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  The memory pressure on many of the EBS servers had reached a point where EBS servers began losing the ability to process cu
  - DAN-107 (correcao) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.407: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  Normally these events are simultaneous. Between the period of time the masters were disconnected from their standbys and th
  - DAN-107 (correcao) [Summary of the October 22, 2012 AWS Service Event in the US-East Region] 0.399: ### Summary of the October 22, 2012 AWS Service Event in the US-East Region  Unfortunately, a bug in the traffic shifting functionality incorrectly mapped a small number of the affected load balancers

## q-129 (esperado: DAN-180)

- busca inicial: DAN-180, DAN-209, DAN-181, DAN-222, DAN-164, DAN-208, DAN-217, DAN-191, DAN-102, DAN-067
- justificativa: 
- aprofundar DAN-180: `ingest down repeatedly cache delays root cause fix` — O resumo cita exatamente o sistema de ingest caindo repetidamente por mais de oito horas, igual ao incidente atual, diferentemente dos outros que têm durações ou componentes distintos.
  - DAN-180 (llm) [The events] 0.654: ## The events  We then forced a scale-down of Shepherds to disrupt the pattern, but the autoscaler decided we had too few Shepherds—crashlooping demands a lot of CPU—and instead added more of them. We
  - DAN-180 (llm) [The events] 0.629: ## The events  Our ingestion path is a core part of the system where we know there is continuously increasing stress, and that we will soon re-architect to support growth. Most salient bottlenecks hav
  - DAN-180 (causa) [On causal confusion] 0.541: ### On causal confusion  At one point, our understanding of the situation looked like the following diagram, where orange denotes places where we observed unusual behavior:  Ingestion volume was highe
  - DAN-180 (correcao) [Analysis] 0.509: ## Analysis  This incident revealed areas where we had built mental models of components that proved inaccurate during incidents, and could even clash with each other. This was an opportunity to contr
  - DAN-180 (correcao) [On the solution found] 0.457: ### On the solution found  We still don’t know what triggered all of this, we just know that it was fixed by the cache pre-fill. We are confident the fix worked and is effective because it’s been thro

## q-130 (esperado: DAN-183)

- busca inicial: DAN-183, DAN-134, DAN-096, DAN-148, DAN-129, DAN-016, DAN-094, DAN-026, DAN-101, DAN-077
- justificativa: 
- aprofundar DAN-183: `GKE Dataplane V2 anetd CPU saturation packet drop Postgres memcached root cause fix` — Bate em tudo: migração de nuvem, picos de timeout Postgres, i/o timeout memcached, pool tuning insuficiente e agente de rede do nó (anetd) saturando CPU e descartando pacotes. Não há diferença relevante.
  - DAN-183 (llm) [OK, so what’s actually going on?] 0.68: ## OK, so what’s actually going on?  This revelation suggests that this isn't a process-local issue. What we mean by this is the fact that we were having network issues between our Kubernetes node and
  - DAN-183 (llm) [Meanwhile, a few desks away] 0.6: ## Meanwhile, a few desks away  While all this had been going on, another unrelated issue had cropped up. Thanks to an accidental database join, we’d been making thousands of duplicate network calls t
  - DAN-183 (causa) [Meanwhile, a few desks away] 0.461: ## Meanwhile, a few desks away  This was only happening for a tiny handful of requests among hundreds of thousands, with seemingly no other consistent pattern when it came to which users, organization
  - DAN-183 (correcao) [Clouds, caches and connection conundrums] 0.391: ## Clouds, caches and connection conundrums  Ben Wheatley  September 26, 2023  13 min read  We recently moved our infrastructure fully into Google Cloud. Most things went very smoothly, but there was 
  - DAN-183 (correcao) [OK, so what’s actually going on?] 0.364: ## OK, so what’s actually going on?  If you think about it, it all starts to line up pretty much perfectly with what we’d seen and done up until this point:  - We mostly fixed the DB timeouts by fixin

## q-131 (esperado: DAN-183)

- busca inicial: DAN-183, DAN-148, DAN-134, DAN-129, DAN-096, DAN-001, DAN-077, DAN-107, DAN-101, DAN-026
- justificativa: 
- aprofundar DAN-183: `root cause network agent CPU saturation packet loss memcached Postgres timeouts fix` — Corresponde quase exatamente: migração para outra nuvem, picos de timeouts do Postgres, erros de i/o timeout no memcached, ajuste de pool de conexões ajudou parcialmente e a causa raiz foi o agente de rede do nó saturando CPU e descartando pacotes.
  - DAN-183 (llm) [Meanwhile, a few desks away] 0.627: ## Meanwhile, a few desks away  While all this had been going on, another unrelated issue had cropped up. Thanks to an accidental database join, we’d been making thousands of duplicate network calls t
  - DAN-183 (llm) [/inc spike in connection timeouts] 0.61: ## /inc spike in connection timeouts  The trigger for this incident was a larger-than-normal number of Postgres connection timeouts. This wasn’t something we’d seen with our previous infrastructure, a
  - DAN-183 (causa) [Meanwhile, a few desks away] 0.461: ## Meanwhile, a few desks away  This was only happening for a tiny handful of requests among hundreds of thousands, with seemingly no other consistent pattern when it came to which users, organization
  - DAN-183 (correcao) [Clouds, caches and connection conundrums] 0.391: ## Clouds, caches and connection conundrums  Ben Wheatley  September 26, 2023  13 min read  We recently moved our infrastructure fully into Google Cloud. Most things went very smoothly, but there was 
  - DAN-183 (correcao) [OK, so what’s actually going on?] 0.364: ## OK, so what’s actually going on?  If you think about it, it all starts to line up pretty much perfectly with what we’d seen and done up until this point:  - We mostly fixed the DB timeouts by fixin

## q-132 (esperado: DAN-186)

- busca inicial: DAN-186, DAN-209, DAN-164, DAN-162, DAN-080, DAN-091, DAN-078, DAN-043, DAN-096, DAN-106
- justificativa: 
- aprofundar DAN-186: `hosted database limit reached migration new database root cause fix recovery` — O resumo diz exatamente o mesmo que o incidente atual: limite de banco de dados hospedado atingido e muitas horas para migrar para um novo banco. É o mais parecido da lista.
  - DAN-186 (llm) [**Prevention**] 0.669: # **Prevention**  Without knowledge of the pre-April 2014 file size limit, it was difficult to foresee and prevent this issue. As far as we can tell, there’s no information in the RDS console in the f
  - DAN-186 (llm) [**Root cause**] 0.65: # **Root cause**  In short, the data failure was caused by a 2TB file size limit for RDS instances created before April 2014. On Wednesday, February 9 at 12:30PM PT our “bookmarks” table that stores a
  - DAN-186 (causa) [**Accountability**] 0.46: # **Accountability**  I take full responsibility for the incident and the downtime. While the information about the 2TB limitation wasn’t directly available to me, it’s my responsibility to understand
  - DAN-186 (correcao) [**Action items**] 0.477: # **Action items**  As part of our retrospective process at Pinterest, we’re defining a better workflow for system-wide Instapaper outages that escalate issues immediately to Pinterest’s Site Reliabil
  - DAN-186 (correcao) [**Full service restoration**] 0.454: # **Full service restoration**  Once we had the new ext4-backed database with full data and indexes synced up to the temporary production database, the final step was to promote the new database to ma

## q-133 (esperado: DAN-186)

- busca inicial: DAN-186, DAN-209, DAN-164, DAN-162, DAN-091, DAN-043, DAN-096, DAN-080, DAN-078, DAN-156
- justificativa: 
- aprofundar DAN-186: `hosted database limits hit migration new database recovery` — Descreve exatamente limites de banco de dados hospedado atingidos e migração de várias horas para um novo banco, igual ao incidente atual.
- aprofundar DAN-209: `critical backend system migration error outage recovery` — Envolve erro durante migração de sistema backend crítico, mas o foco é na migração, não nos limites do banco de dados.
- aprofundar DAN-091: `primary database queued operations backlog failover recovery` — Banco de dados primário saturado com fila de operações, relacionado a sobrecarga de banco de dados, mas não a migração para um novo banco.
  - DAN-186 (llm) [**Full service restoration**] 0.683: # **Full service restoration**  Once we had the new ext4-backed database with full data and indexes synced up to the temporary production database, the final step was to promote the new database to ma
  - DAN-186 (llm) [**Data restoration**] 0.674: # **Data restoration**  Once the service was back up and the data dumps completed, the next step was to import all of the dumps into an instance that wasn’t subject to the 2TB file size limit. We work
  - DAN-186 (causa) [**Accountability**] 0.46: # **Accountability**  I take full responsibility for the incident and the downtime. While the information about the 2TB limitation wasn’t directly available to me, it’s my responsibility to understand
  - DAN-186 (correcao) [**Action items**] 0.477: # **Action items**  As part of our retrospective process at Pinterest, we’re defining a better workflow for system-wide Instapaper outages that escalate issues immediately to Pinterest’s Site Reliabil
  - DAN-186 (correcao) [**Prevention**] 0.407: # **Prevention**  Without knowledge of the pre-April 2014 file size limit, it was difficult to foresee and prevent this issue. As far as we can tell, there’s no information in the RDS console in the f
  - DAN-209 (llm) [sem seção] 0.586: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact
  - DAN-209 (llm) [sem seção] 0.544: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 
  - DAN-091 (llm) [Postmortem] 0.707: ## Postmortem  We identified a couple of changes that required additional work but had performed well in evaluation and rolled them back. Unfortunately, by that time the queued DB operations were back
  - DAN-091 (llm) [Postmortem] 0.656: ## Postmortem  We've also moved over 50 percent of the data that was in our primary database onto its own deployment. The data was orthogonal and didn't need to be co-located, but its heavy use was ca
  - DAN-091 (causa) [Postmortem] 0.449: ## Postmortem  THURSDAY 09:00 UTC: We worked to bring up excess capacity to handle the backlog and push builds in as fast as we could. Then we learned that the throttles we had built into our build sc
  - DAN-091 (correcao) [Resolved] 0.326: ## Resolved  We’re continuing to see builds running normally. We will be monitoring closely throughout the day. Please contact us in support if you’re seeing issues with your builds.  Posted Oct 15, 2
  - DAN-091 (correcao) [Postmortem] 0.423: ## Postmortem  Getting back to the architecture, we've known for a while that our queue model needs to be rebuilt and we've been laying the foundation to get there with the items outlined above, but w

## q-134 (esperado: DAN-188)

- busca inicial: DAN-188, DAN-195, DAN-080, DAN-102, DAN-101, DAN-190, DAN-226, DAN-112, DAN-181, DAN-164
- justificativa: 
- aprofundar DAN-188: `PostgreSQL wraparound lock global lock metadata server root cause fix` — O resumo de DAN-188 descreve exatamente o mesmo cenário do incidente atual: operações bloqueadas por lock no metadados do Postgres, com manutenção de wraparound segurando um lock e consulta requisitando lock global. Não há diferença aparente no cenário descrito.
  - DAN-188 (llm) [Summary of Root Cause] 0.679: ### Summary of Root Cause  In summary:  - All Manta operations touch our sharded, PostgreSQL-backed metadata tier. - During the event, one of the shard databases had all queries on our primary table b
  - DAN-188 (llm) [The problem] 0.645: ### The problem  We observed the autovacuum scan the full table and all of its indexes, and then do the same thing again. After several hours, it successfully completed and updated the "last\_autovacu
  - DAN-188 (causa) [Root cause analysis] 0.545: ## Root cause analysis  For transparency, we've included a lot of detail here about how the incident proceeded. If you're interested in more of a summary, skip to the Summary of Root Cause section bel
  - DAN-188 (correcao) [Closing] 0.517: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working hard to prevent an issue like this from happ
  - DAN-188 (correcao) [Reflections] 0.466: ## Reflections  First of all, we want to emphasize that we're sorry about this incident. We strive to maintain very high availability for all our services, and we know our customers are greatly impact

## q-135 (esperado: DAN-188)

- busca inicial: DAN-188, DAN-195, DAN-080, DAN-102, DAN-190, DAN-181, DAN-226, DAN-164, DAN-101, DAN-112
- justificativa: 
- aprofundar DAN-188: `Postgres wraparound maintenance lock global lock metadata database outage root cause fix` — Mesmo componente (banco de metadados Postgres), mesma causa (manutenção de wraparound segurando lock + query pedindo global lock) e mesmo sintoma (operações bloqueadas).
- aprofundar DAN-195: `Postgres transaction ID wraparound outage root cause fix vacuum` — Também envolve wraparound de IDs de transação do Postgres causando outage, mas não menciona global lock nem banco de metadados.
- aprofundar DAN-102: `Postgres critical locks extension hung migration root cause fix restart` — Envolve extensão Postgres segurando locks críticos e bloqueando operações DB, mas o gatilho é PGAudit/migration, não wraparound.
  - DAN-188 (llm) [Summary of Root Cause] 0.714: ### Summary of Root Cause  In summary:  - All Manta operations touch our sharded, PostgreSQL-backed metadata tier. - During the event, one of the shard databases had all queries on our primary table b
  - DAN-188 (llm) [The problem] 0.694: ### The problem  We quickly identified that API requests were hanging and ultimately failing because all queries to one of the PostgreSQL databases were themselves hanging. API servers timed out these
  - DAN-188 (causa) [Root cause analysis] 0.545: ## Root cause analysis  For transparency, we've included a lot of detail here about how the incident proceeded. If you're interested in more of a summary, skip to the Summary of Root Cause section bel
  - DAN-188 (correcao) [Closing] 0.517: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working hard to prevent an issue like this from happ
  - DAN-188 (correcao) [The problem] 0.482: ### The problem  We observed the autovacuum scan the full table and all of its indexes, and then do the same thing again. After several hours, it successfully completed and updated the "last\_autovacu
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.795: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.667: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg
  - DAN-102 (llm) [sem seção] 0.649: On Wednesday, April 9, 2025, between 14:16 and 14:27 UTC, our systems experienced intermittent availability issues. The incident culminated in a 2-minute database outage from 14:25 to 14:27 UTC across
  - DAN-102 (llm) [sem seção] 0.54: Key elements of our infrastructure are designed to handle this scenario, and so, importantly, no on-call alerts or escalations were dropped during this period.  After restoring service, we temporarily

## q-136 (esperado: DAN-189)

- busca inicial: DAN-189, DAN-103, DAN-106, DAN-191, DAN-146, DAN-067, DAN-068, DAN-064, DAN-048, DAN-210
- justificativa: 
- aprofundar DAN-189: `root cause lax input validation reboot all servers fix remediation` — O incidente DAN-189 é quase idêntico ao atual: operador usou ferramenta com validação fraca para reiniciar servidores em manutenção, esqueceu um parâmetro (-n) e reiniciou todos os servidores do datacenter. Outros incidentes são de falhas de hardware, energia, resfriamento ou upgrades de software, sem relação com erro de operador em ferramenta de reinicialização.
  - DAN-189 (llm) [What Happened?] 0.568: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.536: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-137 (esperado: DAN-189)

- busca inicial: DAN-189, DAN-103, DAN-146, DAN-191, DAN-106, DAN-067, DAN-048, DAN-064, DAN-068, DAN-066
- justificativa: 
- aprofundar DAN-189: `input validation reboot tool forgot parameter root cause fix` — O resumo descreve exatamente o mesmo cenário do incidente atual: operador usou ferramenta com validação frouxa de entrada, esqueceu um parâmetro (-n) e reiniciou todos os servidores do datacenter, diferente dos demais incidentes que envolvem energia, armazenamento ou falhas de software.
  - DAN-189 (llm) [What Happened?] 0.563: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [What Happened?] 0.514: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (causa) [Next Steps] 0.434: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-138 (esperado: DAN-194)

- busca inicial: DAN-194, DAN-156, DAN-190, DAN-164, DAN-048, DAN-133, DAN-078, DAN-066, DAN-093, DAN-098
- justificativa: 
- aprofundar DAN-194: `secondary MongoDB overloaded traffic primary root cause fix` — Bate exatamente: secundárias MongoDB sobrecarregadas e mudança acidental que enviou todo o tráfego para o primário, sobrecarregando-o também. É o único incidente com esse mesmo gatilho e componente.
  - DAN-194 (llm) [Website Intermittent Timeouts] 0.663: ## Website Intermittent Timeouts  ## Postmortem  ## Summary  On January 12th at 14:09 UTC, our engineers began responding to alerts for our click / open tracking services and primary MongoDB clusters 
  - DAN-194 (llm) [Summary] 0.64: ## Summary  After review of our MongoDB configurations, we deployed limits on the number of connections our services could establish to our primary MongoDB server. We prepared these changes and began 
  - DAN-194 (causa) [Corrective Actions] 0.357: ## Corrective Actions  - Deployment of Redundant Tracking Infrastructure (Complete) - Our tracking services have previously operated out of a single region. As part of previously planned infrastructur
  - DAN-194 (correcao) [Resolved] 0.444: ## Resolved  This incident has been resolved.  Posted Jan 12, 2017 - 15:10 PST  ## Monitoring  Mailgun engineers have made a series of changes to our system, which have improved the performance and st
  - DAN-194 (correcao) [Identified] 0.327: ## Identified  We’re seeing improved performance and stability from our core API & SMTP services at this time. The engineering team is continuing to work to completely resolve the issue.  Posted Jan 1

## q-139 (esperado: DAN-194)

- busca inicial: DAN-194, DAN-156, DAN-164, DAN-048, DAN-133, DAN-066, DAN-190, DAN-078, DAN-098, DAN-219
- justificativa: 
- aprofundar DAN-194: `secondary overload accidental reads primary root cause fix` — O resumo é praticamente idêntico ao incidente atual: secondaries sobrecarregadas e mudança acidental enviando leituras para o primary, sobrecarregando-o também; não há diferença aparente no cenário descrito.
  - DAN-194 (llm) [Website Intermittent Timeouts] 0.462: ## Website Intermittent Timeouts  ## Postmortem  ## Summary  On January 12th at 14:09 UTC, our engineers began responding to alerts for our click / open tracking services and primary MongoDB clusters 
  - DAN-194 (llm) [Summary] 0.415: ## Summary  After review of our MongoDB configurations, we deployed limits on the number of connections our services could establish to our primary MongoDB server. We prepared these changes and began 
  - DAN-194 (causa) [Corrective Actions] 0.357: ## Corrective Actions  - Deployment of Redundant Tracking Infrastructure (Complete) - Our tracking services have previously operated out of a single region. As part of previously planned infrastructur
  - DAN-194 (correcao) [Resolved] 0.444: ## Resolved  This incident has been resolved.  Posted Jan 12, 2017 - 15:10 PST  ## Monitoring  Mailgun engineers have made a series of changes to our system, which have improved the performance and st
  - DAN-194 (correcao) [Identified] 0.327: ## Identified  We’re seeing improved performance and stability from our core API & SMTP services at this time. The engineering team is continuing to work to completely resolve the issue.  Posted Jan 1

## q-140 (esperado: DAN-197)

- busca inicial: DAN-066, DAN-154, DAN-197, DAN-106, DAN-029, DAN-209, DAN-018, DAN-067, DAN-145, DAN-023
- justificativa: 
- aprofundar DAN-197: `unannounced breaking change API root cause recovery fix` — O resumo descreve exatamente uma mudança incompatível na API do Azure publicada sem aviso, afetando serviços downstream, igual ao incidente atual.
  - DAN-197 (llm) [sem seção] 0.649: Although APIs are the lifeblood of so many software applications today, the impact on their dependencies when they break can often be overlooked. And while full outages can have a more widespread and 
  - DAN-197 (llm) [Conclusions] 0.618: ## Conclusions  All in all, this was a fairly simple fix, but because of the nature of the API, it could have been worse. The more deeply ingrained a given API is into one’s app, the bigger an effect 
  - DAN-197 (causa) [Discovery of the Outage] 0.424: ## Discovery of the Outage  While this data was not the most helpful, it confirmed that there was something wrong with our request, despite no changes to how we made the request in months. Until seein
  - DAN-197 (correcao) [Background] 0.362: ## Background  First, a bit of background on how we use Azure CosmosDB, and how we obtained the debugging data to determine that Azure published a breaking change without telling their customers. Metr
  - DAN-197 (correcao) [Determining the Change] 0.347: ## Determining the Change  The next step was to figure out what actually changed. Our service monitor code hadn’t been touched in several months and is fairly straightforward, using the account and da

## q-141 (esperado: DAN-197)

- busca inicial: DAN-197, DAN-066, DAN-154, DAN-018, DAN-067, DAN-029, DAN-193, DAN-145, DAN-189, DAN-210
- justificativa: 
- aprofundar DAN-197: `unannounced breaking API change Azure downstream service recovery` — É o único que corresponde exatamente: provedor de nuvem (Azure) mudou API sem aviso e quebrou serviço dependente downstream.
- aprofundar DAN-145: `GCP unexpected Redis migration failover cascading failure fix` — Também envolve provedor de nuvem (GCP) fazendo alteração não anunciada que afetou o serviço, mas é infraestrutura Redis, não uma mudança de API.
  - DAN-197 (llm) [sem seção] 0.757: Although APIs are the lifeblood of so many software applications today, the impact on their dependencies when they break can often be overlooked. And while full outages can have a more widespread and 
  - DAN-197 (llm) [Background] 0.67: ## Background  First, a bit of background on how we use Azure CosmosDB, and how we obtained the debugging data to determine that Azure published a breaking change without telling their customers. Metr
  - DAN-197 (causa) [Discovery of the Outage] 0.424: ## Discovery of the Outage  While this data was not the most helpful, it confirmed that there was something wrong with our request, despite no changes to how we made the request in months. Until seein
  - DAN-197 (correcao) [Conclusions] 0.356: ## Conclusions  All in all, this was a fairly simple fix, but because of the nature of the API, it could have been worse. The more deeply ingrained a given API is into one’s app, the bigger an effect 
  - DAN-197 (correcao) [Determining the Change] 0.347: ## Determining the Change  The next step was to figure out what actually changed. Our service monitor code hadn’t been touched in several months and is fairly straightforward, using the account and da
  - DAN-145 (llm) [Sequence of Events] 0.728: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.685: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci

## q-142 (esperado: DAN-200)

- busca inicial: DAN-200, DAN-103, DAN-154, DAN-191, DAN-126, DAN-198, DAN-209, DAN-066, DAN-116, DAN-170
- justificativa: 
- aprofundar DAN-200: `priority inversion VxWorks remote patch system resets` — O resumo descreve reinícios de sistema dias após o pouso, causados por inversão de prioridade no VxWorks e corrigidos por patch remoto, idêntico ao incidente atual.
- aprofundar DAN-198: `Apollo 11 radar CPU load computer restart fix` — Também envolve reinício do computador de nave espacial, mas a causa é falha de projeto no radar que gera carga excessiva de CPU, não inversão de prioridade.
  - DAN-200 (llm) [THE FAILURE] 0.587: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [THE SOFTWARE ARCHITECTURE] 0.536: ## THE SOFTWARE ARCHITECTURE  The bc_sched and bc_dist tasks check each cycle to be sure that the other had completed its execution. The bc_sched task is the highest priority task in the system (excep
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.718: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.677: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-143 (esperado: DAN-200)

- busca inicial: DAN-200, DAN-191, DAN-198, DAN-116, DAN-154, DAN-106, DAN-103, DAN-189, DAN-221, DAN-113
- justificativa: 
- aprofundar DAN-200: `priority inversion VxWorks remote patch priority inheritance root cause fix` — é o mesmo cenário exato: computador reiniciando dias após início, causa inversão de prioridade em sistema operacional em tempo real e correção via patch remoto
- aprofundar DAN-198: `Apollo 11 rendezvous radar CPU load computer restart root cause fix` — também envolve reinício do computador de nave espacial, mas a causa é carga excessiva de CPU por radar, não inversão de prioridade nem patch remoto de RTOS
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.625: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.6: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-200 (causa) [THE FAILURE] 0.577: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HUMAN NATURE, DEADLINE PRESSURES] 0.436: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-198 (llm) [sem seção] 0.724: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.68: This phenomenon occurred whenever the RR mode was in SLEW or AUTO, regardless of whether the rendezvous radar itself was powered up. | | The CDU interface counters in the LGC were incremented or decre
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-144 (esperado: DAN-204)

- busca inicial: DAN-204, DAN-234, DAN-164, DAN-219, DAN-145, DAN-180, DAN-008, DAN-098, DAN-221, DAN-058
- justificativa: 
- aprofundar DAN-204: `Redis cache queue corruption out of sequence root cause fix cross-user data leakage billing` — Resumo idêntico ao incidente atual: filas Redis corrompidas/fora de ordem, vazamento de dados entre usuários incluindo billing — mesmo tipo de falha, mesmo componente e mesmo sintoma.
- aprofundar DAN-234: `Redis billing cluster network partition root cause fix multiple charges` — Também envolve Redis usado para billing, mas a falha é partição de rede e reinscrição, não filas corrompidas; parecido no componente e domínio, diferente no gatilho.
  - DAN-204 (llm) [Technical details] 0.6: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.563: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-234 (llm) [What We’re Doing About It] 0.728: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.727: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn

## q-145 (esperado: DAN-204)

- busca inicial: DAN-204, DAN-234, DAN-164, DAN-219, DAN-145, DAN-008, DAN-180, DAN-190, DAN-221, DAN-058
- justificativa: 
- aprofundar DAN-204: `Redis cache queue corruption out of sequence root cause fix data leak` — Descreve exatamente o mesmo sintoma: filas de requisição/resposta corrompidas e fora de ordem no Redis fazendo usuários verem dados de outros usuários, incluindo informações de faturamento. Os outros incidentes envolvem Redis ou faturamento, mas com cenários diferentes.
  - DAN-204 (llm) [Technical details] 0.614: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.536: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa

## q-146 (esperado: DAN-205)

- busca inicial: DAN-205, DAN-068, DAN-191, DAN-106, DAN-209, DAN-064, DAN-078, DAN-077, DAN-020, DAN-067
- justificativa: 
- aprofundar DAN-205: `common peering point instability quorum notification failure root cause fix` — O DAN-205 é o único que descreve exatamente o mesmo cenário: duas de três implantações em datacenters diferentes com ponto de peering comum instável, perda de quórum e falha no envio de notificações. Os outros incidentes tratam de falha de energia, erro humano, migração, resfriamento ou descoberta de serviço, sem relação com peering ou quórum.
  - DAN-205 (llm) [The Outage] 0.695: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.597: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig

## q-147 (esperado: DAN-205)

- busca inicial: DAN-205, DAN-068, DAN-191, DAN-078, DAN-066, DAN-020, DAN-106, DAN-209, DAN-077, DAN-067
- justificativa: 
- aprofundar DAN-205: `shared peering point instability quorum notification failure fix` — Bate exatamente com o atual: duas de três implantações em datacenters diferentes, ponto de peering compartilhado instável, perda de quorum e falha ao enviar notificações.
- aprofundar DAN-078: `network partition cross-continent latency MySQL quorum failover fix` — Tem partição de rede e latência entre locais afetando failover/quorum, mas não envolve três implantações com ponto de peering compartilhado.
- aprofundar DAN-077: `network failure heartbeat quorum STONITH recovery fix` — Envolve falha de rede entre locais fazendo pares excederem heartbeats e perderem quorum, mas o gatilho é uma mudança de switch, não um ponto de peering instável.
  - DAN-205 (llm) [The Outage] 0.697: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.617: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig
  - DAN-078 (llm) [Incident timeline] 0.69: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.651: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (causa) [2018 October 22 16:24 UTC] 0.471: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-078 (correcao) [Next steps] 0.448: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-077 (llm) [sem seção] 0.614: disk to the standby node in the pair. Heartbeat and Pacemaker work  together to help manage this process and to failover in the event of  problems on the active node.  With DRBD, it’s important to mak
  - DAN-077 (llm) [sem seção] 0.57: 1. We put GitHub.com into maintenance mode. 2. We paged the entire operations team to assist with the recovery. 3. We downgraded both aggregation switches to the previous software version. 4. We devel
  - DAN-077 (causa) [sem seção] 0.47: minutes of instability while we attempted to work around them within  the maintenance window. Disabling the links between half of the  aggregation switches and the access switches allowed us to mitiga
  - DAN-077 (correcao) [sem seção] 0.423: 1. We worked closely with our network vendor to identify and understand the problems that led to the failure of MLAG to failover in the way that we expected. While it behaved as designed, our vendor p
  - DAN-077 (correcao) [sem seção] 0.342: On Saturday, December 22nd we had a significant outage and we want to take  the time to explain what happened. This was one of the worst outages in  the history of GitHub, and it’s not at all acceptab

## q-148 (esperado: DAN-207)

- busca inicial: DAN-207, DAN-215, DAN-136, DAN-154, DAN-084, DAN-066, DAN-142, DAN-050, DAN-124, DAN-013
- justificativa: 
- aprofundar DAN-207: `security bug mislabeled UI change inadequate review deployed cryptocurrency fix` — Mesmo padrão: grande mudança com falha de segurança rotulada como mudança de interface, revisão insuficiente, deploy e desvio de criptomoeda; os outros incidentes são de tipos totalmente diferentes.
  - DAN-207 (llm) [HOW DID THE BUG ESCAPE NOTICE?] 0.697: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.59: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (causa) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.31: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [sem seção] 0.307: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall

## q-149 (esperado: DAN-207)

- busca inicial: DAN-207, DAN-136, DAN-215, DAN-154, DAN-124, DAN-050, DAN-142, DAN-177, DAN-066, DAN-106
- justificativa: 
- aprofundar DAN-207: `mislabeled UI change security bug deployed diverted cryptocurrency root cause fix` — O resumo cita uma grande mudança de software com bug de segurança rotulada como UI change, revisão inadequada, deploy e desvio de milhões em criptomoeda — correspondência direta com o incidente atual.
  - DAN-207 (llm) [HOW DID THE BUG ESCAPE NOTICE?] 0.616: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.579: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (causa) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.31: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [sem seção] 0.307: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall

## q-150 (esperado: DAN-208)

- busca inicial: DAN-208, DAN-144, DAN-079, DAN-106, DAN-222, DAN-164, DAN-066, DAN-151, DAN-109, DAN-191
- justificativa: 
- aprofundar DAN-208: `Zookeeper too much data boot failure maintenance window fix` — Mesmo componente (Zookeeper), mesmo gatilho (janela de manutenção programada) e mesma causa (dados excessivos impedindo o boot); não há diferença relevante no resumo.
- aprofundar DAN-079: `ZooKeeper reprovisioning replacement hosts leader election fix` — Envolve ZooKeeper durante operação de infraestrutura planejada, mas a falha é eleição de líder duplicado, não dados demais nem impossibilidade de boot.
  - DAN-208 (llm) [Read the socket] 0.717: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (llm) [Wrapping up] 0.715: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\
  - DAN-079 (llm) [sem seção] 0.655: In October, we experienced one incident resulting in significant impact and degraded state of availability for issues, pull requests, webhooks, GitHub Actions, and GitHub Pages services.  While reprov

## q-151 (esperado: DAN-208)

- busca inicial: DAN-208, DAN-151, DAN-222, DAN-109, DAN-164, DAN-079, DAN-144, DAN-134, DAN-188, DAN-103
- justificativa: 
- aprofundar DAN-208: `Zookeeper too much data startup failure maintenance root cause fix` — Corresponde exatamente ao incidente atual: Zookeeper não inicia devido a excesso de dados durante janela de manutenção programada. Outros incidentes são de componentes ou gatilhos diferentes.
  - DAN-208 (llm) [Read the socket] 0.725: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (llm) [Wrapping up] 0.705: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\

## q-152 (esperado: DAN-215)

- busca inicial: DAN-215, DAN-207, DAN-131, DAN-203, DAN-124, DAN-084, DAN-140, DAN-157, DAN-068, DAN-160
- justificativa: 
- aprofundar DAN-215: `employee cryptocurrency theft poor security practices root cause fix` — O resumo é praticamente idêntico ao incidente atual: funcionário roubou criptomoeda em 3 invasões ao longo de 1 mês devido a práticas de segurança fracas.
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.562: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.512: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.353: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Digital Forensic Investigation Following the preliminary investigation, a digital-forensic investigation was launched to analyze both Infrastructure2 and Infrastr
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo

## q-153 (esperado: DAN-215)

- busca inicial: DAN-215, DAN-207, DAN-131, DAN-124, DAN-203, DAN-132, DAN-157, DAN-175, DAN-068, DAN-084
- justificativa: 
- aprofundar DAN-215: `weak security practices employee cryptocurrency theft root cause fix` — O resumo bate quase exatamente com o incidente atual: funcionário roubou criptomoeda devido a práticas de segurança frágeis, em 3 arrombamentos ao longo de 1 mês. Preciso ver a causa raiz detalhada e a correção aplicada.
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.583: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.53: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Conclusion The digital-forensic investigation, combined with the CCSS assessment, identified a number of opportunities to increase ShapeShift’s security. Ledger L
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.355: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo

## q-154 (esperado: DAN-226)

- busca inicial: DAN-226, DAN-048, DAN-116, DAN-181, DAN-190, DAN-126, DAN-129, DAN-120, DAN-094, DAN-058
- justificativa: 
- aprofundar DAN-226: `SQL Server bugcheck root cause read-only outage fix` — É o único incidente que reproduz exatamente o sintoma atual: bugcheck no processo primário do SQL Server, sites em modo somente leitura e queda total. Outros incidentes falam de bancos de dados, mas não de bugcheck do SQL Server.
  - DAN-226 (llm) [sem seção] 0.655: On January 24, 2017 starting at 17:53 UTC, we experienced system degradation (read only) followed by a site outage. The Stack Exchange network went into read-only mode for approximately 5 minutes befo

## q-155 (esperado: DAN-226)

- busca inicial: DAN-226, DAN-120, DAN-048, DAN-181, DAN-027, DAN-094, DAN-080, DAN-066, DAN-146, DAN-154
- justificativa: 
- aprofundar DAN-226: `SQL Server bugcheck root cause fix read only mode outage` — É praticamente idêntico ao incidente atual: mesmo componente (SQL Server), mesmo gatilho (bugcheck do processo) e mesma evolução (read-only, depois outage completo).
  - DAN-226 (llm) [sem seção] 0.659: On January 24, 2017 starting at 17:53 UTC, we experienced system degradation (read only) followed by a site outage. The Stack Exchange network went into read-only mode for approximately 5 minutes befo

## q-156 (esperado: DAN-235)

- busca inicial: DAN-235, DAN-231, DAN-221, DAN-184, DAN-022, DAN-069, DAN-165, DAN-154, DAN-059, DAN-234
- justificativa: 
- aprofundar DAN-235: `SMS filtering root cause fix AT&T network United States` — Este incidente trata exatamente de alto filtramento de SMS para a rede AT&T nos EUA, mesma falha do incidente atual (SMS filtrados em massa para operadora americana). Difere apenas na operadora específica (AT&T vs não informada).
  - DAN-235 (llm) [Investigating] 0.743: ## Investigating  We are experiencing high filtering on SMS towards AT&T network in Unites states. Our engineers are working with our carrier partner to resolve the issue. We expect to provide another
  - DAN-235 (llm) [High Filtering On SMS Towards AT&T Network In United States] 0.74: ## High Filtering On SMS Towards AT&T Network In United States  ## Resolved  We are no longer experiencing high filtering on SMS towards AT&T network in the United States for all senders. This inciden
  - DAN-235 (causa) [Update] 0.24: ## Update  We are experiencing high filtering on SMS towards AT&T network in United States. Our engineers are continuing to work with our carrier partner to resolve the issue. We expect to provide ano
  - DAN-235 (correcao) [Monitoring] 0.273: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States. We will continue to monitor to ensure full service recovery. We expect to provide another
  - DAN-235 (correcao) [Monitoring] 0.254: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States for all senders. We will continue monitoring the service to ensure a full recovery. We wil

## q-157 (esperado: DAN-235)

- busca inicial: DAN-235, DAN-231, DAN-221, DAN-184, DAN-022, DAN-165, DAN-154, DAN-065, DAN-011, DAN-059
- justificativa: 
- aprofundar DAN-235: `SMS filtering AT&T carrier blocked messages root cause fix` — Corresponde ao incidente atual por tratar de filtragem em massa de SMS para uma operadora dos EUA (AT&T), mas difere por ser específico da plataforma Twilio e o resumo não detalhar a causa raiz nem a correção aplicada.
  - DAN-235 (llm) [Investigating] 0.704: ## Investigating  We are experiencing high filtering on SMS towards AT&T network in Unites states. Our engineers are working with our carrier partner to resolve the issue. We expect to provide another
  - DAN-235 (llm) [High Filtering On SMS Towards AT&T Network In United States] 0.698: ## High Filtering On SMS Towards AT&T Network In United States  ## Resolved  We are no longer experiencing high filtering on SMS towards AT&T network in the United States for all senders. This inciden
  - DAN-235 (causa) [Update] 0.24: ## Update  We are experiencing high filtering on SMS towards AT&T network in United States. Our engineers are continuing to work with our carrier partner to resolve the issue. We expect to provide ano
  - DAN-235 (correcao) [Monitoring] 0.273: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States. We will continue to monitor to ensure full service recovery. We expect to provide another
  - DAN-235 (correcao) [Monitoring] 0.254: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States for all senders. We will continue monitoring the service to ensure a full recovery. We wil

## q-158 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-154, DAN-146, DAN-126, DAN-220, DAN-073, DAN-104, DAN-058, DAN-173, DAN-142
- justificativa: 
- aprofundar DAN-236: `steam desktop client deleted local files root cause fix` — O cliente da Steam deletou arquivos e pastas locais dos usuários, e o bug já havia sido relatado meses antes sem ser triado — igual ao incidente atual.
  - DAN-236 (llm) [Activity] 0.702: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.699: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 

## q-159 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-220, DAN-126, DAN-164, DAN-146, DAN-058, DAN-118, DAN-104, DAN-154, DAN-043
- justificativa: 
- aprofundar DAN-236: `steam client deleted local files root cause fix rm -rf` — Corresponde exatamente: cliente de desktop deletou arquivos locais, bug reportado meses antes sem triagem, igual ao incidente atual. Outros incidentes são de banco de dados, cascata ou nuvem, não cliente desktop.
  - DAN-236 (llm) [Activity] 0.72: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [jthill commentedon Jan 15, 2015] 0.708: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [doofy commentedon Jan 15, 2015] 0.293: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 

## q-160 (esperado: DAN-237)

- busca inicial: DAN-237, DAN-131, DAN-124, DAN-203, DAN-152, DAN-142, DAN-157, DAN-215, DAN-011, DAN-122
- justificativa: 
- aprofundar DAN-237: `website compromise malicious zip download links root cause fix` — Bate exatamente: site comprometido e links de download trocados por arquivo zip malicioso, o mesmo cenário do incidente atual. Difere apenas por se tratar de uma distribuição Linux específica (Xubuntu).
- aprofundar DAN-152: `npm account compromise malicious packages root cause fix` — Bate parcialmente: distribuição de pacotes maliciosos após compromisso de credenciais. Difere no vetor: conta npm comprometida, não site com links de download trocados.
- aprofundar DAN-122: `malicious Maven packages impersonation attack root cause fix` — Bate parcialmente: pacotes maliciosos distribuídos por repositório público. Difere no mecanismo: ataque de personificação no JCenter, sem comprometimento de site de downloads.
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.679: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  **Elizabeth K. Joseph**     lyz at ubuntu.com  *Mon Nov 17 17:59:36 UTC 2025*  Dear community, As
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.502: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  in a controlled, read-only mode to allow migration to a new static site. To be perfectly clear: t
  - DAN-237 (causa) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.234: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  generator has actually been in the works for some time as our reliance upon the dynamic features 
  - DAN-152 (llm) [Summary] 0.735: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.71: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.649: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.578: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-161 (esperado: DAN-237)

- busca inicial: DAN-237, DAN-131, DAN-157, DAN-124, DAN-160, DAN-152, DAN-119, DAN-050, DAN-136, DAN-140
- justificativa: 
- aprofundar DAN-237: `website compromise malicious zip download links root cause fix` — Corresponde exatamente ao incidente atual: site do projeto comprometido e links de download trocados por arquivo zip malicioso.
- aprofundar DAN-152: `npm account compromise malicious packages published root cause fix` — Padrão semelhante de comprometimento de conta confiável para distribuir software malicioso, mas via pacotes npm em vez de links do site.
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.679: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  **Elizabeth K. Joseph**     lyz at ubuntu.com  *Mon Nov 17 17:59:36 UTC 2025*  Dear community, As
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.502: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  in a controlled, read-only mode to allow migration to a new static site. To be perfectly clear: t
  - DAN-237 (causa) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.234: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  generator has actually been in the works for some time as our reliance upon the dynamic features 
  - DAN-152 (llm) [Summary] 0.745: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.732: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-162 (esperado: DAN-240)

- busca inicial: DAN-240, DAN-068, DAN-239, DAN-159, DAN-191, DAN-084, DAN-063, DAN-066, DAN-067, DAN-048
- justificativa: 
- aprofundar DAN-240: `leased line failure backup unstable root cause fix bracket cover orders` — DAN-240 descreve exatamente o mesmo cenário: falha do link dedicado primário entre corretora e bolsa, link de backup instável na hora seguinte e tipos específicos de ordem afetados (bracket e cover). É o único incidente da lista com correspondência direta de componente, gatilho e impacto.
  - DAN-240 (llm) [sem seção] 0.578: 13 Apr 2018, 01:48 PM  # Postmortem: Trading and hanging orders on 12th April 2018  Traders,  Yesterday, on the 12th April, one of the NSE leased line connections to our setup went down. This affected
  - DAN-240 (llm) [Postmortem: Trading and hanging orders on 12th April 2018] 0.51: # Postmortem: Trading and hanging orders on 12th April 2018  Once the CTCL was shut off, the orders which were showing any of the pending states were lapsed and reconciled with the exchange. This affe

## q-163 (esperado: DAN-240)

- busca inicial: DAN-240, DAN-068, DAN-239, DAN-209, DAN-191, DAN-084, DAN-077, DAN-106, DAN-066, DAN-078
- justificativa: 
- aprofundar DAN-240: `leased line root cause backup line instability fix remediation` — É o único incidente que envolve exatamente falha de linha alugada primária entre corretora e bolsa, linha de backup instável por aproximadamente uma hora e impacto em tipos específicos de ordem (bracket e cover orders), correspondendo ao cenário atual.
  - DAN-240 (llm) [sem seção] 0.559: 13 Apr 2018, 01:48 PM  # Postmortem: Trading and hanging orders on 12th April 2018  Traders,  Yesterday, on the 12th April, one of the NSE leased line connections to our setup went down. This affected
  - DAN-240 (llm) [Postmortem: Trading and hanging orders on 12th April 2018] 0.394: # Postmortem: Trading and hanging orders on 12th April 2018  Once the CTCL was shut off, the orders which were showing any of the pending states were lapsed and reconciled with the exchange. This affe

## q-164 (esperado: DAN-001)

- busca inicial: DAN-001, DAN-129, DAN-024, DAN-162, DAN-067, DAN-209, DAN-218, DAN-186, DAN-119, DAN-148
- justificativa: 
- aprofundar DAN-001: `cluster resource management configuration prevent starting instances available hardware fix` — O incidente atual é quase idêntico: campanha de marketing, pico de tráfego, site caiu e não era possível subir mais instâncias apesar de máquinas sobrando; DAN-001 descreve exatamente erro de configuração em gerenciamento de recursos de cluster impedindo novas instâncias com hardware disponível.
  - DAN-001 (llm) [Analysis #] 0.641: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (llm) [Outage timeline #] 0.628: ## Outage timeline #  The special offer was to start at noon sharp, and a direct link to its item page had been published before. At 11:15 we manually scaled out Listing service in order to be prepare
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa

## q-165 (esperado: DAN-001)

- busca inicial: DAN-001, DAN-129, DAN-218, DAN-210, DAN-148, DAN-067, DAN-208, DAN-220, DAN-209, DAN-073
- justificativa: 
- aprofundar DAN-001: `configuration error cluster resource management prevented starting instances traffic spike fix` — O incidente atual é quase idêntico: campanha de marketing, pico de tráfego, máquina sobrando e impossibilidade de iniciar novas instâncias do serviço; não há componente diferente.
- aprofundar DAN-148: `extreme load concurrent users service disruptions root cause fix` — Também envolve pico extremo de usuários simultâneos, mas não menciona campanha de marketing nem impedimento de iniciar instâncias com hardware disponível.
- aprofundar DAN-218: `network saturation traffic gateways scale up caused more issues fix` — Envolve tentativa de escalar que piorou a situação, mas a causa é saturação de rede na AWS, não erro de configuração de cluster que bloqueia novas instâncias.
  - DAN-001 (llm) [Outage timeline #] 0.688: ## Outage timeline #  Also just before noon, traffic peaked at 200%-300% of the traffic from previous day, depending on service. At this stage, traffic was at its highest but due to excessive resource
  - DAN-001 (llm) [Analysis #] 0.679: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa
  - DAN-148 (llm) [**XMPP outage**] 0.671: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (llm) [**Account Service outage**] 0.668: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme
  - DAN-218 (llm) [sem seção] 0.617: A little architectural background is needed here: Slack started life, not so many years ago, with everything running in one AWS account. As we’ve grown in size, complexity, and number of engineers we’
  - DAN-218 (llm) [sem seção] 0.61: Unfortunately, our scale-up did not work as intended. We run a service, aptly named ‘provision-service’, which does exactly what it says on the tin. It is responsible for configuring and testing new i
  - DAN-218 (causa) [sem seção] 0.469: Once provision-service was back in operation (around 8:15am PST) we began to see an improvement as healthy instances entered service. We still had some less-critical production issues which were mitig
  - DAN-218 (correcao) [sem seção] 0.391: AWS assures us that they are reviewing the TGW scaling algorithms for large packet-per-second increases as part of their post-incident process. We’ve also set ourselves a reminder (a Slack reminder, o
  - DAN-218 (correcao) [sem seção] 0.383: *And now we welcome the new year. Full of things that have never been.*  *— Rainer Maria Rilke*  January 4th 2021 was the first working day of the year for many around the globe, and for most of us at

## q-166 (esperado: DAN-003)

- busca inicial: DAN-003, DAN-092, DAN-103, DAN-164, DAN-134, DAN-133, DAN-180, DAN-195, DAN-102, DAN-056
- justificativa: 
- aprofundar DAN-003: `schema field type change job distribution rollback fix` — Mesmo gatilho (deploy de schema), mesmo componente (serviço de distribuição de jobs), mesmo sintoma (jobs parados e rollback não resolveu); difere no tipo exato de campo e na forma de recuperação.
- aprofundar DAN-092: `database upgrade statistics stale analyze rollback fix` — Mesmo padrão (deploy/upgrade de banco afeta jobs, rollback ou re-promove necessário); difere na causa (estatísticas desatualizadas vs incompatibilidade de schema) e componente (banco de workflows vs distribuidor de jobs).
- aprofundar DAN-134: `RabbitMQ upgrade consumer ack timeout rollback fix` — Mesmo padrão (upgrade de infraestrutura quebra distribuição/consumidores de jobs); difere no componente (RabbitMQ vs schema do banco) e na natureza da falha (timeout de ack vs validação de schema).
  - DAN-003 (llm) [What happened] 0.706: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.515: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s
  - DAN-092 (llm) [What Happened] 0.71: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [What Happened] 0.575: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (causa) [Summary] 0.393: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-092 (correcao) [Future Prevention and Process Improvement] 0.483: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-134 (llm) [Contributing Event:] 0.693: ## Contributing Event:  On May 20th, we upgraded RabbitMQ from 3.8.9 to 3.8.16 as part of routine upgrades. As usual, the team checked the changelog to ensure there were no breaking changes listed and
  - DAN-134 (llm) [What Happened] 0.591: ## What Happened  At this time there was confidence that the system was in a stable state and everyone dispersed to get some much-needed rest. This incident involved folks from EMEA and NA and came cl
  - DAN-134 (causa) [What Happened] 0.473: ## What Happened  The system had become “wedged” and we had found ourselves in a vicious cycle of creating VMs and then not being able to remove them due to hitting our GCP quotas. In order to break o
  - DAN-134 (correcao) [Resolution and future prevention:] 0.445: ## Resolution and future prevention:  This was a long-running incident with numerous follow-on effects. Remediation falls into two broad categories: detecting this specific failure sooner and improvin
  - DAN-134 (correcao) [What Happened] 0.404: ## What Happened  (all times UTC)  On the 20th of May at 08:37, CircleCI engineers performed routine maintenance on our RabbitMQ cluster and upgraded to version 3.8.16 from 3.8.9. The upgrade was succ

## q-167 (esperado: DAN-003)

- busca inicial: DAN-003, DAN-092, DAN-134, DAN-164, DAN-130, DAN-103, DAN-180, DAN-091, DAN-116, DAN-066
- justificativa: 
- aprofundar DAN-003: `database schema change job distribution rollback recovery fix` — O incidente envolve alteração de esquema de banco de dados após deploy, serviço de distribuição de jobs parou de distribuir trabalho, jobs ficaram presos e o rollback não resolveu — corresponde exatamente ao cenário atual.
- aprofundar DAN-092: `database upgrade statistics planner rollback re-promote recovery` — Envolve mudança de banco de dados após deploy com problemas na consulta/recuperação, mas a causa são estatísticas desatualizadas do planejador, não alteração de esquema que invalida linhas antigas.
  - DAN-003 (llm) [What happened] 0.695: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Background] 0.55: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.348: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-092 (llm) [What Happened] 0.608: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [What Happened] 0.53: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (causa) [Summary] 0.393: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-092 (correcao) [Future Prevention and Process Improvement] 0.483: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru

## q-168 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-066, DAN-008, DAN-050, DAN-129, DAN-067, DAN-211, DAN-020, DAN-016
- justificativa: 
- aprofundar DAN-017: `deployment staging build unauthorized endpoint HTTP 401 root cause fix` — Bate deploy como gatilho, 401 para todas as requisições e falha em cascata em produtos dependentes; difere por ser ambiente Cloudflare e referência a build de staging.
- aprofundar DAN-016: `newly deployed DDoS rule rate limiting cookie validation root cause fix` — Bate deploy recém-implantado causando falha generalizada no serviço; difere porque o sintoma é loop de CPU, não 401.
- aprofundar DAN-008: `Tiered Cache change requests fail 530 root cause fix` — Bate mudança de deploy causando falhas em requisições; difere porque o código de erro é 530, não 401, e não menciona cascata de produtos.
  - DAN-017 (llm) [What was impacted] 0.526: ### What was impacted  A number of Cloudflare services depend on Workers KV for distributing configuration, routing information, static asset serving, and authentication state globally. These services
  - DAN-017 (llm) [Analysis] 0.517: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (causa) [Timeline] 0.417: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Resolution] 0.424: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.716: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Remediation and follow-up steps] 0.711: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi
  - DAN-008 (llm) [sem seção] 0.785: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.672: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac

## q-169 (esperado: DAN-017)

- busca inicial: DAN-017, DAN-220, DAN-067, DAN-211, DAN-183, DAN-016, DAN-020, DAN-129, DAN-050, DAN-066
- justificativa: 
- aprofundar DAN-017: `deployment staging build unauthorized endpoint HTTP 401 root cause fix rollback` — Bate deploy seguido de HTTP 401 e falha em cascata em produtos dependentes; não confirma se o componente é o mesmo core service.
- aprofundar DAN-050: `deployment bug download URL generation broken crate downloads fix rollback` — Bate deploy com bug gerando URLs incorretas, mas não há HTTP 401 nem serviço core retornando erro de autenticação.
- aprofundar DAN-016: `deployed DDoS rule cookie validation infinite loop CPU fix rollback` — Bate deploy novo expondo bug latente, mas sintoma é loop de CPU e validação de cookie, não 401 em todas as requisições.
  - DAN-017 (llm) [Analysis] 0.553: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (llm) [Timeline] 0.531: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.
  - DAN-050 (llm) [Recovery] 0.794: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Summary] 0.775: ## Summary  On 2023-07-20 between 12:17 and 12:30 UTC all crate downloads from crates.io were broken due to a deployment that contained a bug in the download URL generation.  During this time we had a
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi
  - DAN-016 (llm) [Remediation and follow-up steps] 0.718: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.716: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-016 (correcao) [Technical description of the error and how it happened] 0.48: ## Technical description of the error and how it happened  It was 25 minutes after the initial incident was declared when we validated that restarts helped on one sample server. Five minutes after thi

## q-170 (esperado: DAN-018)

- busca inicial: DAN-144, DAN-066, DAN-017, DAN-018, DAN-029, DAN-191, DAN-102, DAN-037, DAN-067, DAN-154
- justificativa: 
- aprofundar DAN-018: `dashboard excessive API calls tenant service dependency array fix` — O dashboard fazendo excessivas chamadas para um serviço interno após mudança no frontend bate com o incidente atual, que também envolve painel sobrecarregando serviço interno depois de deploy frontend.
- aprofundar DAN-144: `thundering herd reconnecting frontend internal queues memory fix` — Tem thundering herd e impacto em filas internas do frontend, mas o gatilho é recuperação de serviço flapping, não deploy do frontend nem chamadas vindas do painel.
- aprofundar DAN-067: `thundering herd API calls overwhelmed services rate limits fix` — Tem chamadas de API overwhelming services e correção com rate limits, mas o gatilho é falha de energia, não deploy frontend nem painel como origem das chamadas.
  - DAN-018 (llm) [What Happened] 0.73: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Reducing impact] 0.695: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [Improving visibility] 0.408: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-144 (llm) [Summary] 0.513: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (llm) [Investigation and Analysis] 0.496: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 
  - DAN-067 (llm) [Disaster Recovery] 0.657: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.515: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 

## q-171 (esperado: DAN-018)

- busca inicial: DAN-066, DAN-144, DAN-029, DAN-018, DAN-067, DAN-133, DAN-129, DAN-218, DAN-145, DAN-220
- justificativa: 
- aprofundar DAN-018: `React component bug dashboard excessive API calls dependency array fix` — O painel gerou excesso de chamadas à API após deploy frontend, igual ao incidente atual, embora a causa seja um bug de componente React e não especificamente inundação de serviço interno.
- aprofundar DAN-067: `thundering herd API calls overwhelmed services rate limits fix` — Possui problema de thundering herd onde chamadas de API sobrecarregaram serviços e o corretivo foi limitar taxa, semelhante à inundação, mas o disparo foi falha de datacenter, não deploy frontend.
- aprofundar DAN-066: `Byzantine failure switch misbehavior API dashboard cascade fix` — Causou indisponibilidade de API e painel por falha em cascata, mas a origem foi comportamento parcial de switch, não chamadas vindas do painel após deploy.
  - DAN-018 (llm) [What Happened] 0.679: ## What Happened  We had an outage in our Tenant Service API which led to a broad outage of many of our APIs and the Cloudflare Dashboard.  The incident’s impact stemmed from several issues, but the i
  - DAN-018 (llm) [Improving visibility] 0.647: ### Improving visibility  We immediately saw an increase in our API usage but found it difficult to identify which requests were retries vs new requests. Had we known that we were seeing a sustained l
  - DAN-018 (causa) [Going forward] 0.407: ## Going forward  We believe it’s important to learn from our mistakes and this incident is an opportunity to make some improvements. Those improvements can be categorized as either ways to reduce / e
  - DAN-018 (correcao) [How we responded] 0.457: ## How we responded  Our first goal in an incident is to restore service. Often that involves fixing the underlying issue directly, but not always. In this case we noticed increased usage across our T
  - DAN-018 (correcao) [Reducing impact] 0.409: ### Reducing impact  We use Argo Rollouts for releasing, which monitors deployments for errors and automatically rolls back that service on a detected error. We’ve been migrating our services over to 
  - DAN-067 (llm) [Disaster Recovery] 0.657: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.515: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 
  - DAN-066 (llm) [The Dashboard] 0.618: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.599: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.463: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain

## q-172 (esperado: DAN-020)

- busca inicial: DAN-020, DAN-220, DAN-205, DAN-066, DAN-109, DAN-145, DAN-222, DAN-067, DAN-113, DAN-144
- justificativa: 
- aprofundar DAN-020: `service discovery client config global outage root cause fix` — O resumo descreve exatamente o mesmo padrão: service discovery caiu globalmente quando um cliente dependente caiu, devido a uma configuração ruim de service discovery nesse cliente. Não bate apenas no detalhe de que o incidente atual menciona 'todas as regiões' enquanto o resumo diz 'globalmente', mas o mecanismo é o mesmo.
  - DAN-020 (llm) [The failure of a core system] 0.698: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.68: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter

## q-173 (esperado: DAN-020)

- busca inicial: DAN-020, DAN-220, DAN-066, DAN-145, DAN-109, DAN-205, DAN-211, DAN-067, DAN-222, DAN-208
- justificativa: 
- aprofundar DAN-020: `service discovery bad client config global outage cause fix` — Bate exatamente: descoberta de serviço caiu globalmente quando um cliente dependente caiu; difere apenas o ator (cliente vs serviço) e o provedor.
- aprofundar DAN-211: `Consul streaming BoltDB service discovery degradation root cause fix` — Envolve Consul e degradação de descoberta de serviço, mas o gatilho foi remoção de bloqueio iptables, não queda de cliente dependente.
- aprofundar DAN-222: `Cassandra cluster crash producers blocking queue insert outage fix` — Falha em cascata de cluster que derruba producers, mas o componente é Cassandra, não serviço de descoberta.
  - DAN-020 (llm) [The failure of a core system] 0.674: ## The failure of a core system  The incident was caused by the failure of an internal service discovery and dynamic configuration system that the vast majority of Datadog software components rely on.
  - DAN-020 (llm) [Improve the resilience of service discovery] 0.663: ## Improve the resilience of service discovery  The need to register and deregister services won’t go away but we must support it with a system that is not a single point of failure (be it distributed
  - DAN-020 (causa) [How do we avoid it in the future?] 0.506: ## How do we avoid it in the future?  Post-incident, all engineering teams have been involved in forensic investigations in order to understand in depth what happened and summarize all the findings in
  - DAN-020 (correcao) [Improve our external response] 0.48: ## Improve our external response  It starts with having a dedicated role with clear processes to disseminate updates about high visibility incidents throughout. It also includes having clearer communi
  - DAN-020 (correcao) [Internal response and recovery] 0.393: ## Internal response and recovery  A few minutes after the intake cluster started to show intermittent failures and roughly 20 minutes before we publicly declared an incident, teams triggered an inter
  - DAN-211 (llm) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.688: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  But what was going on with the slow leaders? We did not figure this out during the incident, but HashiCorp engineers determined the root cause in the
  - DAN-211 (llm) [Outage Summary] 0.683: ### Outage Summary  The outage was unique in both duration and complexity. The team had to address a number of challenges in sequence to understand the root cause and bring the service back up.  - The
  - DAN-211 (causa) [Root Causes Found (10/30 12:00 – 10/30 20:00)] 0.503: ### Root Causes Found (10/30 12:00 – 10/30 20:00)  Several months ago, we enabled a new Consul streaming feature on a subset of our services. This feature, designed to lower the CPU usage and network 
  - DAN-211 (correcao) [Recent Improvements and Future Steps] 0.474: ### Recent Improvements and Future Steps  It has been 2.5 months since the outage. What have we been up to? We used this time to learn as much as we could from the outage, to adjust engineering priori
  - DAN-211 (correcao) [Telemetry Improvements] 0.455: #### Telemetry Improvements  There was a circular dependency between our telemetry systems and Consul, which meant that when Consul was unhealthy, we lacked the telemetry data that would have made it 
  - DAN-222 (llm) [sem seção] 0.689: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (llm) [sem seção] 0.669: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (causa) [sem seção] 0.457: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (correcao) [sem seção] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl

## q-174 (esperado: DAN-022)

- busca inicial: DAN-022, DAN-065, DAN-059, DAN-113, DAN-159, DAN-129, DAN-007, DAN-006, DAN-209, DAN-068
- justificativa: 
- aprofundar DAN-022: `multicast traffic switch configuration root cause fix outage` — O incidente envolve tráfego multicast causando uma queda global, exatamente como o incidente atual; busca-se a causa raiz e correção detalhadas dentro desse post-mortem.
  - DAN-022 (llm) [Multicast Rsync?] 0.566: ### Multicast Rsync?  If we need to get the same bits to all of the boxes, why not send the index via multicast to the replicas? It sure would be nice to only send the data once. We found an implement
  - DAN-022 (llm) [The Index Replication Issue] 0.36: ### The Index Replication Issue  To keep all of the searches on our site working fast we optimize our indexes nightly. Index optimization creates a completely new copy of the index. As we added new bo
  - DAN-022 (causa) [Search at Etsy] 0.27: ### Search at Etsy  Search at Etsy has grown significantly over the years. In January of 2009 we started using Solr for search. We used the standard primary-replica configuration for our search server
  - DAN-022 (correcao) [Improvements] 0.279: ### Improvements  To better deal with the transfer lag we are looking at creating a Torrent file per index segment. Lucene indexes are made up of various segments. Each commit creates an index segment
  - DAN-022 (correcao) [How it Works] 0.273: ### How it Works  HTTP replication doesn’t allow for the transfer of older versions of a given index. This causes issues with some of our static indexes. When we bring up new replicas, Solr creates a 

## q-175 (esperado: DAN-022)

- busca inicial: DAN-022, DAN-159, DAN-077, DAN-113, DAN-059, DAN-209, DAN-078, DAN-109, DAN-148, DAN-006
- justificativa: 
- aprofundar DAN-022: `multicast traffic switch configuration root cause outage fix` — É o único que descreve tráfego multicast causando queda global de rede, exatamente como o incidente atual; os outros envolvem BGP, falhas de link, bugs de SO ou sobrecarga, não multicast.
  - DAN-022 (llm) [Multicast Rsync?] 0.565: ### Multicast Rsync?  If we need to get the same bits to all of the boxes, why not send the index via multicast to the replicas? It sure would be nice to only send the data once. We found an implement
  - DAN-022 (llm) [The Index Replication Issue] 0.362: ### The Index Replication Issue  To keep all of the searches on our site working fast we optimize our indexes nightly. Index optimization creates a completely new copy of the index. As we added new bo
  - DAN-022 (causa) [Search at Etsy] 0.27: ### Search at Etsy  Search at Etsy has grown significantly over the years. In January of 2009 we started using Solr for search. We used the standard primary-replica configuration for our search server
  - DAN-022 (correcao) [Improvements] 0.279: ### Improvements  To better deal with the transfer lag we are looking at creating a Torrent file per index segment. Lucene indexes are made up of various segments. Each commit creates an index segment
  - DAN-022 (correcao) [How it Works] 0.273: ### How it Works  HTTP replication doesn’t allow for the transfer of older versions of a given index. This causes issues with some of our static indexes. When we bring up new replicas, Solr creates a 

## q-176 (esperado: DAN-026)

- busca inicial: DAN-026, DAN-020, DAN-010, DAN-162, DAN-087, DAN-137, DAN-049, DAN-075, DAN-002, DAN-065
- justificativa: 
- aprofundar DAN-026: `IP change DNS timeout NXDOMAIN zone file corrupt fix` — Escolhi porque é o único que combina troca de IP, timeouts de DNS e NXDOMAIN em muitos registros, exatamente como o incidente atual.
- aprofundar DAN-075: `DNS management race condition empty stale record fix` — Escolhi porque envolve registros DNS vazios ou estaleiros após mudanças de gerenciamento, embora não mencione troca de IP nem timeouts iniciais.
- aprofundar DAN-002: `DNS resolver fleet config change query failure fix` — Escolhi porque descreve falha de consultas DNS após mudança de configuração do resolvedor, mas sem troca de IP nem NXDOMAIN explícito.
  - DAN-026 (llm) [What happened…] 0.756: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.666: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-075 (llm) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.61: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  The race condition involves an unlikely interaction between two of the DNS Enactors. Under normal oper
  - DAN-075 (llm) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.581: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  Second, one of the other DNS Enactors then began applying one of the newer plans and rapidly progresse
  - DAN-075 (causa) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.365: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  At 2:25 AM PDT, with the recovery of the DynamoDB APIs, DWFM began to re-establish leases with droplet
  - DAN-075 (correcao) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.384: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. We have already disabled the Dyna
  - DAN-075 (correcao) [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.347: ## Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region  When this issue occurred at 11:48 PM PDT, all systems needing to connect to the DynamoDB service in th
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.584: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We are taking multiple steps to prevent recurrence of this issue, some of which are already comp
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.579: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We’d like to give you some additional information about the service disruption that occurred in 

## q-177 (esperado: DAN-026)

- busca inicial: DAN-026, DAN-020, DAN-087, DAN-162, DAN-075, DAN-010, DAN-049, DAN-137, DAN-081, DAN-002
- justificativa: 
- aprofundar DAN-026: `IP change authoritative nameserver restart zone rebuild NXDOMAIN remediation` — É o mais parecido: IP change causou timeouts DNS e NXDOMAIN em muitos nomes, exatamente como o incidente atual.
- aprofundar DAN-002: `DNS resolver fleet config change minimum healthy hosts remediation` — Bate com falha de resolução DNS após mudança de configuração, mas não com IP change nem NXDOMAIN.
- aprofundar DAN-162: `database migration DNS resolution break cascading recovery temporary resolvers` — Bate com resolução DNS quebrada após mudança e impacto em cascata, mas não com IP change nem NXDOMAIN.
  - DAN-026 (llm) [What happened…] 0.743: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.634: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.577: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We’d like to give you some additional information about the service disruption that occurred in 
  - DAN-002 (llm) [Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)] 0.575: ## Summary of the Amazon EC2 DNS Resolution Issues in the Asia Pacific (Seoul) Region (AP-NORTHEAST-2)  We are taking multiple steps to prevent recurrence of this issue, some of which are already comp
  - DAN-162 (llm) [sem seção] 0.537: In October, we experienced one incident that resulted in degraded performance across GitHub services.  **October 11 05:59 UTC (lasting 19 hours and 12 minutes)**  On October 11, 2024, starting at 05:5

## q-178 (esperado: DAN-033)

- busca inicial: DAN-033, DAN-191, DAN-221, DAN-205, DAN-195, DAN-222, DAN-165, DAN-161, DAN-231, DAN-106
- justificativa: 
- aprofundar DAN-033: `quota service bad config failure root cause fix gmail` — O resumo diz que uma configuração ruim fez o serviço de quota falhar e derrubar múltiplos serviços incluindo o Gmail — idêntico ao incidente atual (quota → e-mail e outros serviços). Não bate no produto (Chromium/Google), mas o padrão de falha é o mesmo.
  - DAN-033 (llm) [sem seção] 0.533: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fre
  - DAN-033 (llm) [sem seção] 0.483: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  - B
  - DAN-033 (causa) [sem seção] 0.294: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  .cc
  - DAN-033 (correcao) [sem seção] 0.262: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  enu
  - DAN-033 (correcao) [sem seção] 0.248: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fie

## q-179 (esperado: DAN-033)

- busca inicial: DAN-033, DAN-191, DAN-218, DAN-147, DAN-144, DAN-220, DAN-148, DAN-205, DAN-221, DAN-109
- justificativa: 
- aprofundar DAN-033: `quota service bad config multiple services email fix recovery` — O resumo cita exatamente falha no serviço de quota derrubando vários serviços incluindo o Gmail, igual ao incidente atual; sem indicação de componente diferente.
  - DAN-033 (llm) [sem seção] 0.46: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fre
  - DAN-033 (llm) [sem seção] 0.398: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  - B
  - DAN-033 (causa) [sem seção] 0.294: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  .cc
  - DAN-033 (correcao) [sem seção] 0.262: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  enu
  - DAN-033 (correcao) [sem seção] 0.248: chromium -    Incorrect SyncDataType parsing for throttled types causes chrome to crash -   An open-source project to help move the web forward. - Google Project Hosting | Category: Config Errors  Fie

## q-180 (esperado: DAN-042)

- busca inicial: DAN-042, DAN-035, DAN-049, DAN-032, DAN-015, DAN-020, DAN-033, DAN-048, DAN-029, DAN-017
- justificativa: 
- aprofundar DAN-042: `deployment config variables missing new code required fix` — Bate: deploy onde novas variáveis de configuração não são usadas pelo código novo. Não bate: pode ser processo de deploy incorreto e não ausência direta da variável nas instâncias.
- aprofundar DAN-015: `deploy credentials wrong environment omitted flag fix` — Bate: deploy com erro de ambiente/configuração (flag --env omitida) quebrando autenticação. Não bate: credenciais de storage, não variável de configuração ausente esperada pelo código.
- aprofundar DAN-035: `configuration rollout unable read config files fix` — Bate: rollout de configuração falhando e código não conseguindo ler configs recentes. Não bate: load balancer e servidor mestre, não variável ausente nas instâncias.
  - DAN-042 (llm) [It was such a nice morning] 0.661: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Did I mess up?] 0.618: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Houston, we have a problem] 0.312: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-015 (llm) [Incident timeline] 0.64: ## Incident timeline  **All timestamps referenced are in Coordinated Universal Time (UTC).**  | Time | Event | |---|---| | Mar 21, 2025 - 19:49 UTC | The R2 engineering team started the credential rot
  - DAN-015 (llm) [Incident timeline] 0.608: ## Incident timeline  Given gradual decline in availability metrics, R2 engineering team suspected a potential regression in propagation of new credentials in storage infrastructure. | | Mar 21, 2025 
  - DAN-015 (causa) [Next steps] 0.493: ## Next steps  The list above is not exhaustive: as we work through the above items, we will likely uncover other improvements to our systems, controls, and processes that we’ll be applying to improve
  - DAN-015 (correcao) [Resolution] 0.484: ## Resolution  Once we identified the root cause, we were able to resolve the incident quickly by deploying the new credentials to the production R2 Gateway Worker. This resulted in an immediate recov
  - DAN-015 (correcao) [Next steps] 0.468: ## Next steps  This incident happened because of human error and lasted longer than it should have because we didn’t have proper visibility into which credentials were being used by the R2 Gateway Wor
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.605: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.585: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.405: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo

## q-181 (esperado: DAN-042)

- busca inicial: DAN-042, DAN-035, DAN-220, DAN-020, DAN-049, DAN-029, DAN-154, DAN-050, DAN-102, DAN-055
- justificativa: 
- aprofundar DAN-042: `deploy new code missing config variable required fix rollback` — é o único que combina deploy com variáveis de configuração que o novo código exige mas não estão sendo usadas, exatamente como o incidente atual.
- aprofundar DAN-035: `configuration roll-out load balancer bug fix rollback` — envolve falha na propagação de configuração após alteração, embora o componente seja um load balancer e não instâncias de serviço.
- aprofundar DAN-055: `configuration change builds fail manual rollback broke fix` — uma mudança de configuração que quebrou builds em produção, mas sem relação direta com variável ausente após deploy.
  - DAN-042 (llm) [It was such a nice morning] 0.647: ## It was such a nice morning  On September 3, I had to deploy a change to switch from calling one internal API endpoint to another. It included a new authentication method between components.  This d
  - DAN-042 (llm) [Did I mess up?] 0.636: ## Did I mess up?  An untrained eye could say “wow, you messed up bad. Why didn’t you run that command?”, and they would be right. Except they actually wouldn’t.  The problem isn’t that I forgot to ru
  - DAN-042 (causa) [Computers are dumb, but they don’t make mistakes] 0.413: ## Computers are dumb, but they don’t make mistakes  Relying on humans to perform multiple manual actions, especially when some of them are only required rarely (we don’t change configuration variable
  - DAN-042 (correcao) [How I Broke `git push heroku main`] 0.399: ## How I Broke `git push heroku main`  Posted By  Damien Mathieu  - Last Updated: October 01, 2020  Incidents are inevitable. Any platform, large or small will have them. While resiliency work will de
  - DAN-042 (correcao) [Houston, we have a problem] 0.312: ## Houston, we have a problem  I started my production deployment. Since I had set the configuration variable earlier, I went straight to deploying the new code.  You may see what I did wrong now.  So
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.75: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.738: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.36: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration
  - DAN-055 (llm) [So what happened?] 0.585: ## So what happened?  Thursday Feb 2nd, we started rolling out a new worker version (v2.6.2) on EC2, for sudo: false, container-based builds.  Friday Feb 3rd, we identified an issue with jobs being in
  - DAN-055 (llm) [So what happened?] 0.55: ## So what happened?  We also learned we did not have alerting which included the errors logged when the image pulls were failing to find v2.5.0.  Sunday, Feb 5th, in order to more quickly eliminate t
  - DAN-055 (causa) [Contributing Factors] 0.437: ## Contributing Factors  The major contributing factors in this outage were  - A change in how our worker's docker backend executes build scripts, so that bash is run explicitly with a login shell. Th
  - DAN-055 (correcao) [Going forward?] 0.437: ## Going forward?  - As part of the incident resolution, we created additional alerting, so that we know we'll be notified about similar errors in the future.  - We are discussing both incremental and
  - DAN-055 (correcao) [Summary] 0.424: ## Summary  We couldn't be more sorry about this incident and the impact that the build outages and delays had on you, our users and customers. We always use problems like these as an opportunity for 

## q-182 (esperado: DAN-043)

- busca inicial: DAN-043, DAN-146, DAN-056, DAN-164, DAN-048, DAN-210, DAN-186, DAN-058, DAN-066, DAN-209
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion backup recovery fix` — Bate diretamente: banco de produção deletado por acidente com backup antigo e perda de horas de dados, igual ao incidente atual. Não bate: backup diário vs backup de horas atrás.
- aprofundar DAN-164: `accidental wrong directory deletion database recovery fix` — Bate: administrador deletou o diretório errado do banco, perdendo horas de dados. Não bate: foi um diretório, não o banco inteiro.
- aprofundar DAN-056: `accidental environment variable truncate production database recovery fix` — Bate: ação acidental causou perda/dano no banco de produção. Não bate: mecanismo foi variável de ambiente que truncou, não delete direto.
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.734: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.661: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [Timeline] 0.617: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (llm) [Root cause analysis] 0.613: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.732: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.715: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-183 (esperado: DAN-043)

- busca inicial: DAN-043, DAN-164, DAN-056, DAN-186, DAN-146, DAN-091, DAN-058, DAN-066, DAN-048, DAN-210
- justificativa: 
- aprofundar DAN-043: `accidental production database deletion backup recovery fix` — Mesmo acidente: banco de produção deletado e backup com horas de atraso, causando perda permanente de dados.
- aprofundar DAN-164: `wrong directory deleted database replication lag recovery` — Mesma causa raiz humana: exclusão acidental de dados críticos com perda de horas, mas com gatilho de sobrecarga de replicação.
- aprofundar DAN-056: `environment variable truncate production database accidental fix` — Mesmo padrão: comando acidental destruiu banco de produção, diferindo no mecanismo (variável de ambiente em testes).
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.734: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.661: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-164 (llm) [Timeline] 0.713: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (llm) [Root cause analysis] 0.704: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-056 (llm) [What We Learned] 0.729: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.711: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-184 (esperado: DAN-048)

- busca inicial: DAN-048, DAN-066, DAN-078, DAN-195, DAN-209, DAN-164, DAN-234, DAN-043, DAN-190, DAN-146
- justificativa: 
- aprofundar DAN-048: `RDS hardware failure MySQL failover data loss configuration fix` — Bate por falha de hardware, failover MySQL e perda de dados em sistema financeiro; não bate se o ambiente gerenciado for diferente da AWS RDS.
- aprofundar DAN-078: `MySQL master failover missing writes latency data integrity restoration` — Bate por failover MySQL com transações recentes ausentes no novo mestre; não bate porque o gatilho foi particionamento de rede, não falha de hardware.
  - DAN-048 (llm) [Incorrect configuration variable] 0.787: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (llm) [Final thoughts] 0.761: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.684: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [Next steps] 0.678: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (causa) [Incident timeline] 0.478: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-078 (correcao) [2018 October 22 16:24 UTC] 0.479: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 

## q-185 (esperado: DAN-048)

- busca inicial: DAN-048, DAN-066, DAN-078, DAN-164, DAN-043, DAN-181, DAN-094, DAN-093, DAN-096, DAN-190
- justificativa: 
- aprofundar DAN-048: `RDS hardware failure MySQL configuration data loss failover fix` — Bate por falha de hardware, failover e perda de dados em sistema financeiro; não bate por ser RDS específico com configuração incorreta.
- aprofundar DAN-078: `MySQL master failover missing writes latency restoration fix` — Bate por failover do MySQL master com writes não propagados após falha; não bate por ser partição de rede durante manutenção.
- aprofundar DAN-093: `failover stale node data drift Pacemaker fix` — Bate por failover para nó desatualizado com drift de dados; não bate por ser trigger de migração de schema/Pacemaker.
  - DAN-048 (llm) [Incorrect configuration variable] 0.792: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (llm) [Final thoughts] 0.763: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.656: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (llm) [Next steps] 0.632: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (causa) [Incident timeline] 0.478: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-078 (correcao) [2018 October 22 16:24 UTC] 0.479: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 
  - DAN-093 (llm) [Tuesday, September 11th] 0.64: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (llm) [Monday, September 10th] 0.566: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member

## q-186 (esperado: DAN-049)

- busca inicial: DAN-049, DAN-073, DAN-026, DAN-109, DAN-162, DAN-050, DAN-208, DAN-024, DAN-129, DAN-164
- justificativa: 
- aprofundar DAN-049: `static domain DNS resolution failure deployment root cause fix` — Bate por ser um deploy de infra que quebrou DNS de domínio de arquivos estáticos (static.crates.io), exatamente como o incidente atual.
- aprofundar DAN-026: `DNS outage deployment root cause fix zone file` — Também envolve DNS e deploy, mas o mecanismo é diferente (Puppet/nameserver), então serve como contraste.
- aprofundar DAN-050: `deployment bug download URL generation root cause fix` — Envolve downloads quebrados por deploy, mas por geração de URL, não por falha de resolução de domínio.
  - DAN-049 (llm) [Resolution] 0.699: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (llm) [sem seção] 0.641: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat
  - DAN-049 (causa) [Postmortem] 0.443: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [Root Cause of the Outage] 0.373: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-026 (llm) [What happened…] 0.739: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [Total number of processes across fileservers] 0.709: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (causa) [What we’re doing about it…] 0.461: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [Summary] 0.443: # Summary  We realize that GitHub is an important part of your development and workflow. Again, I would like to take a moment to apologize for the impact that this outage had to your operations. We ta
  - DAN-050 (llm) [Recovery] 0.674: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Summary] 0.64: ## Summary  On 2023-07-20 between 12:17 and 12:30 UTC all crate downloads from crates.io were broken due to a deployment that contained a bug in the download URL generation.  During this time we had a
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi

## q-187 (esperado: DAN-049)

- busca inicial: DAN-049, DAN-026, DAN-020, DAN-162, DAN-050, DAN-210, DAN-073, DAN-010, DAN-129, DAN-208
- justificativa: 
- aprofundar DAN-049: `static.crates.io DNS record failed resolve deployment certificates DNS records recreated` — Bate com o atual: deploy de infraestrutura derrubou resolução DNS de domínio de static files (static.crates.io) e quebrou downloads; não bate na causa exata (recriação de certificados e registros DNS durante o downtime).
- aprofundar DAN-026: `authoritative nameserver restart zone file corrupt NXDOMAIN provisioning API DNS` — Bate: resolução DNS quebrada durante operação de infraestrutura com zone file corrompido; não bate: gatilho é bug no Puppet e mudança de IP, não deploy de domínio de static files.
- aprofundar DAN-050: `download URL generation bug crate downloads broken deployment fix` — Bate: downloads quebrados durante um deployment no crates.io; não bate: causa é bug na geração de URL de download, não falha de resolução DNS do domínio de static files.
  - DAN-049 (llm) [Resolution] 0.745: ## Resolution  The outage resolved itself after Terraform finished the deployment and created a new DNS record for `static.crates.io`. For some users, the outage lasted a few minutes longer due to cac
  - DAN-049 (llm) [Root Cause of the Outage] 0.713: ## Root Cause of the Outage  The Rust infrastructure is managed with Terraform, a tool to configure and provision infrastructure-as-code. The Infrastructure team recently made changes to this configur
  - DAN-049 (causa) [Postmortem] 0.443: ## Postmortem  The outage could have been avoided by deploying the changes to the TLS certificate and DNS records individually. We have identified two reasons why this did not happen as well as lesson
  - DAN-049 (correcao) [Postmortem] 0.453: ## Postmortem  - We need to document the process of deploying changes to production, in particular how to pick the Git commit and how to review the changeset. Defining a process will enable us to iter
  - DAN-049 (correcao) [sem seção] 0.341: On Wednesday, 2023-01-25 at 09:15 UTC, we deployed changes to the production infrastructure for crates.io. During the deployment, the DNS record for `static.crates.io` failed to resolve for an estimat
  - DAN-026 (llm) [What happened…] 0.754: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (llm) [What happened…] 0.618: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto
  - DAN-050 (llm) [Summary] 0.744: ## Summary  On 2023-07-20 between 12:17 and 12:30 UTC all crate downloads from crates.io were broken due to a deployment that contained a bug in the download URL generation.  During this time we had a
  - DAN-050 (llm) [Recovery] 0.744: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi

## q-188 (esperado: DAN-050)

- busca inicial: DAN-050, DAN-106, DAN-116, DAN-035, DAN-220, DAN-148, DAN-129, DAN-191, DAN-017, DAN-003
- justificativa: 
- aprofundar DAN-050: `deployment bug download URL generation crate download fix rollback` — É o único que bate exatamente: um deploy introduziu bug na geração de URL de download, quebrando todos os downloads de pacotes (crates) e gerando retries do cargo, igual ao incidente atual.
- aprofundar DAN-017: `deployment tool bug staging build 401 error fix rollback` — Também é um deploy que causou falha generalizada em produção, mas o componente é roteamento de tráfego/endpoint não autorizado, não downloads de pacotes.
- aprofundar DAN-003: `deploy database field type change rollback recovery fix` — Um deploy mudou o esquema e quebrou um serviço crítico, com rollback insuficiente, mas não envolve downloads de pacotes nem retries de clientes.
  - DAN-050 (llm) [Recovery] 0.78: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Response] 0.75: ## Response  After the incident was detected, the deploying developer immediately initiated a rollback to the previous deployment through the Heroku user interface. This process took about one minute 
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi
  - DAN-017 (llm) [Timeline] 0.593: ### Timeline  *All timestamps referenced are in Coordinated Universal Time (UTC).*  | Time | Description | |---|---| | 2023-10-30 18:58 UTC | The Workers KV team began a progressive deployment of a ne
  - DAN-017 (llm) [Analysis] 0.589: ### Analysis  Although automated alerting detected the issue immediately, there was a delay between the time we realized we were having an issue and the time we were actually able to perform the roll 
  - DAN-017 (causa) [Resolution] 0.416: ### Resolution  Cloudflare engineers manually switched (via break glass mechanism) the production route to the previous working version of Workers KV, which immediately eliminated the failing request 
  - DAN-017 (correcao) [Next steps] 0.455: ### Next steps  As more teams at Cloudflare have built on Workers, we have "organically" ended up in a place where Workers KV now underpins a tremendous amount of our products and services. This incid
  - DAN-017 (correcao) [Timeline] 0.394: ### Timeline  This was caused by the fact that multiple tools within Cloudflare rely on Workers KV including Cloudflare Access. Access leverages Workers KV as part of its request verification process.
  - DAN-003 (llm) [What happened] 0.623: ## What happened  All times are UTC.  At 18:50, we rolled out a deploy to change a field type in our distribution database. Incoming work received data of the new type, and any work from before the de
  - DAN-003 (llm) [Incident Report: November 8, 2021 - Jobs stuck in a “not running” state] 0.436: ## Incident Report: November 8, 2021 - Jobs stuck in a “not running” state  ## Summary  Customer jobs were blocked in a “not running” state from approximately 18:50 UTC to 19:43 UTC on Monday, Novembe
  - DAN-003 (causa) [Future prevention] 0.418: ## Future prevention  We’re making efforts in three places: preventing an identical incident, limiting impact for similar failures, and ensuring faster recovery when unforeseen failures occur.  To pre
  - DAN-003 (correcao) [Background] 0.371: ## Background  All work coming into CircleCI’s execution platform flows through a distribution service that accepts requests to run a discrete task and moves that task to the appropriate queue. This s

## q-189 (esperado: DAN-050)

- busca inicial: DAN-050, DAN-220, DAN-116, DAN-106, DAN-035, DAN-183, DAN-113, DAN-003, DAN-129, DAN-001
- justificativa: 
- aprofundar DAN-050: `deployment bug download URL generation broken crate downloads fix rollback` — Pacotes pararam de baixar logo após um deploy por causa de bug na geração de URL de download, batendo com falha de download de pacotes após deploy e retry de clientes; difere por ser crates.io/cargo.
- aprofundar DAN-035: `configuration roll-out load balancer bug root cause fix error rate` — Rollout de configuração causou explosão de taxa de erro, semelhante ao deploy que dispara erro generalizado; difere por afetar load balancer, não downloads de pacotes.
  - DAN-050 (llm) [Recovery] 0.794: ## Recovery  After rolling back to the previous deployment the system immediately recovered itself and produced correct redirect URLs again.  A fix for the broken pull request was subsequently develop
  - DAN-050 (llm) [Summary] 0.775: ## Summary  On 2023-07-20 between 12:17 and 12:30 UTC all crate downloads from crates.io were broken due to a deployment that contained a bug in the download URL generation.  During this time we had a
  - DAN-050 (causa) [Root cause identification: The Five Whys] 0.489: ## Root cause identification: The Five Whys  - The redirect URLs for crate and readme downloads were broken in production.   - **Why were the redirect URLs broken?** There was a bug introduced in pull
  - DAN-050 (correcao) [Lessons learned] 0.456: ## Lessons learned  - The detection time from deployment to incident notification could have been faster if the symptom was identified earlier to be caused by the cargo retry behavior. The heightened 
  - DAN-050 (correcao) [Corrective actions] 0.35: ## Corrective actions  - **HIGH** Include crate downloads in the smoke test plan for the staging environment - **MEDIUM** Automate the staging environment smoke tests - **MEDIUM** Develop rules on whi
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.786: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.732: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.36: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration

## q-190 (esperado: DAN-058)

- busca inicial: DAN-175, DAN-058, DAN-204, DAN-131, DAN-048, DAN-164, DAN-231, DAN-056, DAN-203, DAN-043
- justificativa: 
- aprofundar DAN-058: `free tier database backup identifier misconfiguration data leak fix` — É o único que envolve bancos de dados do plano gratuito com vazamento de dados entre clientes, mas não confirma se o vazamento ocorre dentro do próprio banco do cliente.
- aprofundar DAN-204: `Redis corrupted queues cross user data leak fix` — Envolve vazamento de dados de um usuário para outro, mas em cache de requisições, não em bancos de dados próprios de clientes gratuitos.
- aprofundar DAN-175: `private token leak customer account data access fix` — Envolve acesso indevido a dados de contas de clientes, mas por vazamento de token de atacante, não por falha de isolamento multitenant em banco gratuito.
  - DAN-058 (llm) [What happened?] 0.82: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.775: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-204 (llm) [Actions we’ve taken] 0.618: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (llm) [Technical details] 0.61: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-175 (llm) [Incident Summary] 0.61: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.554: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-191 (esperado: DAN-058)

- busca inicial: DAN-058, DAN-175, DAN-164, DAN-204, DAN-231, DAN-141, DAN-006, DAN-048, DAN-056, DAN-043
- justificativa: 
- aprofundar DAN-058: `free tier database backup identifier misconfiguration data leak fix` — É o mais parecido: mesmo cenário de clientes da camada gratuita vendo dados alheios, embora a causa seja identificadores de backup mal configurados, não o próprio banco.
- aprofundar DAN-204: `Redis cache queue corrupted out of sequence cross user data fix` — Também envolve dados de um usuário expostos a outro, mas por filas Redis corrompidas, não por bancos de clientes gratuitos.
- aprofundar DAN-175: `private token leak attacker customer data access root cause fix` — Envolve acesso indevido a dados de clientes via tokens vazados, mas por atacantes e não por exibição acidental entre clientes no próprio banco.
  - DAN-058 (llm) [What happened?] 0.82: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.775: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-204 (llm) [Technical details] 0.647: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.61: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-175 (llm) [Incident Summary] 0.609: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.574: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-192 (esperado: DAN-059)

- busca inicial: DAN-007, DAN-059, DAN-159, DAN-022, DAN-006, DAN-154, DAN-106, DAN-209, DAN-113, DAN-005
- justificativa: 
- aprofundar DAN-059: `BGP configuration change multiple transit providers global outage fix` — Bad BGP config severed Level 3, Telia, Abovenet/Zayo causing global Steam outage — matches multiple transit providers and BGP change trigger exactly.
- aprofundar DAN-007: `BGP communities prefix ordering disabled datacenters malfunction fix` — Incorrect ordering of disabled BGP advertised prefixes after standardization change affected 19 datacenters — matches BGP config change trigger, though datacenters not transit providers.
- aprofundar DAN-006: `network configuration typo Atlanta datacenter traffic fix recovery` — Typo in backbone network config during maintenance crushed one datacenter — matches network config error theme but involves single datacenter, not multiple transit providers.
  - DAN-059 (llm) [Only Some Roads Lead to Seattle] 0.597: ### Only Some Roads Lead to Seattle  When traffic from some networks completely terminates, while traffic from others is properly delivered, its usually a physical network failure (broken link or rout
  - DAN-059 (llm) [Troubles in the Data Center] 0.448: ### Troubles in the Data Center  So we have a situation with high levels of packet loss from many locations around the world. Let’s take a look at a Path Visualization to see where the network instabi
  - DAN-059 (causa) [sem seção] 0.384: Data centers are the factories of the Internet, churning out computation and services that customers demand. Apple is currently converting a 1.3M sq ft factory into a data center. And like factories, 
  - DAN-059 (correcao) [A (Nearly) Global Outage] 0.255: ### A (Nearly) Global Outage  We were monitoring the Steam API at the time of the outage. You can follow the interactive data here. The first thing we noticed was a dramatic drop in API availability, 
  - DAN-059 (correcao) [Steam Outage on May 7th] 0.254: ### Steam Outage on May 7th  Starting at 11:45 Pacific on May 7th and lasting for 2 hours, the popular online gaming service Steam suffered a widespread outage. Steam regularly has more than 8 million
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.727: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.675: ### Technical description of the error and how it happened  ``` [edit policy-options policy-statement 4-COGENT-TRANSIT-OUT term ADV-SITELOCAL then] +      community add STATIC-ROUTE; +      community 
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We
  - DAN-006 (llm) [Timeline] 0.626: ### Timeline  All timestamps are UTC.  First, an issue occurred on the backbone link between Newark and Chicago which led to backbone congestion in between Atlanta and Washington, DC.  In responding t
  - DAN-006 (llm) [Conclusion] 0.611: ### Conclusion  We’ve never experienced an outage on our backbone and our team responded quickly to restore service in the affected locations, but this was a very painful period for everyone involved.
  - DAN-006 (causa) [sem seção] 0.364: Today a configuration error in our backbone network caused an outage for Internet properties and Cloudflare services that lasted 27 minutes. We saw traffic drop by about 50% across our network. Becaus
  - DAN-006 (correcao) [What happened and what we’re doing about it] 0.372: ### What happened and what we’re doing about it  - Introduce a maximum-prefix limit on our backbone BGP sessions - this would have shut down the backbone in Atlanta, but our network is built to functi
  - DAN-006 (correcao) [What happened and what we’re doing about it] 0.314: ### What happened and what we’re doing about it  As there was backbone congestion in Atlanta, the team had decided to remove some of Atlanta’s backbone traffic. But instead of removing the Atlanta rou

## q-193 (esperado: DAN-059)

- busca inicial: DAN-007, DAN-059, DAN-006, DAN-023, DAN-154, DAN-022, DAN-159, DAN-205, DAN-209, DAN-019
- justificativa: 
- aprofundar DAN-059: `BGP configuration change transit providers connectivity loss root cause fix` — Corresponde exatamente: perda de conexão com vários provedores de trânsito (Level 3, Telia, Abovenet/Zayo) após mudança de config BGP, com pane global. Não bate: não há postmortem oficial detalhado.
- aprofundar DAN-007: `BGP advertised prefixes ordering change malfunction datacenters root cause fix` — É uma mudança de configuração BGP (padronização de comunidades) que causou mau funcionamento em datacenters, mas não menciona perda de provedores de trânsito nem pane mundial total.
- aprofundar DAN-023: `backbone router configuration change global outage root cause fix` — Mudanças de configuração em roteadores de backbone causaram pane global de todos os serviços, mas não menciona especificamente provedores de trânsito externos.
  - DAN-059 (llm) [Only Some Roads Lead to Seattle] 0.644: ### Only Some Roads Lead to Seattle  When traffic from some networks completely terminates, while traffic from others is properly delivered, its usually a physical network failure (broken link or rout
  - DAN-059 (llm) [Troubles in the Data Center] 0.464: ### Troubles in the Data Center  So we have a situation with high levels of packet loss from many locations around the world. Let’s take a look at a Path Visualization to see where the network instabi
  - DAN-059 (causa) [sem seção] 0.384: Data centers are the factories of the Internet, churning out computation and services that customers demand. Apple is currently converting a 1.3M sq ft factory into a data center. And like factories, 
  - DAN-059 (correcao) [A (Nearly) Global Outage] 0.255: ### A (Nearly) Global Outage  We were monitoring the Steam API at the time of the outage. You can follow the interactive data here. The first thing we noticed was a dramatic drop in API availability, 
  - DAN-059 (correcao) [Steam Outage on May 7th] 0.254: ### Steam Outage on May 7th  Starting at 11:45 Pacific on May 7th and lasting for 2 hours, the popular online gaming service Steam suffered a widespread outage. Steam regularly has more than 8 million
  - DAN-007 (llm) [Incident timeline and impact] 0.717: ### Incident timeline and impact  In order to be reachable on the Internet, networks like Cloudflare make use of a protocol called BGP. As part of this protocol, operators define policies which decide
  - DAN-007 (llm) [Technical description of the error and how it happened] 0.69: ### Technical description of the error and how it happened  As part of our continued effort to standardize our infrastructure configuration, we were rolling out a change to standardize the BGP communi
  - DAN-007 (causa) [Technical description of the error and how it happened] 0.465: ### Technical description of the error and how it happened  ``` !    term REJECT-THE-REST { ... } !    term 4-ADV-SITE-LOCALS { ... } !    term 6-ADV-SITE-LOCALS { ... } ``` In this diff format, the e
  - DAN-007 (correcao) [Remediation and follow-up steps] 0.488: ### Remediation and follow-up steps  This incident had widespread impact, and we take availability very seriously. We have identified several areas of improvement and will continue to work on uncoveri
  - DAN-007 (correcao) [Conclusion] 0.433: ### Conclusion  Although Cloudflare has invested significantly in our MCP design to improve service availability, we clearly fell short of our customer expectations with this very painful incident. We
  - DAN-023 (llm) [sem seção] 0.637: This was the source of yesterday’s outage. During one of these routine maintenance jobs, a command was issued with the intention to assess the availability of global backbone capacity, which unintenti
  - DAN-023 (llm) [sem seção] 0.618: Now that our platforms are up and running as usual after yesterday’s outage, I thought it would be worth sharing a little more detail on what happened and why — and most importantly, how we’re learnin
  - DAN-023 (causa) [sem seção] 0.458: All of this happened very fast. And as our engineers worked to figure out what was happening and why, they faced two large obstacles: first, it was not possible to access our data centers through our 
  - DAN-023 (correcao) [sem seção] 0.434: Helpfully, this is an event we’re well prepared for thanks to the “storm” drills we’ve been running for a long time now. In a storm exercise, we simulate a major system failure by taking a service, da

## q-194 (esperado: DAN-060)

- busca inicial: DAN-068, DAN-067, DAN-060, DAN-063, DAN-062, DAN-064, DAN-191, DAN-106, DAN-071, DAN-209
- justificativa: 
- aprofundar DAN-060: `transformer failure PLC generator phase backup generators offline fix` — Bate: perda de energia no datacenter e geradores de reserva que não entraram, afetando instâncias, volumes e bancos de uma zona. Não bate: é um evento da AWS EU West, não do nosso ambiente.
- aprofundar DAN-063: `utility power lost breaker generator mechanical failure overload manual start` — Bate: perda de utilidade e falha de geradores de reserva deixando a zona sem energia. Não bate: inclui um segundo problema de rota após a restauração de energia.
- aprofundar DAN-068: `breaker coordination settings power loss redundant paths fix` — Bate: falha de energia que bypassou caminhos de potência redundantes. Não bate: causa é configuração incorreta de breakers, não geradores que não ligam.
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.567: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  Normally, when utility power fails, electrical load is seamlessly picked up by backup generators. Program
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.467: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  By Sunday morning, August 7th, we had completed the work to fully understand root cause, prevent the prob
  - DAN-060 (causa) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.442: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  In one of the days leading up to the Friday, August 5th deletion run, there was a hardware failure that t
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.417: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  We learned a number of lessons from this event that we will use to continually improve the reliability of
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.39: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  There are several places we can improve on the communication front. First, we can accelerate the pace wit
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.587: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.509: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-068 (llm) [What happened to the power in the data center?] 0.656: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.563: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is

## q-195 (esperado: DAN-060)

- busca inicial: DAN-060, DAN-068, DAN-067, DAN-062, DAN-061, DAN-063, DAN-064, DAN-071, DAN-078, DAN-070
- justificativa: 
- aprofundar DAN-060: `backup generator PLC phase failure root cause fix` — Semelha exatamente: perda de energia no datacenter, geradores de backup não entraram por falha em PLC de sincronia de fase, afetando EC2/EBS/RDS; difere por ser na AWS EU West e ter causa específica em PLC.
- aprofundar DAN-063: `generator mechanical failure breaker overload manual restart fix` — Semelha: perda de utilidade, geradores falharam durante failover e sistema automatizado mal funcionou forçando reinício manual; difere por envolver sobrecarga de geradores remanescentes e problema de rota de rede após restauração.
- aprofundar DAN-067: `generator ground fault manual restart power restoration fix` — Semelha: geradores não voltaram online automaticamente e precisaram de acesso físico/reinício manual por disjuntor de fuga à terra; difere por ser Cloudflare Flexential e focar na restauração de energia em vez de instâncias/bancos.
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.553: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  Normally, when utility power fails, electrical load is seamlessly picked up by backup generators. Program
  - DAN-060 (llm) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.476: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  By Sunday morning, August 7th, we had completed the work to fully understand root cause, prevent the prob
  - DAN-060 (causa) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.442: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  In one of the days leading up to the Friday, August 5th deletion run, there was a hardware failure that t
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.417: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  We learned a number of lessons from this event that we will use to continually improve the reliability of
  - DAN-060 (correcao) [Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region] 0.39: ### Summary of the Amazon EC2, Amazon EBS, and Amazon RDS Service Event in the EU West Region  There are several places we can improve on the communication front. First, we can accelerate the pace wit
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.581: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Shortly thereafter, a second generator independently failed due to a mechanical issue. The loss of utility power combine
  - DAN-063 (llm) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.453: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  **December 20, 2013**  We want to give you some additional insight into the event that impacted a single Availability Zo
  - DAN-063 (causa) [Summary of the December 17th event in the South America Region (SA-EAST-1)] 0.419: ### Summary of the December 17th event in the South America Region (SA-EAST-1)  Instances in the second Availability Zone in the Region did not experience any power related issues, however instances i
  - DAN-067 (llm) [Attempting to Restore Power] 0.617: ### Attempting to Restore Power  While we haven't gotten official confirmation, we have been told by employees that three things hampered getting the generators back online. First, they needed to be p
  - DAN-067 (llm) [Informed Speculation On What Happened Next] 0.603: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (causa) [Lessons and Remediation] 0.574: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-196 (esperado: DAN-065)

- busca inicial: DAN-065, DAN-006, DAN-113, DAN-022, DAN-005, DAN-231, DAN-106, DAN-059, DAN-159, DAN-007
- justificativa: 
- aprofundar DAN-065: `IMP malfunction routing checksum recompute buffer fill keepalive nodes offline fix` — O resumo descreve exatamente os sintomas atuais: dados de roteamento estranhos com checksums válidos, buffers enchendo e nós saindo da rede um após o outro. Difere por ser um caso antigo da ARPANET/IMP, não de infra moderna.
  - DAN-065 (llm) [sem seção] 0.683: our own building (after taking dumps, of course).  This procedure initializes  all  of  the IMPs' dynamic data structures, and will                               - 2 - RFC 789                         
  - DAN-065 (llm) [sem seção] 0.669: because  of  the  failure  of some line, each has the most recent update  from   the   other   by   the   time   communication   is re-established.      This  very  short  introduction  to  the routin
  - DAN-065 (causa) [sem seção] 0.485: ```                                                           RFC 789     Vulnerabilities of Network Control Protocols: An Example                           Eric C. Rosen                   Bolt Berane
  - DAN-065 (correcao) [sem seção] 0.395: loader/dumper.  In the case under discussion, we would have liked to  have  all  the  IMPs  go  into  their loader/dumpers when the problem arose.  This would have enabled us to  re-initialize  and re
  - DAN-065 (correcao) [sem seção] 0.389: possible  for so  many updates from one IMP to be extant simultaneously, we did understand enough to be able to get the network to recover.   All that was necessary was to patch the IMPs to disregard 

## q-197 (esperado: DAN-065)

- busca inicial: DAN-065, DAN-113, DAN-109, DAN-005, DAN-006, DAN-238, DAN-022, DAN-026, DAN-106, DAN-218
- justificativa: 
- aprofundar DAN-065: `IMP corrupted routing data checksums sequence numbers buffer overflow keepalive fix` — Bate com quase todos os sintomas: nós saindo da rede, buffers enchendo, dados de roteamento estranhos e checksums válidos; não bate pela era (ARPANET/IMP).
- aprofundar DAN-113: `latent defect OS packet signature devices fail disable protocol fix` — Semelha por falhas em cascata de dispositivos de rede, mas não menciona buffers, checksums ou dados de roteamento.
- aprofundar DAN-109: `metadata service timeout storage node self shutdown retry load cascade fix` — Semelha por nós se desconectarem sozinhos e carga crescente, mas não envolve dados de roteamento nem buffers.
  - DAN-065 (llm) [sem seção] 0.666: our own building (after taking dumps, of course).  This procedure initializes  all  of  the IMPs' dynamic data structures, and will                               - 2 - RFC 789                         
  - DAN-065 (llm) [sem seção] 0.642: possible  for so  many updates from one IMP to be extant simultaneously, we did understand enough to be able to get the network to recover.   All that was necessary was to patch the IMPs to disregard 
  - DAN-065 (causa) [sem seção] 0.485: ```                                                           RFC 789     Vulnerabilities of Network Control Protocols: An Example                           Eric C. Rosen                   Bolt Berane
  - DAN-065 (correcao) [sem seção] 0.395: loader/dumper.  In the case under discussion, we would have liked to  have  all  the  IMPs  go  into  their loader/dumpers when the problem arose.  This would have enabled us to  re-initialize  and re
  - DAN-065 (correcao) [sem seção] 0.365: a problem.  There is only one exception  to  this.   Suppose  two IMPs  A  and  B  are  out  of  communication for a period of time because there is no physical path between them.  (This may be due ei
  - DAN-113 (llm) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.497: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  While disabling the new protocol resolved the event, engineering teams have continued working to identify the underlying r
  - DAN-113 (llm) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.475: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  This procedure upgrades individual devices in specific places where the upgraded devices can be exposed to production traf
  - DAN-113 (causa) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.431: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  While the removal of additional devices provided temporary remediation, several other network devices subsequently began t
  - DAN-113 (correcao) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.314: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  On September 2, 2021 at 7:30 AM JST, internal alarms alerted AWS engineers to elevated packet loss for Direct Connect cust
  - DAN-113 (correcao) [Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region] 0.242: ### Summary of AWS Direct Connect Event in the Tokyo (AP-NORTHEAST-1) Region  We would like to provide additional information about the AWS Direct Connect service disruption that occurred in the Tokyo
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.614: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.587: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-198 (esperado: DAN-069)

- busca inicial: DAN-069, DAN-191, DAN-068, DAN-063, DAN-205, DAN-064, DAN-067, DAN-209, DAN-060, DAN-102
- justificativa: 
- aprofundar DAN-069: `transmission line foliage alarm bug cascading failure root cause fix` — Bate com linhas de transmissão caindo em cascata e alarme não disparado por bug no sistema de monitoramento; não bate por ser rede elétrica física, não TI.
- aprofundar DAN-068: `breaker coordination cascade safety breakers power loss root cause fix` — Bate com falha em cascata de disjuntores e perda de energia; não bate porque não envolve alarme ausente nem linhas de transmissão.
- aprofundar DAN-067: `data center power failure cascading failures remediation lessons` — Bate com falha em cascata em data center; não bate porque não menciona alarme ausente nem linhas de transmissão.
  - DAN-069 (llm) [Cascade] 0.618: ## Cascade  ## Timeline  The following is the blackout's sequence of events on August 14, 2003 (times in EDT):  - 12:15 p.m. Incorrect telemetry data renders the state estimator, a power flow monitori
  - DAN-069 (llm) [Findings] 0.56: ## Findings  In April 2004, the U.S.-Canada Power System Outage Task Force released their final report, placing the causes of the blackout into four groups:  - FirstEnergy (FE) and its reliability cou
  - DAN-069 (causa) [Computer failure] 0.545: ## Computer failure  A software bug known as a race condition existed in General Electric Energy's Unix-based XA/21 energy management system. Once triggered, the bug stalled FirstEnergy's control room
  - DAN-069 (correcao) [Restoration of service] 0.437: ## Restoration of service  Preparations against the possible disruptions threatened by the Year 2000 problem have been credited for the installation of new electrical equipment and systems which allow
  - DAN-069 (correcao) [Investigation efforts] 0.397: ## Investigation efforts  A joint federal task force was formed by the governments of Canada and the U.S. to oversee the investigation and report directly to Ottawa and Washington. The task force was 
  - DAN-068 (llm) [What happened to the power in the data center?] 0.69: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.568: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is
  - DAN-067 (llm) [Lessons and Remediation] 0.754: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (llm) [Disaster Recovery] 0.687: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-199 (esperado: DAN-069)

- busca inicial: DAN-069, DAN-068, DAN-191, DAN-067, DAN-060, DAN-063, DAN-205, DAN-064, DAN-240, DAN-184
- justificativa: 
- aprofundar DAN-069: `alarm bug transmission line foliage cascading failure root cause fix` — Bate com o atual: falha de alarme na sala de controle e desarme em cascata de linhas de transmissão. Não bate: gatilho foi vegetação, não falha elétrica direta.
- aprofundar DAN-068: `breaker coordination settings power loss redundant paths fix` — Bate com o atual: falha de coordenação de disjuntores causando perda em cascata e bypass de redundância. Não bate: ocorre em data center, não em rede de transmissão.
- aprofundar DAN-067: `ground fault high voltage lines generator shutdown protection fix` — Bate com o atual: falha em linhas de alta tensão e desarme de proteção em cascata. Não bate: contexto é data center, não transmissão de energia.
  - DAN-069 (llm) [Cascade] 0.593: ## Cascade  ## Timeline  The following is the blackout's sequence of events on August 14, 2003 (times in EDT):  - 12:15 p.m. Incorrect telemetry data renders the state estimator, a power flow monitori
  - DAN-069 (llm) [Computer failure] 0.553: ## Computer failure  A software bug known as a race condition existed in General Electric Energy's Unix-based XA/21 energy management system. Once triggered, the bug stalled FirstEnergy's control room
  - DAN-069 (causa) [Findings] 0.529: ## Findings  In April 2004, the U.S.-Canada Power System Outage Task Force released their final report, placing the causes of the blackout into four groups:  - FirstEnergy (FE) and its reliability cou
  - DAN-069 (correcao) [Restoration of service] 0.437: ## Restoration of service  Preparations against the possible disruptions threatened by the Year 2000 problem have been credited for the installation of new electrical equipment and systems which allow
  - DAN-069 (correcao) [Investigation efforts] 0.397: ## Investigation efforts  A joint federal task force was formed by the governments of Canada and the U.S. to oversee the investigation and report directly to Ottawa and Washington. The task force was 
  - DAN-068 (llm) [What happened to the power in the data center?] 0.656: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.563: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is
  - DAN-067 (llm) [Informed Speculation On What Happened Next] 0.633: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (llm) [Informed Speculation On What Happened Next] 0.547: ### Informed Speculation On What Happened Next  From this decision onward, we don't yet have clarity from Flexential on the root cause or some of the decisions they made or the events. We will update 
  - DAN-067 (causa) [Lessons and Remediation] 0.574: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s

## q-200 (esperado: DAN-073)

- busca inicial: DAN-073, DAN-164, DAN-129, DAN-209, DAN-048, DAN-109, DAN-026, DAN-186, DAN-066, DAN-226
- justificativa: 
- aprofundar DAN-073: `storage volume failure cause recovery fix` — Bate com o incidente atual: falha de storage server derrubou o site principal e depois sites/programas dos usuários em cascata. Não confirma se o componente exato é o mesmo.
  - DAN-073 (llm) [Next steps¶] 0.702: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (llm) [18:23¶] 0.68: #### 18:23¶  At this time, livefile1 had the new volumes attached, and we were logged in and checking everything out. The server needed to do a full filesystem check before the storage was available, 
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi

## q-201 (esperado: DAN-073)

- busca inicial: DAN-073, DAN-209, DAN-109, DAN-226, DAN-129, DAN-208, DAN-026, DAN-191, DAN-064, DAN-103
- justificativa: 
- aprofundar DAN-073: `storage volume failure root cause fix recovery outage` —  bate com o incidente atual: falha de volume em servidor de storage derrubou o site e sites/programas dos usuários dependentes desse volume, espalhando para outros sites.
- aprofundar DAN-191: `3PAR storage controller failure root cause fix impact` —  envolve falha em controlador de storage, mas resumo diz sem impacto inicial nos usuários, diferente do incidente atual.
- aprofundar DAN-109: `storage nodes metadata load timeout root cause fix` —  envolve storage nodes derrubando a si mesmos, mas o gatilho é disrupção de rede, não um único servidor de storage com problema.
  - DAN-073 (llm) [Next steps¶] 0.689: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (llm) [18:23¶] 0.681: #### 18:23¶  At this time, livefile1 had the new volumes attached, and we were logged in and checking everything out. The server needed to do a full filesystem check before the storage was available, 
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi
  - DAN-191 (llm) [sem seção] 0.607: Controllers                                                                                       4. Legacy workload (eg., oracle database, Solaris hosts,    4                      for adaptive       
  - DAN-191 (llm) [sem seção] 0.604: On the 17th October 2016 one of the four controllers within the principal HP storage system located in the Strand Data Centre failed. There was no user impact. HP hardware engineers then arrived on si
  - DAN-191 (causa) [sem seção] 0.483: IT INFRASTRUCTURE RESILIENCY REVIEW  23 February 2017  Introduction  Objective of the review:                                      Structure of the report:  This report presents the findings of the IT
  - DAN-191 (correcao) [sem seção] 0.456: The incident timeline presented overleaf is a high level  depiction of the incident from the start on Monday 17th Oct until  the BCP Silver team handed over the recovery and restoration  work to the r
  - DAN-191 (correcao) [sem seção] 0.446: It was later established, in an assessment of the incident by HP, that the inability of the storage system to return to service after the defective hardware was replaced was due to a flaw in the firmw
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.542: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.539: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.364: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-202 (esperado: DAN-076)

- busca inicial: DAN-076, DAN-154, DAN-073, DAN-127, DAN-148, DAN-106, DAN-059, DAN-198, DAN-103, DAN-126
- justificativa: 
- aprofundar DAN-076: `boot.ini deletion expansion installer root cause fix` — O incidente envolve instalação de expansão de jogo que impede o computador de iniciar ao deletar o boot.ini, correspondendo exatamente ao sintoma relatado, embora seja de um jogo diferente (EVE Online).
  - DAN-076 (llm) [About the boot.ini issue] 0.763: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.731: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 

## q-203 (esperado: DAN-076)

- busca inicial: DAN-076, DAN-154, DAN-073, DAN-059, DAN-127, DAN-142, DAN-146, DAN-189, DAN-103, DAN-216
- justificativa: 
- aprofundar DAN-076: `boot.ini deletion installer expansion root cause fix` — O incidente atual envolve computadores que não bootam após instalação de expansão de jogo; DAN-076 é exatamente sobre um instalador de expansão que deletava o boot.ini, impedindo o boot — mesma causa (instalação de expansão) e mesmo sintoma (não boot), diferindo apenas no jogo específico.
- aprofundar DAN-142: `content update Windows BSOD root cause fix rollback` — Também envolve uma atualização que causa falha no Windows (BSOD) em máquinas dos usuários, semelhante ao sintoma de não boot, mas se trata de atualização de conteúdo de segurança, não de expansão de jogo.
- aprofundar DAN-127: `logging channel cluster nodes dying patch root cause fix` — Envolve um patch de jogo causando falhas, mas do lado do cluster de servidores, não do boot de computadores dos jogadores, então a semelhança é limitada.
  - DAN-076 (llm) [About the boot.ini issue] 0.752: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.725: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 
  - DAN-142 (llm) [Q: What happened?] 0.658: ### Q: What happened?  On July 19, 2024, a Rapid Response Content update was delivered to certain Windows hosts, evolving a new sensor capability first released in February 2024 that enabled visibilit
  - DAN-142 (llm) [What Happened?] 0.62: ### What Happened?  On Friday, July 19, 2024 at 04:09 UTC, as part of regular operations, CrowdStrike released a content configuration update for the Windows sensor to gather telemetry on possible nov
  - DAN-142 (causa) [What Went Wrong and Why?] 0.384: ### What Went Wrong and Why?  Template Type Stress Testing: On March 05, 2024, a stress test of the IPC Template Type was executed in our staging environment, which consists of a variety of operating 
  - DAN-142 (correcao) [Q: Has this issue been fixed?] 0.463: ### Q: Has this issue been fixed?  Channel File 291 was identified and fixed 78 minutes after it was released, at 1:27 a.m. EDT on July 19. A logic error in our Content Validator (software that perfor
  - DAN-142 (correcao) [Remediation Videos] 0.449: ## Remediation Videos  ### CrowdStrike Host Self-Remediation for Remote Users  This video outlines the steps required to self-remediate impacted remote Windows laptops. Follow these instructions if di
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.675: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.639: # Behind the Scenes of a long EVE Online downtime  We had prepared a series of escalating steps that we intended to follow. Each one would progressively add more factors in to the mix, until the issue
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan

## q-204 (esperado: DAN-083)

- busca inicial: DAN-083, DAN-195, DAN-190, DAN-102, DAN-058, DAN-092, DAN-188, DAN-126, DAN-003, DAN-056
- justificativa: 
- aprofundar DAN-083: `Postgres HA upgrade sequence jump nextval SEQ_LOG_VALS 32 WAL fix` — DAN-083 é o único que descreve exatamente o mesmo sintoma: pulo de 32 em IDs sequenciais após promoção de follower Postgres em atualização de HA; os outros incidentes tratam de wraparound de XID, replicação MySQL, locks PGAudit ou estatísticas, sem relação com sequências.
  - DAN-083 (llm) [sem seção] 0.74: ``` /*  * We don't want to log each fetching of a value from a sequence,  * so we pre-log a few fetches in advance. In the event of  * crash we can lose (skip over) as many values as we pre-logged.  *
  - DAN-083 (llm) [sem seção] 0.62: 1. We go to great lengths to ensure that if someone asks us to create an incident, we do so (!). We hadn't seen any issues and had no reports from customers, either. 2. For failed incident creation to
  - DAN-083 (causa) [See related articles] 0.353: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-083 (correcao) [sem seção] 0.325: As part of this promotion, the follower (which in many cases had a sequence value up to 32 ahead) became the new primary, at which point all sequences essentially jumped 32 values forward.  Something 
  - DAN-083 (correcao) [sem seção] 0.318: The other day, we started getting strange reports from some customers of incident.io.  Their incident identifiers — unique numbers to identify each incident — appeared to have jumped unexpectedly. One

## q-205 (esperado: DAN-083)

- busca inicial: DAN-083, DAN-195, DAN-190, DAN-102, DAN-092, DAN-188, DAN-164, DAN-003, DAN-048, DAN-080
- justificativa: 
- aprofundar DAN-083: `Postgres HA upgrade nextval sequence cache 32 jump failover fix` — É o único incidente com o mesmo sintoma exato (salto de 32 em sequências após upgrade/HA do Postgres com promoção de follower) e mesmo componente (nextval de sequências Postgres); difere apenas no objeto sequenciado (IDs de organização vs números de registro).
  - DAN-083 (llm) [sem seção] 0.712: ``` /*  * We don't want to log each fetching of a value from a sequence,  * so we pre-log a few fetches in advance. In the event of  * crash we can lose (skip over) as many values as we pre-logged.  *
  - DAN-083 (llm) [sem seção] 0.621: However, in the case of a rollback, while the changes to the rows in the database is reverted, any impact on sequences isn't. They'll just keep increasing, so you can end up with the sequence “running
  - DAN-083 (causa) [sem seção] 0.401: 1. We go to great lengths to ensure that if someone asks us to create an incident, we do so (!). We hadn't seen any issues and had no reports from customers, either. 2. For failed incident creation to
  - DAN-083 (correcao) [See related articles] 0.426: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you
  - DAN-083 (correcao) [sem seção] 0.325: As part of this promotion, the follower (which in many cases had a sequence value up to 32 ahead) became the new primary, at which point all sequences essentially jumped 32 values forward.  Something 

## q-206 (esperado: DAN-085)

- busca inicial: DAN-164, DAN-085, DAN-050, DAN-157, DAN-097, DAN-129, DAN-130, DAN-092, DAN-098, DAN-078
- justificativa: 
- aprofundar DAN-085: `SHA-1 collision deduplication test data checkout consistency root cause fix` — Bate com o atual: repositório de código indisponível, checkout falha consistência, depois de commit com arquivos de teste. Não bate exatamente: causa é colisão SHA-1 intencional em Subversion com deduplicação.
  - DAN-085 (llm) [Problem Statement] 0.657: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options] 0.641: # Subversion SHA1 Collision Problem Statement — Prevention and Remediation Options  You probably saw the news last week that researchers at Google had found a scenario where they were able to break th
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-207 (esperado: DAN-085)

- busca inicial: DAN-085, DAN-164, DAN-050, DAN-157, DAN-055, DAN-173, DAN-097, DAN-129, DAN-078, DAN-130
- justificativa: 
- aprofundar DAN-085: `SHA1 collision deduplication test files checkout consistency remediation fix` — Repositório de código indisponível após commit com arquivos de teste e checkout falha consistência, igual ao incidente atual; difere por ser Subversion com deduplicação e colisão SHA-1 intencional.
  - DAN-085 (llm) [Problem Statement] 0.714: ## Problem Statement  The problem that happens is caused by a feature that was added in Subversion 1.6 called “Representation Sharing”. When Subversion stores the data for a commit, eventually bytes f
  - DAN-085 (llm) [Wrapping Up] 0.699: ## Wrapping Up  Finally, there is still another problem scenario to be aware of and that is on the SVN client. Suppose you decide to turn off representation sharing in the repository. When this happen
  - DAN-085 (causa) [Wrapping Up] 0.277: ## Wrapping Up  To summarize so far, there are options to prevent the problem. If the disk space savings offered by representation sharing are not your main concern then that is the best solution and 
  - DAN-085 (correcao) [Remediation Options] 0.38: ## Remediation Options  Another option is the one the Webkit repository used and that is to create a Subversion permission rule (authz) that blocks access to the file(s). This will work with tools lik
  - DAN-085 (correcao) [Remediation Options] 0.366: ## Remediation Options  So these first two options talk about how to PREVENT the problem. Now lets talk about what to do once you get the problem. To do that, lets first talk about the scope of the pr

## q-208 (esperado: DAN-086)

- busca inicial: DAN-086, DAN-015, DAN-090, DAN-191, DAN-154, DAN-221, DAN-103, DAN-210, DAN-142, DAN-016
- justificativa: 
- aprofundar DAN-086: `February 29 certificate expiration invalid date fix` — Bate: 29 de fevereiro, certificados rejeitados por data inválida e criação de instâncias falhando; não bate: plataforma Azure específica versus plataforma atual não especificada.
- aprofundar DAN-090: `expired certificate outage fix certificate store` — Bate: certificados causando falha em plataforma ampla; não bate: expiração normal de certificado versus erro de cálculo de data bissexto.
  - DAN-086 (llm) [The Leap Day Bug] 0.576: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.534: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover
  - DAN-090 (llm) [Root Cause Analysis] 0.652: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.471: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (causa) [sem seção] 0.366: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a

## q-209 (esperado: DAN-086)

- busca inicial: DAN-086, DAN-129, DAN-210, DAN-103, DAN-029, DAN-154, DAN-049, DAN-090, DAN-189, DAN-015
- justificativa: 
- aprofundar DAN-086: `leap year certificate expiration date February 29 root cause fix code patch` — O incidente atual ocorre em 29 de fevereiro com certificados rejeitados e criação de instâncias falhando — corresponde exatamente ao bug de ano bissexto do Azure em 2012, onde código calculava um ano como data atual mais um ano, gerando expiração em 29 de fevereiro de 2013 (data inválida). Não há outro incidente na lista com gatilho de ano bissexto ou falha de certificado por data inválida.
  - DAN-086 (llm) [The Leap Day Bug] 0.591: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.554: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-210 (esperado: DAN-088)

- busca inicial: DAN-088, DAN-103, DAN-129, DAN-066, DAN-209, DAN-089, DAN-189, DAN-116, DAN-087, DAN-064
- justificativa: 
- aprofundar DAN-088: `leap second xtime_lock printk klogd deadlock kernel fix` — Semelhante porque é travamento de servidores Linux no leap second por deadlock no kernel, diferindo apenas no gatilho (printk/klogd).
- aprofundar DAN-089: `leap second CLOCK_REALTIME hrtimer futex spinwait fix patch` — Semelhante porque é leap second em Linux derrubando serviços em massa, diferindo no mecanismo (futex/hrtimer e giro ocupado, não deadlock).
- aprofundar DAN-087: `leap second time.Now monotonic rand.Int63n DNS panic fix` — Semelhante porque é pane provocada por leap second, diferindo porque ocorre em DNS em Go/Cloudflare, não em travamento de servidores Linux.
  - DAN-088 (llm) [sem seção] 0.812: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.774: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (causa) [sem seção] 0.329: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco
  - DAN-089 (llm) [sem seção] 0.81: | Messages in this thread |  | On 07/01/2012 11:29 AM, John Stultz wrote: > TODOs: > \* Chase down the futex/hrtimer interaction to see if this could > be triggered in any other way. Ok, got a little 
  - DAN-089 (llm) [sem seção] 0.784: /\* Set the leap second insert flag \*/ tx.modes = ADJ\_STATUS; tx.status = STA\_INS; adjtimex(&tx); clock\_gettime(clock\_type, &ts); now = then = ts.tv\_sec; while(now - then \< 30){ struct timespec
  - DAN-089 (causa) [sem seção] 0.239: The test sets a leapsecond to trigger in 10 seconds, then in a loop sleeps for half a second via clock\_nanosleep, printing out the current time, and the delta from the target wakeup time for 30 secon
  - DAN-089 (correcao) [sem seção] 0.261: With my fix to call clock\_was\_set when we apply a leapsecond, I no longer see the issue. thanks -john /\* Leap second timer test \* by: john stultz (johnstul@us.ibm.com) \* (C) Copyright IBM 2012 \*
  - DAN-089 (correcao) [sem seção] 0.225: if (ns \< 0) { neg = 1; ns = -ns; } a.tv\_sec = ns/NSEC\_PER\_SEC; a.tv\_nsec = ns%NSEC\_PER\_SEC; if (neg) { a.tv\_sec = -a.tv\_sec; a.tv\_nsec = -a.tv\_nsec; } return a; } int main(void) { struct ti
  - DAN-087 (llm) [A falsehood programmers believe about time] 0.729: ### A falsehood programmers believe about time  The root cause of the bug that affected our DNS service was the belief that *time cannot go backwards*. In our case, some code assumed that the *differe
  - DAN-087 (llm) [A falsehood programmers believe about time] 0.661: ### A falsehood programmers believe about time  RRDNS doesn’t just keep a single measurement for each resolver, it takes many measurements and smoothes them. So, the single measurement wouldn’t cause 
  - DAN-087 (causa) [sem seção] 0.385: At midnight UTC on New Year’s Day, deep inside Cloudflare’s custom RRDNS software, a number went negative when it should always have been, at worst, zero. A little later this negative value caused RRD
  - DAN-087 (correcao) [The one character fix] 0.332: ### The one character fix  One precaution when using a non-monotonic clock source is to always check whether the difference between two timestamps is negative. Should this happen, it’s not possible to
  - DAN-087 (correcao) [Timeline] 0.444: ### Timeline  The following is the complete timeline of the events around the leap second bug.  2017-01-01 00:00 UTC Impact starts  2017-01-01 00:10 UTC Escalated to engineers  2017-01-01 00:34 UTC Is

## q-211 (esperado: DAN-088)

- busca inicial: DAN-088, DAN-103, DAN-129, DAN-073, DAN-026, DAN-116, DAN-205, DAN-209, DAN-064, DAN-066
- justificativa: 
- aprofundar DAN-088: `leap second xtime_lock printk klogd deadlock fix` — É o único incidente com segundo bissexto e travamento simultâneo de servidores Linux por deadlock no xtime_lock; o gatilho e o componente batem exatamente com o incidente atual.
  - DAN-088 (llm) [sem seção] 0.806: q\_exit () at kernel/softirq.c:310 #22 0xffffffff8101b0fe in smp\_apic\_timer\_interrupt (regs=\<value optimized out>) at arch/x86/kernel/apic\_64.c:514 #23 0xffffffff8100cf52 in apic\_timer\_interrup
  - DAN-088 (llm) [sem seção] 0.765: sync=0, key=0x0) at kernel/sched.c:4387 #10 0xffffffff8102b97b in \_\_wake\_up (q=0xffffffff813d3180, mode=1, nr\_exclusive=1, key=0x0) at kernel/sched.c:4406 #11 0xffffffff8103692f in wake\_up\_klogd
  - DAN-088 (causa) [sem seção] 0.328: I'm looking at the source for the RHEL 4 kernel 2.6.9-67.0.7.EL (which I had crash on a system), and the scheduler is enough different that I am not finding the path to the deadlock right off. In any 
  - DAN-088 (correcao) [sem seção] 0.299: p=0xffff81003b8ac418, wakeup=-994836480) at kernel/sched.c:1550 #5 0xffffffff81029a39 in activate\_task (rq=0xffff810009013880, p=0xffff81003b8ac418, wakeup=20045) at kernel/sched.c:1614 #6 0xffffffff
  - DAN-088 (correcao) [sem seção] 0.269: args=\<value optimized out>) at kernel/printk.c:789 #14 0xffffffff81037081 in printk ( fmt=0xffffffff8158bb30 "yj$\201????\2008\001\t") at kernel/printk.c:613 #15 0xffffffff8104ec16 in ntp\_leap\_seco

## q-212 (esperado: DAN-092)

- busca inicial: DAN-092, DAN-103, DAN-133, DAN-134, DAN-080, DAN-209, DAN-195, DAN-101, DAN-148, DAN-035
- justificativa: 
- aprofundar DAN-092: `workflows database cutover stale statistics ANALYZE disk reads fix` — Escolhi porque é praticamente o mesmo padrão: cutover de banco de workflows, queries lendo do disco por estatísticas desatualizadas e jobs descartados, diferindo apenas no provedor (CircleCI).
- aprofundar DAN-080: `postgres migration long running query blocked queries downtime fix` — Escolhi porque envolve migração de banco de dados causando bloqueio de queries e indisponibilidade, mas não trata de estatísticas desatualizadas nem leitura completa do disco após cutover.
- aprofundar DAN-133: `MongoDB slow queries workflow delay thread pool fix` — Escolhi porque menciona delays em workflows e jobs acumulados, mas a causa é MongoDB e pools de conexão JVM, não estatísticas desatualizadas após cutover de banco de workflows.
  - DAN-092 (llm) [What Happened] 0.704: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [What Happened] 0.643: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (causa) [Summary] 0.393: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers
  - DAN-092 (correcao) [Future Prevention and Process Improvement] 0.483: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-080 (llm) [Avoiding downtime] 0.725: ## Avoiding downtime  Applications vary too much for there to be a "one size fits all" solution to this problem, but there are a few good places to start:  - Eliminate long-running queries/transaction
  - DAN-080 (llm) [So what happened?] 0.696: ## So what happened?  We deployed the changes, and all of our assumptions got blown out of the water. Just after the schema migration started, we started getting alerts about API requests timing out. 
  - DAN-080 (causa) [Zero-downtime Postgres migrations - the hard parts] 0.354: ## Zero-downtime Postgres migrations - the hard parts  Written by  Last editedJun 2024  A few months ago, we took around 15 seconds of unexpected API downtime during a planned database migration. We'r
  - DAN-080 (correcao) [Background] 0.31: ## Background  We're no strangers to zero-downtime schema changes. Having the database stop responding to queries for more than a second or two isn't an option, so there's a bunch of stuff you learn e
  - DAN-080 (correcao) [The migration] 0.305: ## The migration  Jump back to late January. At the time, we were building invoicing for our Pro product. We'd been through a couple of iterations, and settled on model/table names. We'd already deplo
  - DAN-133 (llm) [Incident Report] 0.715: ## Incident Report  Perhaps most importantly, MongoDB support pointed us at the `tcmalloc.spinlock_total_delay_ns` MongoDB stat. This stat correlates with the time spent on database operations blocked
  - DAN-133 (llm) [Incident Report] 0.713: ## Incident Report  April 10, 2019 at 13:25 UTC we were alerted to sharp increases in multiple queues responsible for job and workflow processing. Our monitoring of MongoDB showed some issues, but not
  - DAN-133 (causa) [Incident Report] 0.453: ## Incident Report  Between March 26 and April 10, 2019, our platform experienced instability and downtime primarily due to issues with the datastore backing our builds queue. These datastore issues r
  - DAN-133 (correcao) [Incident Report] 0.533: ## Incident Report  Ultimately, refactoring the way we store and access portions of our data set in MongoDB will reduce load. Improving our data access and storage at the application level is one of o
  - DAN-133 (correcao) [Incident Report] 0.47: ## Incident Report  Around the same time, we updated many services to a new minor version of the JVM to pick up security changes. This update also included improvements for docker-awareness enabled by

## q-213 (esperado: DAN-092)

- busca inicial: DAN-092, DAN-133, DAN-164, DAN-134, DAN-080, DAN-148, DAN-101, DAN-078, DAN-130, DAN-096
- justificativa: 
- aprofundar DAN-092: `root cause stale statistics ANALYZE index full table scan disk cutover fix re-promote blue database` — Mesmo componente (workflows database), mesmo gatilho (cutover/upgrade), mesmo sintoma (queries lendo tudo do disco, latência alta, jobs sendo dropados). Difere apenas no detalhe de ter havido uma segunda atualização de versão major após o ANALYZE.
  - DAN-092 (llm) [What Happened] 0.705: ## What Happened  Post-incident, the team continued to investigate. The root cause was determined to be that the analyze operation to rebuild the database’s statistics table, which is used for indexes
  - DAN-092 (llm) [Future Prevention and Process Improvement] 0.594: ## Future Prevention and Process Improvement  The blue/green database deployment procedures have been updated to run an analysis procedure after every major version change. The team has also tested ru
  - DAN-092 (causa) [What Happened] 0.429: ## What Happened  (all times UTC)  At approximately 22:00 on April 4, we initiated an upgrade to the service responsible for workflows. We expected a short delay (\< 90 seconds) during the database up
  - DAN-092 (correcao) [Summary] 0.402: ## Summary  On April 3, 2025, from 22:08 UTC to 23:45 UTC, CircleCI customers experienced increased latency and some failures with starting and canceling workflows and jobs. During this time customers

## q-214 (esperado: DAN-093)

- busca inicial: DAN-048, DAN-078, DAN-093, DAN-094, DAN-003, DAN-190, DAN-164, DAN-096, DAN-186, DAN-058
- justificativa: 
- aprofundar DAN-093: `schema migration failover MySQL data drift wrong owner fix` — Bate quase exatamente: migração de schema gerou carga que disparou failover do MySQL e, após eleições simultâneas, o primário stale roteou repositórios privados para donos errados. Não bate: envolve Pacemaker, buffer pool frio e failback, além do failover inicial.
  - DAN-093 (llm) [Monday, September 10th] 0.645: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.591: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.368: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member

## q-215 (esperado: DAN-093)

- busca inicial: DAN-048, DAN-078, DAN-093, DAN-003, DAN-164, DAN-094, DAN-096, DAN-186, DAN-080, DAN-056
- justificativa: 
- aprofundar DAN-093: `schema migration MySQL failover stale node data drift wrong owner fix` — É o único que combina migração de schema, failover inesperado do MySQL e dados entregues a contas erradas (repositórios privados roteados para donos errados) — espelha diretamente o incidente atual; difere apenas nos componentes (Percona/Pacemaker).
- aprofundar DAN-078: `MySQL master failover missing writes data integrity restoration fix` — Compartilha o failover do MySQL master e o trabalho de restauração de integridade de dados, mas não tem gatilho de migração de schema nem vazamento de dados entre contas.
  - DAN-093 (llm) [Monday, September 10th] 0.668: ## Monday, September 10th  The events that led up to Monday’s downtime began with a rather innocuous database migration. We use a two-pass migration system to allow for zero-downtime MySQL schema migr
  - DAN-093 (llm) [Tuesday, September 11th] 0.621: ## Tuesday, September 11th  The following morning, our operations team was notified by a developer of incorrect query results returning from the node providing the ‘standby’ role. I investigated the s
  - DAN-093 (causa) [Tuesday, September 11th] 0.473: ## Tuesday, September 11th  In summary, three primary events contributed to the downtime of the past few days. First, several failovers of the ‘active’ database role happened when they shouldn’t have.
  - DAN-093 (correcao) [Tuesday, September 11th] 0.392: ## Tuesday, September 11th  As a result of this data drift, inconsistencies between MySQL and other data stores in our infrastructure were possible. We use Redis to query dashboard event stream entrie
  - DAN-093 (correcao) [In ops I trust] 0.336: ## In ops I trust  The automated failover of our main production database could be described as the root cause of both of these downtime events. In each situation in which that occurred, if any member
  - DAN-078 (llm) [Next steps] 0.688: ## Next steps  ## Resolving data inconsistencies  During our recovery, we captured the MySQL binary logs containing the writes we took in our primary site that were not replicated to our West Coast si
  - DAN-078 (llm) [2018 October 22 00:05 UTC] 0.662: ## 2018 October 22 00:05 UTC  Engineers involved in the incident response team began developing a plan to resolve data inconsistencies and implement our failover procedures for MySQL. Our plan was to 
  - DAN-078 (causa) [Incident timeline] 0.478: ## Incident timeline  ## 2018 October 21 22:52 UTC  During the network partition described above, Orchestrator, which had been active in our primary data center, began a process of leadership deselect
  - DAN-078 (correcao) [Organizational initiatives] 0.538: ## Organizational initiatives  This incident has led to a shift in our mindset around site reliability. We have learned that tighter operational controls or improved response times are insufficient sa
  - DAN-078 (correcao) [2018 October 22 16:24 UTC] 0.479: ## 2018 October 22 16:24 UTC  Once the replicas were in sync, we conducted a failover to the original topology, addressing the immediate latency/availability concerns. As part of a conscious decision 

## q-216 (esperado: DAN-106)

- busca inicial: DAN-106, DAN-073, DAN-048, DAN-164, DAN-109, DAN-071, DAN-191, DAN-064, DAN-139, DAN-060
- justificativa: 
- aprofundar DAN-106: `routine networking upgrade EBS volume freeze outage root cause fix` — Atualização de rede de rotina causou pane em volumes de bloco por toda a região, igual ao incidente atual.
- aprofundar DAN-109: `network disruption storage nodes take themselves down retry fix` — Disrupção de rede derrubou nós de armazenamento, mas não menciona atualização de rotina nem congelamento de blocos.
- aprofundar DAN-073: `storage volume failure outage root cause fix` — Falha em volume de armazenamento derrubou instâncias dependentes, mas foi em um servidor, não região inteira por atualização de rede.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.677: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  When this network connectivity issue occurred, a large number of EBS nodes in a single EBS cluster lost connectio
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.674: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  A large majority of the volumes in the degraded EBS cluster were still functioning properly and the focus was to 
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.574: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.539: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  The specific assignment of a group of partitions to a given server is called a “membership.” The member
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.368: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.407: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-073 (llm) [17:04¶] 0.694: #### 17:04¶  By this point we had become sure that the system was getting blocked on storage IO, but the problem did not seem to be the machine itself like the original indications had suggested. Howe
  - DAN-073 (llm) [Next steps¶] 0.686: ### Next steps¶  The first thing to note here is that storage volume failure of this kind is incredibly rare, as we noted above. We do have some ideas about how to reduce it further – for example, by 
  - DAN-073 (causa) [16:16¶] 0.526: #### 16:16¶  Initial indications were that the problem was on the file server itself rather than its attached storage; there were kernel-level errors in syslog that looked very much like machine hardw
  - DAN-073 (correcao) [Speeding up recovery¶] 0.434: #### Speeding up recovery¶  There were four points where our processes were too slow:  - Identifying the underlying cause of the problem. Clearly it’s not good that that the issue started at 16:06, bu
  - DAN-073 (correcao) [Speeding up recovery¶] 0.294: #### Speeding up recovery¶  This is something we should have ready to go in a fully tested script so that we just need to run something like `python3 replace_file_server_storage_with_backups.py livefi

## q-217 (esperado: DAN-106)

- busca inicial: DAN-106, DAN-073, DAN-060, DAN-109, DAN-107, DAN-210, DAN-071, DAN-222, DAN-048, DAN-143
- justificativa: 
- aprofundar DAN-106: `routine networking upgrade human error EBS volume stuck resource crunch fix` — Bate: upgrade de rede rotineira causou pane regional em volumes e instâncias dependentes; não bate: não menciona explicitamente volumes travados, apenas perda de 0,07% de volumes.
- aprofundar DAN-143: `automatic upgrade network rules removed Cilium outage fix` — Bate: upgrade automático removeu regras de rede e causou pane multirregional; não bate: não envolve volumes de armazenamento em bloco, apenas regras de rede Cilium.
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.685: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  A large majority of the volumes in the degraded EBS cluster were still functioning properly and the focus was to 
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.663: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  When this network connectivity issue occurred, a large number of EBS nodes in a single EBS cluster lost connectio
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.434: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-143 (llm) [Root cause] 0.665: ## Root cause  We have identified (and since disabled) the initial trigger for the outage: on March 8, 2023, at 06:00 UTC, a security update to systemd was automatically applied to a number of VMs, wh
  - DAN-143 (llm) [Root cause] 0.564: ## Root cause  However, the base OS image we use to run Kubernetes had a legacy security update channel enabled, which caused the update to apply automatically. By design we use fairly minimal base OS
  - DAN-143 (causa) [Lessons learned] 0.422: ## Lessons learned  The following is not the sum total of everything we learned during the incident but rather important themes that pertain to the whole platform.  This was our first global incident.
  - DAN-143 (correcao) [Lessons learned] 0.446: ## Lessons learned  Even with separate systems that serve live data when historical data is not accessible (e.g., APM’s Live Search and Log Management’s Live Tail), we did not provide our customers wi
  - DAN-143 (correcao) [Recovery] 0.445: ## Recovery  The high-level steps of the recovery had to be sequenced because of the magnitude of the compute capacity drop:  - First, for each region, recover enough compute capacity so that it could

## q-218 (esperado: DAN-116)

- busca inicial: DAN-126, DAN-146, DAN-103, DAN-066, DAN-209, DAN-106, DAN-048, DAN-191, DAN-116, DAN-189
- justificativa: 
- aprofundar DAN-116: `double free database update all impression bus servers crash simultaneous root cause fix rollback` — Bate: atualização de banco/dados seguida de queda simultânea de todos os servidores após um atraso/tempo. Não bate: componente específico é impression bus, não um serviço crítico genérico.
  - DAN-116 (llm) [sem seção] 0.697: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (llm) [sem seção] 0.696: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b

## q-219 (esperado: DAN-116)

- busca inicial: DAN-066, DAN-126, DAN-103, DAN-222, DAN-205, DAN-209, DAN-116, DAN-109, DAN-191, DAN-189
- justificativa: 
- aprofundar DAN-116: `database update double free crash simultaneous servers fix` — O resumo menciona uma atualização de banco de dados que fez todos os servidores caírem ao mesmo tempo, com atraso temporário antes do bug disparar, correspondendo ao padrão do incidente atual.
- aprofundar DAN-209: `migration critical backend system outage error fix` — Envolve erro durante mudança em sistema back-end crítico, mas não especifica queda simultânea de todos os servidores após atualização de dados.
- aprofundar DAN-126: `update side effects data loss server misconfiguration hotfix` — Envolve efeitos colaterais de atualização e hotfix em vários servidores, mas foca em perda de dados, não em queda simultânea imediata.
  - DAN-116 (llm) [sem seção] 0.729: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.599: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b
  - DAN-209 (llm) [sem seção] 0.569: As we modernize our infrastructure, we may continue to perform different types of server migrations. Since this was due to a unique and risky migration that is now complete, we don’t expect this exact
  - DAN-209 (llm) [sem seção] 0.537: tl;dr  On Thursday, August 11, Reddit was down and unreachable across all platforms for about 1.5 hours, and slow to respond for an additional 1.5 hours. We apologize for the downtime and want to let 
  - DAN-126 (llm) [Server Configurations] 0.612: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-126 (llm) [Server Configurations] 0.609: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [sem seção] 0.436: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’

## q-220 (esperado: DAN-118)

- busca inicial: DAN-148, DAN-118, DAN-066, DAN-067, DAN-154, DAN-217, DAN-209, DAN-191, DAN-001, DAN-109
- justificativa: 
- aprofundar DAN-118: `root cause customers lost access products remediation` — Setecentos e setenta e cinco clientes perderam acesso aos produtos, igual ao incidente atual, mas o resumo não revela causa nem correção.
- aprofundar DAN-154: `global outage software bug configuration change fix` — Interrupção global afetou todos os clientes de uma vez, mas o resumo não detalha a causa raiz nem a correção aplicada.
- aprofundar DAN-066: `Byzantine failure cascading API dashboard root cause remediation` — Falha em cascata afetou a disponibilidade de API e dashboard, semelhante à perda total de acesso, embora tenha origem em switch parcial.
  - DAN-118 (llm) [Executive summary] 0.59: ## Executive summary  On Tuesday, April 5th, 2022, starting at 7:38 UTC, 775 Atlassian customers lost access to their Atlassian products. The outage spanned up to 14 days for a subset of these custome
  - DAN-118 (llm) [Executive summary] 0.58: ## Executive summary  At the start of the incident, we knew exactly which sites were affected and our priority was to establish communication with the approved owner for each impacted site to inform t
  - DAN-118 (causa) [How will we improve?] 0.465: ## How will we improve?  We have immediately blocked bulk sites deletes until appropriate changes can be made.  As we move forward from this incident and re-evaluate our internal processes, we want to
  - DAN-118 (correcao) [Workstream 3: Accelerated recovery and the Restoration 2 approach] 0.479: #### Workstream 3: Accelerated recovery and the Restoration 2 approach  **Timestamp: Days 4 – 13 (April 9th – 17th)**  With the Restoration 1 approach, it would have taken us three weeks to restore al
  - DAN-118 (correcao) [Learning 4: Improve our communications processes] 0.473: ### Learning 4: Improve our communications processes  **a) We deleted critical customer identifiers, impacting communications and actions to those affected**  The same script which deleted customer si
  - DAN-154 (llm) [sem seção] 0.692: We experienced a global outage due to an undiscovered software bug that surfaced on June 8 when it was triggered by a valid customer configuration change. We detected the disruption within one minute,
  - DAN-154 (llm) [**What happened?**] 0.69: ### **What happened?**  On May 12, we began a software deployment that introduced a bug that could be triggered by a specific customer configuration under specific circumstances.  Early June 8, a cust
  - DAN-154 (causa) [**Where do we go from here?**] 0.397: ### **Where do we go from here?**  In the short term:  - We’re deploying the bug fix across our network as quickly and safely as possible. - We are conducting a complete post mortem of the processes a
  - DAN-154 (correcao) [**Conclusion**] 0.407: ### **Conclusion**  Even though there were specific conditions that triggered this outage, we should have anticipated it. We provide mission critical services, and we treat any action that can cause s
  - DAN-066 (llm) [The Dashboard] 0.652: ### The Dashboard  The Cloudflare dashboard, like most web applications, has the notion of a user session. When user sessions are created (each time a user logs in) we perform some database operations
  - DAN-066 (llm) [sem seção] 0.587: *An analysis of the Cloudflare API availability incident on 2020-11-02*  When we review design documents at Cloudflare, we are always on the lookout for Single Points of Failure (SPOFs). Eliminating t
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.463: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain

## q-221 (esperado: DAN-118)

- busca inicial: DAN-067, DAN-118, DAN-148, DAN-154, DAN-209, DAN-066, DAN-191, DAN-068, DAN-109, DAN-217
- justificativa: 
- aprofundar DAN-118: `atlassian april 2022 outage root cause fix customers lost access products` — Cento e poucos clientes perderam acesso a todos os produtos de uma vez, como no incidente atual; difere pelo prazo de restauração de até 14 dias.
- aprofundar DAN-067: `cloudflare control plane analytics outage root cause remediation power failure` — Falha no plano de controle pode derrubar todos os produtos de uma só vez, como no incidente atual; o sumário aponta falha de energia em data center terceirizado.
- aprofundar DAN-068: `cloudflare data center power failure breaker coordination root cause fix` — Perda completa de energia derrubou todos os serviços, compatível com perda de acesso a todos os produtos; difere por ser incidente de um único data center.
  - DAN-118 (llm) [Executive summary] 0.804: ## Executive summary  On Tuesday, April 5th, 2022, starting at 7:38 UTC, 775 Atlassian customers lost access to their Atlassian products. The outage spanned up to 14 days for a subset of these custome
  - DAN-118 (llm) [Table of contents] 0.732: ## Table of contents  ## Overview of Atlassian’s cloud architecture  To understand contributing factors to the incident as discussed throughout this document, it is helpful to first understand the dep
  - DAN-118 (causa) [How will we improve?] 0.465: ## How will we improve?  We have immediately blocked bulk sites deletes until appropriate changes can be made.  As we move forward from this incident and re-evaluate our internal processes, we want to
  - DAN-118 (correcao) [Workstream 3: Accelerated recovery and the Restoration 2 approach] 0.479: #### Workstream 3: Accelerated recovery and the Restoration 2 approach  **Timestamp: Days 4 – 13 (April 9th – 17th)**  With the Restoration 1 approach, it would have taken us three weeks to restore al
  - DAN-118 (correcao) [Learning 4: Improve our communications processes] 0.473: ### Learning 4: Improve our communications processes  **a) We deleted critical customer identifiers, impacting communications and actions to those affected**  The same script which deleted customer si
  - DAN-067 (llm) [sem seção] 0.813: Beginning on Thursday, November 2, 2023, at 11:43 UTC Cloudflare's control plane and analytics services experienced an outage. The control plane of Cloudflare consists primarily of the customer-facing
  - DAN-067 (llm) [Lessons and Remediation] 0.801: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-068 (llm) [What happened to the power in the data center?] 0.802: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [sem seção] 0.764: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (causa) [What happened to the power in the data center?] 0.502: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is

## q-222 (esperado: DAN-121)

- busca inicial: DAN-129, DAN-144, DAN-147, DAN-121, DAN-016, DAN-137, DAN-134, DAN-209, DAN-148, DAN-220
- justificativa: 
- aprofundar DAN-121: `database overloaded throttling requests services timing out fix` — Banco backend sobrecarregado limitando requisições e vários serviços com timeout, incluindo player de vídeo (iPlayer) — igual ao incidente atual.
- aprofundar DAN-147: `database capacity overload cascading failure request queue fix` — Fila de requisições sobrecarregando banco com capacidade insuficiente causando falha em cascata — similar, mas sem menção a player de vídeo.
- aprofundar DAN-129: `health check timeouts unresponsiveness fix postmortem` — Inresponsividade intermitente por timeouts muito baixos — gatilho diferente, menos parecido com banco sobrecarregado.
  - DAN-121 (llm) [sem seção] 0.496: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.46: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.61: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.597: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-129 (llm) [Health Check Timeouts] 0.771: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [Corrective Actions] 0.579: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (causa) [Conclusion] 0.457: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 
  - DAN-129 (correcao) [Load Planning] 0.361: ### Load Planning  We realized at the time of soft launch that we couldn’t cut-over to the new site without supporting the /universe endpoint. As such we held off on cutting over to get that implement

## q-223 (esperado: DAN-121)

- busca inicial: DAN-147, DAN-148, DAN-101, DAN-129, DAN-134, DAN-219, DAN-164, DAN-121, DAN-144, DAN-094
- justificativa: 
- aprofundar DAN-121: `database overload throttle requests services timing out fix` — Descreve banco de dados sobrecarregado throttling requisições e serviços de vídeo (iPlayer) com timeout — quase idêntico ao incidente atual.
- aprofundar DAN-147: `database capacity overload cascading failure fix` — Falha em cascata por fila de requisições sobrecarregando capacidade insuficiente do banco — mesmo mecanismo, contexto diferente.
- aprofundar DAN-164: `database overloaded influx requests outage fix` — Influx de requisições sobrecarregou o banco — mesmo gatilho, mas inclui exclusão acidental e perda de dados não relacionadas.
  - DAN-121 (llm) [sem seção] 0.493: Hi, I'm Richard Cooper, the BBC's Controller of Digital Distribution for BBC Future Media.  As many of you will have noticed we suffered a serious incident over the weekend which impacted BBC iPlayer,
  - DAN-121 (llm) [sem seção] 0.472: Our first priority was to restore the caching layer. The failure was a complex one (we’re still doing the forensics on it), and it has repeated a number of times. It was this failure that resulted in 
  - DAN-121 (causa) [sem seção] 0.348: We recognise that during this incident, with BBC iPlayer unavailable for some periods for some users you may not have been able to watch or listen to the programmes you wanted. I’m afraid we can’t sim
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.567: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.515: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-164 (llm) [Timeline] 0.643: ## Timeline  On January 31st an engineer started setting up multiple PostgreSQL servers in our staging environment. The plan was to try out pgpool-II to see if it would reduce the load on our database
  - DAN-164 (llm) [Root cause analysis] 0.642: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-224 (esperado: DAN-122)

- busca inicial: DAN-152, DAN-122, DAN-124, DAN-177, DAN-157, DAN-136, DAN-215, DAN-203, DAN-237, DAN-142
- justificativa: 
- aprofundar DAN-152: `npm account compromise malicious packages published root cause fix` — Bate: conta de mantenedor comprometida e pacotes maliciosos publicados em repositório público (npm), igual ao incidente atual. Não bate: é específico do ecossistema JavaScript/ESLint.
- aprofundar DAN-122: `malicious Maven packages JCenter impersonation attack root cause fix` — Bate: pacotes maliciosos em repositório público (JCenter) com ataque de personificação. Não bate: foco em pacotes Maven/Android, não necessariamente conta de desenvolvedor conhecido comprometida.
- aprofundar DAN-157: `GitHub organization compromise malicious commits root cause fix` — Bate: conta de desenvolvedor/organização comprometida para injetar código malicioso. Não bate: alvo é repositórios GitHub/commits, não pacotes publicados em nome de desenvolvedor.
  - DAN-152 (llm) [Summary] 0.745: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.732: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.747: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.661: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-157 (llm) [Incident summary] 0.682: ## Incident summary  An unknown entity gained control of an admin account for the Gentoo GitHub Organization and removed all access to the organization (and its repositories) from Gentoo developers. T
  - DAN-157 (llm) [2018-06-28] 0.673: ### 2018-06-28  Force-push.   - Same history as *gentoo/gentoo* in a squashed commit. - 21:00 (approx) GitHub informal report that they are starting to look - 21:05 Infra's formal ticket to GitHub Sup
  - DAN-157 (causa) [What went badly] 0.426: ### What went badly  - Initial communications were unclear and lacking detail in two areas.   - How can users verify their tree to be sure they had a clean copy?   - Clearer guidelines that even if us
  - DAN-157 (correcao) [Lessons] 0.478: ## Lessons  ### What went well  - Gentoo responded quickly to reports of problems. - GitHub responded quickly and had a function to hide the impacted organization. - Gentoo quickly removed account acc
  - DAN-157 (correcao) [Action items] 0.381: ## Action items  - Note: During the access revocation, some hosts were missed. - action-item: prod gentoo-infra members to start using local password managers (pass, gopass, etc.)   - *In-Progress: Dr

## q-225 (esperado: DAN-122)

- busca inicial: DAN-122, DAN-152, DAN-177, DAN-124, DAN-136, DAN-203, DAN-157, DAN-142, DAN-050, DAN-216
- justificativa: 
- aprofundar DAN-122: `malicious packages impersonation attack JCenter root cause fix` — Bate por ser repositório público de pacotes (JCenter/Maven) com ataque de personificação de desenvolvedor conhecido; não bate por ser ecossistema Android/Maven em vez do repositório do incidente atual.
- aprofundar DAN-152: `compromised maintainer npm account malicious package root cause fix` — Bate por conta de mantenedor público comprometida usada para publicar pacotes maliciosos no npm; não bate por ser invasão de conta em vez de personificação direta do nome do desenvolvedor.
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.774: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.691: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Summary] 0.729: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.722: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-226 (esperado: DAN-124)

- busca inicial: DAN-124, DAN-131, DAN-015, DAN-140, DAN-203, DAN-017, DAN-157, DAN-053, DAN-014, DAN-175
- justificativa: 
- aprofundar DAN-131: `malware stolen valid session unauthorized production access root cause fix` — Bate: credenciais válidas usadas para acesso não autorizado à produção. Não bate: roubo via malware em laptop, não chaves diretas.
- aprofundar DAN-175: `private tokens leaked unauthorized data access root cause fix` — Bate: tokens/chaves vazados permitindo acesso não autorizado. Não bate: foco em dados e repositórios, não acesso direto à produção.
- aprofundar DAN-124: `secret keys compromised production breach root cause fix` — Bate: chaves secretas expostas levando à violação da produção. Não bate: vulnerabilidade Shellshock em máquina protótipo antiga.
  - DAN-131 (llm) [What happened?] 0.6: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.553: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi
  - DAN-175 (llm) [Incident Summary] 0.566: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (llm) [Incident Summary] 0.558: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro
  - DAN-124 (llm) [Where did we go wrong?] 0.586: ## Where did we go wrong?  All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover,
  - DAN-124 (llm) [What happened?] 0.548: ## What happened?  BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was t
  - DAN-124 (causa) [BrowserStack Security Incident Report — November 2014 (Resolved)] 0.331: # BrowserStack Security Incident Report — November 2014 (Resolved)  Original Incident Statement — Published November 10, 2014  As you may already know, BrowserStack experienced an attack on 9th Novemb
  - DAN-124 (correcao) [Security measures taken to mitigate and prevent further incidents] 0.556: ## Security measures taken to mitigate and prevent further incidents  - After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an add
  - DAN-124 (correcao) [Security Evolution: 2014 → 2026] 0.407: ## Security Evolution: 2014 → 2026  This incident catalyzed a complete transformation of our security infrastructure. Here is what BrowserStack looks like today.  | Area | 2014 Status | 2026 Status (C

## q-227 (esperado: DAN-124)

- busca inicial: DAN-124, DAN-131, DAN-140, DAN-203, DAN-015, DAN-017, DAN-157, DAN-175, DAN-132, DAN-073
- justificativa: 
- aprofundar DAN-131: `malware session cookie theft valid SSO session production access remediation` — Bate pelo uso de credencial válida (sessão SSO com 2FA) para acessar produção de forma não autorizada; não bate por envolver malware em laptop do engenheiro, não chave direta.
- aprofundar DAN-124: `Shellshock prototype machine secret keys production breach remediation` — Bate por chaves secretas levarem a violação do sistema de produção; não bate por ser uma máquina protótipo antiga com vulnerabilidade Shellshock.
- aprofundar DAN-132: `MongoHQ breach valid tokens keys revocation remediation` — Bate por vazamento de chaves e tokens válidos (AWS IAM, SSH, OAuth) expostos em violação; não bate por ser banco de provedor externo, não acesso direto com chave própria.
  - DAN-131 (llm) [What happened?] 0.611: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.5: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi
  - DAN-124 (llm) [Where did we go wrong?] 0.574: ## Where did we go wrong?  All our servers, running or not, whether in active use or not, should have been patched with the latest security upgrades and updates including the shellshock one. Moreover,
  - DAN-124 (llm) [What happened?] 0.562: ## What happened?  BrowserStack application servers run using Amazon Web Services. The configuration is vast, consisting of thousands of servers. One of these was an old prototype machine, which was t
  - DAN-124 (causa) [BrowserStack Security Incident Report — November 2014 (Resolved)] 0.331: # BrowserStack Security Incident Report — November 2014 (Resolved)  Original Incident Statement — Published November 10, 2014  As you may already know, BrowserStack experienced an attack on 9th Novemb
  - DAN-124 (correcao) [Security measures taken to mitigate and prevent further incidents] 0.556: ## Security measures taken to mitigate and prevent further incidents  - After taking down the service, we revoked all the existing AWS keys and passwords, and generated new ones immediately, as an add
  - DAN-124 (correcao) [Security Evolution: 2014 → 2026] 0.407: ## Security Evolution: 2014 → 2026  This incident catalyzed a complete transformation of our security infrastructure. Here is what BrowserStack looks like today.  | Area | 2014 Status | 2026 Status (C
  - DAN-132 (llm) [Our response] 0.661: # Our response  To contain any potential risk we determined that the best course of action was to shutdown the CircleCI website and stop all builds. We also determined that it would be best to revoke 
  - DAN-132 (llm) [Our response] 0.654: # Our response  At 11:26pm we sent Heroku a list of all known SSH keys. We learned at 1:25pm today that those keys have all been revoked.  At 11:44pm we completed the process of deleting all our cache
  - DAN-132 (causa) [Incident details] 0.331: # Incident details  On Monday, October 28th, at 3:46pm Pacific, we noticed an IAM key had been deleted. We immediately searched for any evidence that our systems had been compromised, and to discover 
  - DAN-132 (correcao) [sem seção] 0.5: On October 29th, we received a notification email from our database provider telling us that they had been compromised. We later learned that our database was among those accessed by the attackers.  A
  - DAN-132 (correcao) [What you should do] 0.398: # What you should do  In order to protect your data and users, we strongly urge you to secure each of these systems:  - systems accessible by SSH keys uploaded to CircleCI - systems accessible using A

## q-228 (esperado: DAN-125)

- busca inicial: DAN-164, DAN-147, DAN-156, DAN-048, DAN-096, DAN-043, DAN-094, DAN-209, DAN-134, DAN-109
- justificativa: 
- aprofundar DAN-147: `insufficient database capacity cascading failure remediation fix` — Semelha por falha em cascata e capacidade insuficiente do banco sob carga, mas não menciona redução recente de tamanho.
- aprofundar DAN-096: `peak hour database cluster connection exhaustion root cause fix` — Semelha por carga de pico esgotando cluster de banco, mas mecanismo é ProxySQL/conexões, não redução de tamanho.
- aprofundar DAN-109: `cascading failure load metadata services remediation fix` — Semelha por falha em cascata sob carga, mas componente é serviço de metadados/DynamoDB, não banco relacional.
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.569: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.534: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.321: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-096 (llm) [March 17 13:46 UTC (lasting 2 hours and 28 minutes)] 0.698: ## March 17 13:46 UTC (lasting 2 hours and 28 minutes)  The following day, we saw the same peak traffic pattern and load on mysql1. We were not able to pinpoint and address the query performance issue
  - DAN-096 (llm) [March 22 15:53 UTC (lasting 2 hours and 53 minutes)] 0.652: ## March 22 15:53 UTC (lasting 2 hours and 53 minutes)  While we had reduced load seen in the previous incidents, we were not fully confident in the mitigations. We wanted to do more to analyze perfor
  - DAN-096 (causa) [March 23 14:49 UTC (lasting 2 hours and 51 minutes)] 0.429: ## March 23 14:49 UTC (lasting 2 hours and 51 minutes)  We again saw a recurrence of load characteristics that caused client connections to fail and again performed a primary failover in order to reco
  - DAN-096 (correcao) [Next steps] 0.497: ## Next steps  In order to prevent these types of incidents from occurring in the future, we have started an audit of load patterns for this particular database during peak hours and a series of perfo
  - DAN-096 (correcao) [In summary] 0.395: ## In summary  We sincerely apologize for the negative impacts these disruptions have caused. We understand the impact these types of outages have on customers who rely on us to get their work done ev
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.62: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  Initially, we were unable to add capacity to the metadata service because it was under such high load, 
  - DAN-109 (llm) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.575: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There’s one other bit worth mentioning. After we resolved the key issue on Sunday, we were left with a 
  - DAN-109 (causa) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  So, when the network disruption occurred on Sunday morning, and a number of storage servers simultaneou
  - DAN-109 (correcao) [Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region] 0.359: ### Summary of the Amazon DynamoDB Service Disruption and Related Impacts in the US-East Region  There are several actions we'll take immediately to avoid a recurrence of Sunday's DynamoDB event. Firs
  - DAN-109 (correcao) [Impact on Other Services] 0.345: ### Impact on Other Services  Between 2:15am PDT and 7:10am PDT, the EC2 Auto Scaling Service delivered significantly increased API faults. From 7:10am PDT to 10:52am PDT, the Auto Scaling service was

## q-229 (esperado: DAN-125)

- busca inicial: DAN-147, DAN-156, DAN-164, DAN-096, DAN-094, DAN-130, DAN-194, DAN-129, DAN-091, DAN-125
- justificativa: 
- aprofundar DAN-125: `database capacity downgrade cascading collapse dependent servers peak load root cause fix` — Menciona downgrade de capacidade do banco e colapso em cascata de servidores dependentes em horário de pico, exatamente como o incidente atual.
- aprofundar DAN-147: `cascading failure request queue insufficient database capacity root cause fix` — Descreve falha em cascata por fila de requisições sobrecarregando capacidade insuficiente do banco, embora não mencione redimensionamento explícito.
- aprofundar DAN-091: `primary database queued operations peak load could not catch up root cause fix` — Banco de dados principal ficou com fila de operações em carga de pico e não conseguiu se recuperar, sem menção a redução recente de capacidade.
  - DAN-125 (llm) [Database performance issues] 0.62: ## Database performance issues  We scheduled a maintenance window on the weekend to downgrade the database. The downgrade was successful and everything was looking great. The performance of the new da
  - DAN-125 (llm) [AWS issues prevented us from fixing anything] 0.537: ## AWS issues prevented us from fixing anything  After some time we were eventually able to upgrade the database to an instance type that could handle the load and roll out new servers that fixed self
  - DAN-125 (causa) [What a morning…] 0.436: ## What a morning…  The Buildkite team are currently based out of Melbourne, Australia — which meant we were all asleep when we first went offline (3:21 AM AEST). Usually if this happens our primary o
  - DAN-125 (correcao) [Moving forward] 0.469: ## Moving forward  Tim, Sam and I would like to personally apologise for the downtime. We know exactly what it’s like when services you rely upon have technical issues (AWS had problems when we were t
  - DAN-125 (correcao) [AWS issues prevented us from fixing anything] 0.367: ## AWS issues prevented us from fixing anything  Once we were all online and had finished identifying what the problems were, we decided the first thing we wanted to do was upgrade the database.  We l
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.615: ## Authentication Issues - DUO1  From that point, the DUO1 deployment was stable but traffic and load continued to grow. After further review of the data surrounding the incident, it was determined th
  - DAN-147 (llm) [Authentication Issues - DUO1] 0.597: ## Authentication Issues - DUO1  Now that we had a better understanding of what was causing these prolonged backups, we knew what to do. On August 29th, we implemented a max limit to this queue. If we
  - DAN-147 (causa) [Authentication Latency on DUO1 Deployment] 0.398: ## Authentication Latency on DUO1 Deployment  ## Postmortem  ## Authentication Issues - DUO1  Incident Report - 2018/08/29  Summary:  From 14:11 to 15:13 UTC on August 29th, 2018, the DUO1 deployment 
  - DAN-147 (correcao) [Authentication Issues - DUO1] 0.367: ## Authentication Issues - DUO1  - We’ve been actively re-architecting the database tier of our deployments so that we can home customers to a specific database server within a deployment. That way, w
  - DAN-147 (correcao) [Update] 0.323: ## Update  We're still monitoring an elevated number of slow and/or failed authentication requests affecting our DUO1 deployment. Our Engineering team is actively working to resolve this issue.  Poste
  - DAN-091 (llm) [Postmortem] 0.704: ## Postmortem  We identified a couple of changes that required additional work but had performed well in evaluation and rolled them back. Unfortunately, by that time the queued DB operations were back
  - DAN-091 (llm) [Linux build queue backing up] 0.652: ## Linux build queue backing up  ## Postmortem  CircleCI is a platform for continuous integration and continuous delivery. We take care of all the low-level details so that you have the simplest, fast
  - DAN-091 (causa) [Postmortem] 0.464: ## Postmortem  We've also moved over 50 percent of the data that was in our primary database onto its own deployment. The data was orthogonal and didn't need to be co-located, but its heavy use was ca
  - DAN-091 (correcao) [Resolved] 0.326: ## Resolved  We’re continuing to see builds running normally. We will be monitoring closely throughout the day. Please contact us in support if you’re seeing issues with your builds.  Posted Oct 15, 2
  - DAN-091 (correcao) [Postmortem] 0.423: ## Postmortem  Getting back to the architecture, we've known for a while that our queue model needs to be rebuilt and we've been laying the foundation to get there with the items outlined above, but w

## q-230 (esperado: DAN-126)

- busca inicial: DAN-126, DAN-076, DAN-059, DAN-106, DAN-211, DAN-127, DAN-216, DAN-145, DAN-146, DAN-116
- justificativa: 
- aprofundar DAN-126: `wrong timestamps bug fix data loss hotfix rollback` — É um jogo (Destiny 2) em que uma correção/hotfix causou perda de dados que reapareceu numa atualização seguinte, parecido com perda de itens após atualização, embora o gatilho sejam carimbos de data/hora.
- aprofundar DAN-076: `typo name conflict installer delete boot.ini expansion` — É um jogo (EVE Online) em que uma instalação de expansão apagou arquivos por erro de digitação/conflito de nome, semelhante à perda de dados após atualização, mas afeta boot.ini e não itens de jogador.
- aprofundar DAN-127: `problematic logging channel cluster nodes dying game patch` — É um jogo (EVE Online) em que um novo patch derruba nós de cluster por canal de log problemático, parecido pelo gatilho de atualização, mas causa indisponibilidade e não perda de itens/progresso.
  - DAN-126 (llm) [Server Configurations] 0.58: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (llm) [sem seção] 0.579: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’
  - DAN-126 (correcao) [Server Configurations] 0.372: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-076 (llm) [About the boot.ini issue] 0.693: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.681: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.711: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.699: # Behind the Scenes of a long EVE Online downtime  Via the console we modified the campaign loading functions so that they performed the load-from-DB operations normally, but all their logging operati
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan

## q-231 (esperado: DAN-126)

- busca inicial: DAN-126, DAN-059, DAN-076, DAN-127, DAN-146, DAN-058, DAN-145, DAN-116, DAN-142, DAN-043
- justificativa: 
- aprofundar DAN-126: `data loss bug fix hotfix game update rollback cause correction` — O incidente atual envolve perda de itens e progresso após atualização de jogo; DAN-126 envolve perda de dados após correção/hotfix que reapareceu em atualização seguinte, mas foca em configuração de servidor e timestamps, não especificamente itens de jogador.
- aprofundar DAN-127: `logging channel cluster nodes game patch downtime cause fix` — Ambos envolvem patches de jogos causando problemas após implantação, mas DAN-127 é sobre nós do cluster morrendo na sequência de inicialização, não perda de itens/progresso dos jogadores.
- aprofundar DAN-076: `typo name conflict installer boot.ini deletion expansion fix` — Ambos envolvem atualizações/expansões de jogo, mas DAN-076 é sobre instalador deletando arquivo boot.ini, não perda de itens/progresso durante o gameplay.
  - DAN-126 (llm) [sem seção] 0.644: Earlier today (Tuesday, February 11th), after the launch of Hotfix 2.7.1.1, we were made aware of the re-emergence of an issue which caused a small percentage of players to lose currency and materials
  - DAN-126 (llm) [Server Configurations] 0.63: ## Server Configurations  Unbeknownst to us, this crash resulted in those WorldServers **not** applying the previous character data corruption fix. This meant that a small percentage of WorldServers w
  - DAN-126 (causa) [Server Configurations] 0.393: ## Server Configurations  Once we determined this was the same issue that occurred on January 28th and we understood how it happened, the team decided that our best path forward – rather than trying t
  - DAN-126 (correcao) [Inventory Management] 0.393: ## Inventory Management  In Destiny 2, quests are treated similar to other inventory items, such as currency and materials. All items have a timestamp, based on when they were first added to a player’
  - DAN-126 (correcao) [Server Configurations] 0.372: ## Server Configurations  Before every major release (for example, Shadowkeep), we do comprehensive stress testing to try and model user behavior and its impact on our service architecture. Because th
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.719: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.717: # Behind the Scenes of a long EVE Online downtime  Via the console we modified the campaign loading functions so that they performed the load-from-DB operations normally, but all their logging operati
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan
  - DAN-076 (llm) [About the boot.ini issue] 0.723: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.701: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 

## q-232 (esperado: DAN-127)

- busca inicial: DAN-127, DAN-211, DAN-219, DAN-210, DAN-208, DAN-103, DAN-145, DAN-066, DAN-094, DAN-151
- justificativa: 
- aprofundar DAN-127: `logging channel cluster start sequence game patch root cause fix` — Mesmo cenário: novo patch do jogo e nós do cluster morrem na sequência de inicialização, impedindo o servidor de subir.
- aprofundar DAN-210: `Kubernetes cluster upgrade node metadata networking failure fix` — Falha de cluster após upgrade/patch que derruba nós; difere por ser metadados do Kubernetes, não patch de jogo.
- aprofundar DAN-208: `Zookeeper too much data boot failure maintenance fix` — Serviço não consegue inicializar após janela de manutenção; difere por ser volume de dados no Zookeeper, não patch de jogo.
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.64: # Behind the Scenes of a long EVE Online downtime  We had prepared a series of escalating steps that we intended to follow. Each one would progressively add more factors in to the mix, until the issue
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.636: # Behind the Scenes of a long EVE Online downtime  Via the console we modified the campaign loading functions so that they performed the load-from-DB operations normally, but all their logging operati
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan
  - DAN-210 (llm) [Get to the Point, Spock, If You Have One] 0.666: ## Get to the Point, Spock, If You Have One  How did it actually break? That’s one of the most unexpected things of all. In doing the research, we discovered that the way that the route reflectors wer
  - DAN-210 (llm) [It Begins] 0.662: ## It Begins  All at once the site came to a screeching halt. We opened an incident immediately, and brought all hands on deck, trying to figure out what had happened. Hands were on deck and in the ca
  - DAN-210 (causa) [A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack] 0.526: ## A little self-reflection; or, a needle in a 3.9 Billion Log Line Haystack  Further investigation kicked off. We started looking at everything we could think of to try and narrow down the exact mome
  - DAN-210 (correcao) [It Begins] 0.466: ## It Begins  We are sufficiently paranoid, so of course our upgrade procedure includes taking a backup as standard. However, this backup procedure, and the restore, were written several years ago. Wh
  - DAN-210 (correcao) [TL;DR] 0.449: ## TL;DR  - Upgrades, particularly to our Kubernetes clusters, are risky for us, but we must do them anyway. We test and validate them in advance as best we can, but we still have plenty of work to do
  - DAN-208 (llm) [Read the socket] 0.718: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (llm) [Wrapping up] 0.689: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\

## q-233 (esperado: DAN-127)

- busca inicial: DAN-127, DAN-211, DAN-148, DAN-070, DAN-103, DAN-210, DAN-094, DAN-208, DAN-219, DAN-029
- justificativa: 
- aprofundar DAN-127: `logging channel cluster nodes dying start sequence patch root cause fix` — Batem: novo patch de game e nós do cluster morrem durante a sequência de inicialização do cluster. Pode não bater: o componente culpado (canal de logging) pode ser diferente do incidente atual.
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.675: # Behind the Scenes of a long EVE Online downtime  | 1 2 3 4 5 | # Step 2a: Log the same line 500 times per node, on the generic log channel \[generic\_logger.warn('The quick brown fox jumps over the 
  - DAN-127 (llm) [Behind the Scenes of a long EVE Online downtime] 0.648: # Behind the Scenes of a long EVE Online downtime  We had prepared a series of escalating steps that we intended to follow. Each one would progressively add more factors in to the mix, until the issue
  - DAN-127 (causa) [Behind the Scenes of a long EVE Online downtime] 0.492: # Behind the Scenes of a long EVE Online downtime  Unfortunately, 2 startups later, we were no closer to having a healthy server online, so it was time to call in the cavalry. EVE programmers joined O
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.413: # Behind the Scenes of a long EVE Online downtime  Hotfix #5 was requested at 21.48, containing what we believed would mitigate the issue. All logging within the campaign system was entirely removed, 
  - DAN-127 (correcao) [Behind the Scenes of a long EVE Online downtime] 0.382: # Behind the Scenes of a long EVE Online downtime  We tried a few long shots over the next hour as developers continued their investigations. Our next idea came at 15.29, when EVE Dev presented a plan

## q-234 (esperado: DAN-129)

- busca inicial: DAN-129, DAN-209, DAN-119, DAN-224, DAN-011, DAN-073, DAN-035, DAN-205, DAN-162, DAN-116
- justificativa: 
- aprofundar DAN-129: `health check timeouts post launch latency fix root cause` — Bate perfeitamente: site caiu duas horas após o lançamento com latência alta e inresponsividade intermitente, exatamente como o atual; a causa apontada foi timeouts muito baixos de health check, o que explica instâncias marcadas como não saudáveis.
- aprofundar DAN-224: `regex backtracking health check failures outage postmortem fix` — Bate em health-check failures levando a outage e instâncias não saudáveis; não bate no gatilho (regex em post, não lançamento de site).
- aprofundar DAN-035: `load balancer configuration rollout increased error rates fix` — Bate em configuração de load balancer causando erros após mudança; não bate nos sintomas de lançamento, latência alta e health checks específicos.
  - DAN-129 (llm) [Health Check Timeouts] 0.709: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [sem seção] 0.557: Approximately two hours after Supermarket became the official community site it started to experience increased latency and intermittent unresponsiveness. This made downloading cookbooks problematic a
  - DAN-129 (causa) [Conclusion] 0.457: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (correcao) [Corrective Actions] 0.447: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 
  - DAN-224 (llm) [Follow-up Actions] 0.66: # Follow-up Actions  - Audit our regular expressions and post validation workflow for any similar issues - Add controls to our load balancer to disable the healthcheck – as we believe everything but t
  - DAN-224 (llm) [Overview] 0.643: # Overview  On July 20, 2016 we experienced a 34 minute outage starting at 14:44 UTC. It took 10 minutes to identify the cause, 14 minutes to write the code to fix it, and 10 minutes to roll out the f
  - DAN-224 (causa) [Technical Details] 0.25: # Technical Details  The regular expression was: `^[\s\u200c]+|[\s\u200c]+$` Which is intended to trim unicode space from start and end of a line. A simplified version of the Regex that exposes the sa
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.799: ## Update — Apr 12, 2017 14:11  ISSUE SUMMARY  On Wednesday 5 April 2017, requests to the Google Cloud HTTP(S) Load Balancer experienced a 25% error rate for a duration of 22 minutes.  We apologize fo
  - DAN-035 (llm) [Update — Apr 12, 2017 14:11] 0.756: ## Update — Apr 12, 2017 14:11  The configuration update process is controlled by a master server. In this case, one of the replicas of the master servers lost access to Google's distributed file syst
  - DAN-035 (causa) [Update — Apr 12, 2017 14:11] 0.36: ## Update — Apr 12, 2017 14:11  To prevent incidents of this type in future, we are taking the following actions:  - Master servers will be configured to never push HTTP(S) Load Balancer configuration

## q-235 (esperado: DAN-129)

- busca inicial: DAN-129, DAN-218, DAN-205, DAN-011, DAN-209, DAN-148, DAN-073, DAN-035, DAN-133, DAN-211
- justificativa: 
- aprofundar DAN-129: `health check timeout low root cause fix supermarket launch latency` — Bate com o incidente atual: lançamento recente, duas horas após, latência alta, intermitência e instâncias unhealthy por health check. Não bate: componente específico (site de receitas Chef) e não menciona correção exata no resumo.
  - DAN-129 (llm) [Health Check Timeouts] 0.741: ### Health Check Timeouts  The health check timeouts were set too low to be effective. We ended up in a state where nodes were being taken out of the pool causing a domino effect. As one node would be
  - DAN-129 (llm) [Conclusion] 0.643: ## Conclusion  We are sorry about the issues with Supermarket, especially so soon after launch. We know that the community depends on these services to be reliable and will work hard to prevent these 
  - DAN-129 (causa) [Contributing Factors] 0.456: ## Contributing Factors  The supermarket application runs in an AWS account. At launch, it was hosted on three m3.medium instances, with an RDS database, ElasticCache Redis cache, with an Elastic Load
  - DAN-129 (correcao) [Corrective Actions] 0.447: ## Corrective Actions  1. Change the behavior of the Berkshelf API Servers, to use the new `/universe` endpoint. (Berkshelf Core Team) 2. Adjust the number of unicorn workers on each node as necessary
  - DAN-129 (correcao) [Background] 0.483: ## Background  At Chef, we perform a postmortem for any significant production environment outage or incident that results in an engineer being paged. We have a postmortem writeup, with the timeline, 

## q-236 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-029, DAN-048, DAN-217, DAN-078, DAN-221, DAN-164, DAN-210
- justificativa: 
- aprofundar DAN-145: `Redis primary failover cluster rebalance cascading connection failure fix` — Bate quase exatamente: Redis primário de um cluster HA caiu, o cluster rebalanceou e houve falha em cascata nas conexões. Não bate: o gatilho foi migração automática da GCP, não uma queda espontânea.
- aprofundar DAN-234: `Redis cluster network partition resynchronization master crash read-only fix` — Bate por envolver Redis cluster e queda do master, mas não bate: o foco é faturamento, resincronização de escravos e modo só-leitura, não rebalanceamento de cluster nem falha em cascata de conexões de usuário.
- aprofundar DAN-217: `massive disconnection reconnection cascading connection failures database capacity fix` — Bate por descrever falha em cascata de conexões após desconexões em massa, mas não bate: a causa é capacidade do banco de dados, não Redis primário caindo com rebalanceamento de cluster.
  - DAN-145 (llm) [Sequence of Events] 0.713: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.685: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-234 (llm) [What We’re Doing About It] 0.616: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Root Cause] 0.593: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (causa) [Root Cause] 0.489: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Timeline] 0.413: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn
  - DAN-217 (llm) [TUESDAY] 0.763: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [sem seção] 0.552: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [WEDNESDAY] 0.429: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou

## q-237 (esperado: DAN-145)

- busca inicial: DAN-145, DAN-234, DAN-066, DAN-048, DAN-029, DAN-070, DAN-096, DAN-210, DAN-078, DAN-221
- justificativa: 
- aprofundar DAN-145: `Redis primary failover cluster rebalance cascading connection failure fix` — Mesmo padrão: queda do Redis primário, rebalanceamento do cluster e falha em cascata nas conexões de usuários em todo o sistema.
- aprofundar DAN-234: `Redis cluster network partition resync master crash recovery fix` — Falha em cluster Redis com efeitos em cascata, mas o gatilho é partição de rede e o escopo é cobrança, não todo o sistema.
- aprofundar DAN-070: `Redis cluster restoration power outage recovery fix` — Menciona Redis clusters indisponíveis que precisaram ser restaurados, mas a causa foi perda de energia, não failover ou rebalanceamento.
  - DAN-145 (llm) [Sequence of Events] 0.713: ## Sequence of Events  - 14:01 - Discord engineers are alerted to anomalies via our real time metrics and monitoring  - 14:01 - Initial investigation points to a Redis instance for a highly available 
  - DAN-145 (llm) [Action Items / Response] 0.685: ## Action Items / Response  - We’ve increased the priority of fixing the known issues with Redis failovers. We hope to accomplish this within the coming weeks to avoid further problems caused by indiv
  - DAN-145 (causa) [Investigation and Analysis] 0.521: ## Investigation and Analysis  The root cause of this issue was something we expect our services to handle correctly—an outage of one node within a highly available cluster. Despite this expectation, 
  - DAN-145 (correcao) [Sequence of Events] 0.439: ## Sequence of Events  - Engineers realize that due to human error, an important API setting for allowing users to quickly and safely reconnect to Discord is improperly set.  - This improperly configu
  - DAN-145 (correcao) [Update] 0.423: ## Update  After engineers were alerted to similar issues on Saturday (by alerts added due to the findings of this post-mortem), they were able to safely decommission and investigate a node experienci
  - DAN-234 (llm) [What We’re Doing About It] 0.628: ## What We’re Doing About It  In the process of resolving the incident, we replaced the original redis cluster that triggered the incident. The incorrect configuration for redis-master was identified 
  - DAN-234 (llm) [Timeline] 0.596: ## Timeline  July 18, 2013  - 1:35 AM PDT / 8:35 UTC: We experienced a loss of network connectivity between all of our billing redis-slaves and our redis-master. This caused all redis-slaves to reconn
  - DAN-234 (causa) [Root Cause] 0.57: ## Root Cause  Twilio’s billing system uses an in-memory Redis cluster to store in-flight account balances. This cluster is configured with a single master and multiple slaves distributed across data-
  - DAN-234 (correcao) [Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause] 0.454: ## Billing Incident Post-Mortem: Breakdown, Analysis and Root Cause  Time to read:  July 23, 2013  Written by  Twilio  Twilion  Twilio experienced an incident with its billing system on July 18, 2013.
  - DAN-234 (correcao) [Root Cause] 0.439: ## Root Cause  With all account balances at zero and read-only, Twilio usage that resulted in a billing transaction (e.g. 1 cent for a SMS message or a phone call) triggered the billing system to atte
  - DAN-070 (llm) [The Event] 0.772: ## The Event  By this point, we had a fairly clear picture of what was required to restore service and began working towards that end. We needed to repair our servers that were not booting, and we nee
  - DAN-070 (llm) [The Event] 0.642: ## The Event  Initial notifications for unreachable servers and a spike in exceptions related to Redis connectivity directed our team to investigate a possible outage in our internal network. We also 
  - DAN-070 (causa) [Future Work] 0.507: ## Future Work  Complex systems are defined by the interaction of many discrete components working together to achieve an end result. Understanding the dependencies for each component in a complex sys
  - DAN-070 (correcao) [Future Work] 0.534: ## Future Work  A number of less technical improvements are also being implemented. Strengthening our cross-team communications would have shaved minutes off the recovery time. Predefining escalation 
  - DAN-070 (correcao) [In Conclusion] 0.461: ## In Conclusion  We realize how important GitHub is to the workflows that enable your projects and businesses to succeed. All of us at GitHub would like to apologize for the impact of this outage. We

## q-238 (esperado: DAN-148)

- busca inicial: DAN-148, DAN-106, DAN-217, DAN-191, DAN-067, DAN-066, DAN-221, DAN-209, DAN-109, DAN-144
- justificativa: 
- aprofundar DAN-148: `root cause fix concurrent users peak service disruption` — Bate com o incidente atual: pico recorde de usuários simultâneos causando disrupções parciais e totais; não necessariamente bate se a causa for específica de plataforma de jogos.
- aprofundar DAN-217: `root cause fix database capacity cascading connection failures` — Bate com desconexões em massa excedendo capacidade e falhas em cascata; não bate porque o gatilho inicial não é um pico recorde de usuários simultâneos.
- aprofundar DAN-144: `root cause fix thundering herd reconnect memory queue` — Bate com enxame de reconexões sobrecarregando serviços e falha em cascata; não bate porque a origem é um serviço flapping, não um pico de CCU.
  - DAN-148 (llm) [**Account Service outage**] 0.61: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (llm) [**XMPP outage**] 0.606: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (causa) [Postmortem of Service Outage at 3.4M CCU] 0.45: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme
  - DAN-217 (llm) [TUESDAY] 0.633: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [MONDAY] 0.476: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (causa) [WEDNESDAY] 0.41: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (correcao) [sem seção] 0.375: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou
  - DAN-144 (llm) [Investigation and Analysis] 0.559: ## Investigation and Analysis  While we’ve invested immense effort and engineering in scaling and improving the performance of many core services and database over the past months, we’ve also seen imm
  - DAN-144 (llm) [Summary] 0.554: ## Summary  At 11:38 on March 20, a server for one of the internal services (presence) at Discord which tracks real time state and presence information for all connected users, disconnected from its o
  - DAN-144 (causa) [Investigation and Analysis] 0.455: ## Investigation and Analysis  The initial issue which caused this outage can be boiled down to the CPU soft lockups that we observed on the individual presence server. Although we’ve previously seen 
  - DAN-144 (correcao) [Action Items / Response] 0.441: ## Action Items / Response  During the outage, engineers were able to roll out upgrades to our presence server (which had previously been untouched for almost a year). These changes fix the split-brai
  - DAN-144 (correcao) [Resolved] 0.382: ## Resolved  We look to be back to nominal operation. We've isolated the issue to within the GCP hypervisor causing a soft-cpu lock on one of our services - causing a cascading failure throughout our 

## q-239 (esperado: DAN-148)

- busca inicial: DAN-148, DAN-209, DAN-001, DAN-067, DAN-066, DAN-217, DAN-106, DAN-109, DAN-191, DAN-208
- justificativa: 
- aprofundar DAN-148: `concurrent user peak service disruption root cause fix mitigation` — Corresponde quase exatamente: pico recorde de usuários concorrentes causando interrupções parciais e totais, igual ao incidente atual.
- aprofundar DAN-001: `traffic spike cluster resource management configuration error fix` — Também envolve pico de tráfego e queda de serviços, embora a causa seja erro de configuração em gerenciamento de cluster, não apenas carga.
- aprofundar DAN-217: `database capacity cascading connection failures disconnection reconnection fix` — Envolve falha em cascata sob carga massiva de usuários, mas o gatilho é processo de reconexão, não um pico direto de concorrência.
  - DAN-148 (llm) [**Account Service outage**] 0.642: ### **Account Service outage**  Below is a quick post-mortem summary: - Timeline: 	  - 2018-02-04 18:30 UTC - 2018-02-04 20:20 UTC - Root cause: 	  - Nginx in front of the Java application was saturat
  - DAN-148 (llm) [Postmortem of Service Outage at 3.4M CCU] 0.64: # Postmortem of Service Outage at 3.4M CCU  However once deployed to our live environment, we noticed requests experiencing increased latency (double ms average to double seconds) that was not present
  - DAN-148 (causa) [**XMPP outage**] 0.495: ### **XMPP outage**  On Sunday we had a situation while mitigating a known instability problem that resulted in overloading a downstream system component and effectively paralyzing presence flow.  Wit
  - DAN-148 (correcao) [**Cloud capacity limits and throttling**] 0.387: ### **Cloud capacity limits and throttling**  - **Rearchitecting our core messaging stack.** Our stack wasn’t architected to handle this scale and we need to look at larger changes in our architecture
  - DAN-148 (correcao) [**XMPP outage**] 0.374: ### **XMPP outage**  And at 22:00 UTC on Sunday we started losing cluster nodes and disconnecting players.   - A decision was made to immediately failover to a stand-by cluster via green/blue deployme
  - DAN-001 (llm) [Analysis #] 0.683: ## Analysis #  What is going on inside a service which experiences traffic higher than it can handle with available resources? As response times increase, the autoscaler tries to scale up the service.
  - DAN-001 (llm) [Outage timeline #] 0.678: ## Outage timeline #  Also just before noon, traffic peaked at 200%-300% of the traffic from previous day, depending on service. At this stage, traffic was at its highest but due to excessive resource
  - DAN-001 (causa) [sem seção] 0.512: We messed up. On July 18th, 2018, at noon, Allegro went down and was unavailable for twenty minutes. The direct cause was a special offer in which one hundred Honor 7C phones whose regular price is ar
  - DAN-001 (correcao) [Closing remarks #] 0.392: ## Closing remarks #  I think that despite the outage taking place, the way we handled it validated our approach to architecture. Thanks to the cloud, we were able to scale out all critical services a
  - DAN-001 (correcao) [Analysis #] 0.385: ## Analysis #  In most cases, requests which time out, are repeated after a short delay. Under normal conditions, the second or third attempt usually succeeds, so these retries can often fix the situa
  - DAN-217 (llm) [TUESDAY] 0.725: ### TUESDAY  - We undertook some routine maintenance, during which, as a result of an automation malfunction, corrupted code was deployed to our web servers and “job queue workers” (machines which pro
  - DAN-217 (llm) [WEDNESDAY] 0.5: ### WEDNESDAY  - Late on Tuesday night, Google released a statement about the POODLE vulnerability, which necessitated a disabling of SSLv3, as reflected in our tweet at the time. - We reconfigured in
  - DAN-217 (causa) [MONDAY] 0.435: ### MONDAY  - A portion of the internal network of our hosting provider suddenly became unavailable. Most of the affected machines were in our search clusters. - This caused a large backlog of message
  - DAN-217 (correcao) [sem seção] 0.375: It’s been a rough couple of days at Slack HQ. We’ve had two separate incidents where too many users were unable to connect for too long a time. Firstly, and most importantly, we want to apologize. Whi
  - DAN-217 (correcao) [sem seção] 0.324: Slack has grown extremely quickly. With the exception of national holidays, we’ve broken a usage record every single day for the last year (every Monday has been our best-ever Monday, every Tuesday ou

## q-240 (esperado: DAN-152)

- busca inicial: DAN-009, DAN-175, DAN-140, DAN-152, DAN-177, DAN-015, DAN-017, DAN-124, DAN-131, DAN-028
- justificativa: 
- aprofundar DAN-152: `malicious package compromised account npm registry access token exfiltration fix` — Envolve pacotes maliciosos publicados em registro público via conta de mantenedor comprometida, parecido com um pacote não nosso enviando tokens, embora o alvo seja de terceiros.
- aprofundar DAN-009: `service token code release error fix root cause` — Envolve service tokens e falha no release de código, mas não trata de pacote malicioso publicado por terceiros.
- aprofundar DAN-131: `malware session cookie theft token exfiltration fix root cause` — Envolve roubo de tokens de sessão por malware, mas ocorre em laptop de funcionário e não por meio de um pacote publicado.
  - DAN-152 (llm) [Timeline] 0.756: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (llm) [Summary] 0.747: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-009 (llm) [How did we fix the issue?] 0.649: ### How did we fix the issue?  As a temporary solution, we were able to manually restore the correct service token values for the accounts with overwritten service tokens. This stopped the immediate i
  - DAN-009 (llm) [sem seção] 0.643: Several Cloudflare services became unavailable for 121 minutes on January 24, 2023 due to an error releasing code that manages service tokens. The incident degraded a wide range of Cloudflare products
  - DAN-009 (causa) [Cloudflare R2 Storage and Cache Reserve] 0.368: ### Cloudflare R2 Storage and Cache Reserve  Cloudflare R2 Storage allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud 
  - DAN-009 (correcao) [What are we doing to prevent this from happening again?] 0.539: ### What are we doing to prevent this from happening again?  We take incidents like this seriously and recognize the impact it had. We have identified several steps we can take to address the risk of 
  - DAN-009 (correcao) [Incident Timeline] 0.424: ### Incident Timeline  At 2023-01-24 18:56 The same solution was implemented on the Cloudflare API account, impacting Cache Purge, Cache Reserve, Images and R2. **Impact ended for Cache Purge, Cache R
  - DAN-131 (llm) [What happened?] 0.625: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.556: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi

## q-241 (esperado: DAN-152)

- busca inicial: DAN-152, DAN-009, DAN-015, DAN-177, DAN-140, DAN-017, DAN-122, DAN-131, DAN-175, DAN-204
- justificativa: 
- aprofundar DAN-152: `compromised npm account malicious package publish root cause fix` — O atacante publicou pacotes maliciosos via conta de mantenedor comprometida, igual a versão não publicada que exfiltra tokens; diferença: alvo é npm, não nosso pacote.
- aprofundar DAN-122: `malicious Maven packages impersonation JCenter root cause fix` — Pacotes maliciosos entraram num registro por ataque de personificação, vetor de cadeia de suprimentos parecido; diferença: ecossistema Maven/Android, não npm.
- aprofundar DAN-177: `leaked GitHub token unauthorized git push root cause fix` — Token vazado permitiu push não autorizado de código, análogo à publicação não autorizada do pacote; diferença: alvo são repositórios Git, não pacote publicado.
  - DAN-152 (llm) [Summary] 0.761: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.749: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.735: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.669: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-177 (llm) [sem seção] 0.707: On 31st July 2018 a security researcher identified a GitHub personal access token with recently elevated scopes was leaked from Homebrew’s Jenkins that gave them access to git push on Homebrew/brew an
  - DAN-177 (llm) [What was impacted] 0.637: ## What was impacted  GitHub Support was contacted and they verified the relevant token had not been used to perform any pushes to Homebrew/brew or Homebrew/homebrew-core during the period of elevated
  - DAN-177 (causa) [What we’re doing about it] 0.231: ## What we’re doing about it  - We have for several years enabled 2FA and third party application restrictions for the entire Homebrew GitHub organisation. This was also recommended by the security re

## q-242 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-109, DAN-026, DAN-129, DAN-145, DAN-106, DAN-009, DAN-008, DAN-067, DAN-016
- justificativa: 
- aprofundar DAN-011: `database permissions file output limit systemwide outage fix rollback` — Bate: outage sistêmico repentino em CDN/cloud com arquivo se propagando pela rede; não bate: causa é banco de dados de bot-detection, não CDN direto.
- aprofundar DAN-016: `DDoS mitigation rule rate limiting cookie validation infinite loop CPU fix` — Bate: erro se propagando por data centers afetando serviço global; não bate: origem é regra de mitigação DDoS, não queda total de CDN.
- aprofundar DAN-008: `Tiered Cache change 530 error fix rollback` — Bate: mudança em sistema de cache/CDN causando erros em requests; não bate: impacto foi parcial (5%), não mundial e total.
  - DAN-011 (llm) [The query behaviour change] 0.563: ### The query behaviour change  ``` SELECT   name,   type FROM system.columns WHERE   table = 'http_requests_features' order by name; ``` Note how the query does not filter for the database name. With
  - DAN-011 (llm) [Memory preallocation] 0.528: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.532: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.751: ## Technical description of the error and how it happened  1. The rate-limit rules generated by the DDoS logic are using internal APIs in ways that haven't been anticipated. This caused the `parent_ke
  - DAN-016 (llm) [Technical description of the error and how it happened] 0.715: ## Technical description of the error and how it happened  ``` for (rule in active_mitigations) {    // ... (ignore other rule types)    if (rule.match_current_request()) {        if (!has_valid_cooki
  - DAN-016 (causa) [Technical description of the error and how it happened] 0.444: ## Technical description of the error and how it happened  1. The increase in CPU utilization for the server causes Unimog to lower the amount of new traffic that server receives, moving traffic to ot
  - DAN-016 (correcao) [Remediation and follow-up steps] 0.472: ## Remediation and follow-up steps  To resolve the immediate impact to our network from the request poisoning, Cloudflare instigated mass rolling restarts of the affected service until the change that
  - DAN-016 (correcao) [Conclusion] 0.488: ## Conclusion  Cloudflare experienced two back-to-back incidents that affected a significant set of customers using our CDN and network services. The first was network backbone congestion that our sys
  - DAN-008 (llm) [sem seção] 0.75: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.696: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac

## q-243 (esperado: DAN-154)

- busca inicial: DAN-011, DAN-067, DAN-026, DAN-008, DAN-210, DAN-209, DAN-205, DAN-129, DAN-109, DAN-145
- justificativa: 
- aprofundar DAN-011: `bot detection permissions file limit systemwide outage fix rollback` — É uma queda sistêmica/worldwide da Cloudflare (CDN) causada por uma mudança que se propagou pela rede, batendo com a queda mundial de CDN; não confirma se o componente é exatamente cache de CDN.
- aprofundar DAN-008: `Tiered Cache change 530 error root cause rollback fix` — É uma falha no componente Tiered Cache da Cloudflare (CDN) que fez requisições retornarem erro, batendo com servidor retornando erros, mas foi parcial (~5%) e não mundial.
- aprofundar DAN-026: `DNS Puppet manifest nameserver corrupt zone outage root cause fix` — Falha de DNS causou timeouts e erros generalizados nos servidores, parecido com 'servidores retornando erros', mas não é especificamente uma queda de CDN.
  - DAN-011 (llm) [Remediation and follow-up steps] 0.687: ## Remediation and follow-up steps  Although the issue was also present in prior versions of our proxy, the impact was smaller as described below. | | 13:37 | Work focused on rollback of the Bot Manag
  - DAN-011 (llm) [Memory preallocation] 0.59: ### Memory preallocation  Each module running on our proxy service has a number of limits in place to avoid unbounded memory consumption and to preallocate memory as a performance optimization. In thi
  - DAN-011 (causa) [The outage] 0.431: ## The outage  The chart below shows the volume of 5xx error HTTP status codes served by the Cloudflare network. Normally this should be very low, and it was right up until the start of the outage.  T
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.486: ## Remediation and follow-up steps  Now that our systems are back online and functioning normally, work has already begun on how we will harden them against failures like this in the future. In partic
  - DAN-011 (correcao) [Remediation and follow-up steps] 0.476: ## Remediation and follow-up steps  | Time (UTC) | Status | Description | |---|---|---| | 11:05 | Normal. | Database access control change deployed. | | 11:28 | Impact starts. | Deployment reaches cus
  - DAN-008 (llm) [sem seção] 0.751: *This post is also available in 简体中文, 日本語, Français, Deutsch and Español.*  Today, a change to our Tiered Cache system caused some requests to fail for users with status code 530. The impact lasted fo
  - DAN-008 (llm) [Conclusion] 0.689: ### Conclusion  We experienced an incident that affected a significant set of customers using Tiered Cache. After identifying the faulty component, we were able to quickly rollback and remediate the i
  - DAN-008 (causa) [Incident timeline and impact] 0.429: ### Incident timeline and impact  - 2022-10-25 08:40: The release started to roll out to a small subset of data centers. - 2022-10-25 10:35: An individual customer alert fires, indicating an increase 
  - DAN-008 (correcao) [Remediation and follow-up steps] 0.468: ### Remediation and follow-up steps  To prevent this from happening again, in addition to the fixing the bug, we have identified a set of changes that help us detect and prevent issues like this in th
  - DAN-008 (correcao) [Incident timeline and impact] 0.39: ### Incident timeline and impact  At 08:40 UTC, a software release of a CDN component containing a bug began slowly rolling out. The bug was triggered when a user visited a site with either Tiered Cac
  - DAN-026 (llm) [What happened…] 0.726: # What happened…  In order to roll out these changes, we had prepared changes to our firewall and router configuration to update the IP addresses our name servers used to send queries and receive resp
  - DAN-026 (llm) [What happened…] 0.713: # What happened…  Our caching and authoritative name servers were reloaded at 13:49 PST, resolving DNS query timeouts. However, we observed that certain queries were now incorrectly returning `NXDOMAI
  - DAN-026 (causa) [Total number of processes across fileservers] 0.487: ### Total number of processes across fileservers  ### Total memory footprint across fileservers  The failing fileservers began creating a back pressure in our routing layer that prevented connections 
  - DAN-026 (correcao) [What we’re doing about it…] 0.426: # What we’re doing about it…  This small problem uncovered quite a bit about our infrastructure that we will be critically reviewing over the next few weeks. This includes:  1. We are investigating fu
  - DAN-026 (correcao) [What we’re doing about it…] 0.417: # What we’re doing about it…  During the failure when filesevers became so exhausted that the routing layer failed due to back pressure, we should have seen several protective measures kick in to auto

## q-244 (esperado: DAN-165)

- busca inicial: DAN-165, DAN-195, DAN-231, DAN-124, DAN-184, DAN-221, DAN-033, DAN-183, DAN-164, DAN-001
- justificativa: 
- aprofundar DAN-165: `repeated email batch cron job non-atomic root cause fix mark sent waiting` — Bate: e-mail enviado dezenas de vezes para mesma pessoa por job em lote não atômico. Não bate: contexto é Google Code Jam, não o sistema de e-mail atual.
  - DAN-165 (llm) [So what was the bug?] 0.701: ## So what was the bug?  In the App Engine datastore, we have an object called a "notification". That notification has a "status" property, which takes on the following values: "Waiting", "Sending", a
  - DAN-165 (llm) [sem seção] 0.571: A few hours ago, the automated email system for Code Jam went a little bit crazy. I'll write about the technical details below, but the short version is that it sent an email titled "Registration Now 
  - DAN-165 (causa) [Why did I get the repeated email at all?] 0.284: ## Why did I get the repeated email at all?  We sent the notification email to users who registered for Code Jam 2013, checked the box saying "I would like to receive email notifying me about the next
  - DAN-165 (correcao) [Why does Code Jam have its own email system?] 0.272: ## Why does Code Jam have its own email system?  To automatically identify the users who should get an email based on Code Jam-specific properties (such as scores, booleans in user profiles, and regis

## q-245 (esperado: DAN-165)

- busca inicial: DAN-165, DAN-183, DAN-231, DAN-124, DAN-195, DAN-033, DAN-221, DAN-164, DAN-184, DAN-016
- justificativa: 
- aprofundar DAN-165: `batch cron job repeated email non-atomic waiting mark sent root cause fix` — Bate exatamente: mesmo sintoma (mesmo e-mail dezenas de vezes) e mesmo componente (sistema de e-mail/lote). Não bate: é um caso do Google Code Jam, não necessariamente o mesmo stack.
  - DAN-165 (llm) [So what was the bug?] 0.742: ## So what was the bug?  In the App Engine datastore, we have an object called a "notification". That notification has a "status" property, which takes on the following values: "Waiting", "Sending", a
  - DAN-165 (llm) [sem seção] 0.59: A few hours ago, the automated email system for Code Jam went a little bit crazy. I'll write about the technical details below, but the short version is that it sent an email titled "Registration Now 
  - DAN-165 (causa) [Why did I get the repeated email at all?] 0.284: ## Why did I get the repeated email at all?  We sent the notification email to users who registered for Code Jam 2013, checked the box saying "I would like to receive email notifying me about the next
  - DAN-165 (correcao) [Why does Code Jam have its own email system?] 0.272: ## Why does Code Jam have its own email system?  To automatically identify the users who should get an email based on Code Jam-specific properties (such as scores, booleans in user profiles, and regis

## q-246 (esperado: DAN-170)

- busca inicial: DAN-170, DAN-198, DAN-126, DAN-200, DAN-065, DAN-103, DAN-191, DAN-035, DAN-154, DAN-116
- justificativa: 
- aprofundar DAN-170: `incorrect orbital mechanics satellite positions rollback did not fix root cause correction` — É o único que trata de posições incorretas de satélites após atualização e rollback que não resolveu, exatamente como o incidente atual; difere por envolver GLONASS e cálculos de mecânica orbital.
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.581: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  From CODE Analysis protocol: Number of GLONASS observations    reduced by about 10% on April 2nd.  this is why the IGS post
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.577: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Bad Broadcast Messages (resulting in position errors up to about ±200km) were sent out     starting April 1, 2014, 21:00; Fi
  - DAN-170 (causa) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.358: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Understood:    The GNONASS April 1st event was not a joke.    The failure was caused by wrong Broadcast Ephemerides   … p
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.318: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol of April 1). Some receivers unaffected, some stopped tracking GLONASS after 9h p.m. (red line), some even stopped GPS trackin
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.307: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Real-time GNSS Service   -timeIGSOpen Data       •   Observations & derived products freely available       •   Streaming da

## q-247 (esperado: DAN-170)

- busca inicial: DAN-170, DAN-126, DAN-050, DAN-198, DAN-035, DAN-103, DAN-065, DAN-200, DAN-154, DAN-074
- justificativa: 
- aprofundar DAN-170: `bad update incorrect orbital mechanics rollback did not fix incorrect positions` — DAN-170 é o único que envolve receptores recebendo posições incorretas de satélites após uma atualização, com rollback que não resolveu o problema, exatamente como no incidente atual.
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.518: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  From CODE Analysis protocol: Number of GLONASS observations    reduced by about 10% on April 2nd.  this is why the IGS post
  - DAN-170 (llm) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.518: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Understood:    The GNONASS April 1st event was not a joke.    The failure was caused by wrong Broadcast Ephemerides   … p
  - DAN-170 (causa) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.337: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol of April 1). Some receivers unaffected, some stopped tracking GLONASS after 9h p.m. (red line), some even stopped GPS trackin
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.307: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Real-time GNSS Service   -timeIGSOpen Data       •   Observations & derived products freely available       •   Streaming da
  - DAN-170 (correcao) [GLONASS satellites tracked by IGS receivers (from CODE analysis protocol] 0.3: # GLONASS satellites tracked by IGS receivers (from CODE analysis protocol  Bad Broadcast Messages (resulting in position errors up to about ±200km) were sent out     starting April 1, 2014, 21:00; Fi

## q-248 (esperado: DAN-180)

- busca inicial: DAN-180, DAN-164, DAN-191, DAN-129, DAN-209, DAN-222, DAN-048, DAN-181, DAN-107, DAN-102
- justificativa: 
- aprofundar DAN-180: `ingest system repeatedly down cache delays root cause fix` — O sistema de ingestão caiu repetidamente por mais de oito horas, igual ao incidente atual de ingestão instável.
- aprofundar DAN-222: `Cassandra cluster crash ingestion message bus producers blocking fix` — O cluster de ingestão caiu e bloqueou produtores, parecido com a instabilidade do sistema de ingestão atual.
- aprofundar DAN-181: `total outage no data processed root cause fix` — Indisponibilidade total impediu o processamento de dados, mas não cita especificamente o sistema de ingestão.
  - DAN-180 (llm) [The events] 0.655: ## The events  We then forced a scale-down of Shepherds to disrupt the pattern, but the autoscaler decided we had too few Shepherds—crashlooping demands a lot of CPU—and instead added more of them. We
  - DAN-180 (llm) [The events] 0.644: ## The events  We decided to do more aggressive sampling in an attempt to stabilize the Refinery cluster by keeping less data. This seemed to work, but sampling aggressively was impacting our ability 
  - DAN-180 (causa) [On causal confusion] 0.541: ### On causal confusion  At one point, our understanding of the situation looked like the following diagram, where orange denotes places where we observed unusual behavior:  Ingestion volume was highe
  - DAN-180 (correcao) [Analysis] 0.509: ## Analysis  This incident revealed areas where we had built mental models of components that proved inaccurate during incidents, and could even clash with each other. This was an opportunity to contr
  - DAN-180 (correcao) [On the solution found] 0.457: ### On the solution found  We still don’t know what triggered all of this, we just know that it was fixed by the cache pre-fill. We are confident the fix worked and is effective because it’s been thro
  - DAN-222 (llm) [sem seção] 0.641: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (llm) [sem seção] 0.638: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (causa) [sem seção] 0.457: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (correcao) [sem seção] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl
  - DAN-181 (llm) [**The incident**] 0.594: ## **The incident**  The moment we understood this, we wrote a command to restart our query engine’s cluster without interfering with other critical features (querying and alerting). But right before 
  - DAN-181 (llm) [**Corrective actions**] 0.589: ### **Corrective actions**  For the duration of the outage, no new data could be ingested. If our users or customers did not buffer this data to disk somewhere to replay it later, it is gone for good.
  - DAN-181 (causa) [**How a database dies**] 0.525: ### **How a database dies**  The core of the database failure was a deadlock in MySQL’s internals. There’s no clear path on how we specifically got there, but since this is a concurrency issue, we thi
  - DAN-181 (correcao) [**Contributing factors**] 0.535: ### **Contributing factors**  Preventing a bug by switching to the old infrastructure set up the stage. We suspended deployments during the investigation, which prevented restarts accidentally making 
  - DAN-181 (correcao) [**Conclusion**] 0.499: ## **Conclusion**  While we wish such incidents wouldn’t happen, we know that we’ll have to manage them—no matter how hard we plan for them. One of the most intriguing themes that came up from many of

## q-249 (esperado: DAN-180)

- busca inicial: DAN-180, DAN-209, DAN-181, DAN-222, DAN-164, DAN-048, DAN-208, DAN-191, DAN-067, DAN-217
- justificativa: 
- aprofundar DAN-180: `ingest system repeated outage cache delay root cause fix` — O resumo cita ingest system down repeatedly por mais de oito horas, igual ao incidente atual, mas o componente citado é Shepherd Cache.
- aprofundar DAN-222: `Cassandra cluster crash ingest message bus queue fix` — Envolve ingestão de dados em cluster que falhou e afetou produtores, embora o foco seja Cassandra e não apenas o sistema de ingest.
- aprofundar DAN-181: `total outage data processing root cause remediation` — Trata de pane total com impossibilidade de processar dados, mas não menciona especificamente sistema de ingest nem instabilidade prolongada.
  - DAN-180 (llm) [The events] 0.663: ## The events  We then forced a scale-down of Shepherds to disrupt the pattern, but the autoscaler decided we had too few Shepherds—crashlooping demands a lot of CPU—and instead added more of them. We
  - DAN-180 (llm) [The events] 0.639: ## The events  This outage took out a serious portion of our ingest data for over eight hours and a half, not all consecutive, and involved about 10 engineers. We believe most customers sending data a
  - DAN-180 (causa) [On causal confusion] 0.541: ### On causal confusion  At one point, our understanding of the situation looked like the following diagram, where orange denotes places where we observed unusual behavior:  Ingestion volume was highe
  - DAN-180 (correcao) [Analysis] 0.509: ## Analysis  This incident revealed areas where we had built mental models of components that proved inaccurate during incidents, and could even clash with each other. This was an opportunity to contr
  - DAN-180 (correcao) [On the solution found] 0.457: ### On the solution found  We still don’t know what triggered all of this, we just know that it was fixed by the cache pre-fill. We are confident the fix worked and is effective because it’s been thro
  - DAN-222 (llm) [sem seção] 0.685: Due to the widespread failure in the Cassandra ring, we did not attempt to restore the cluster incrementally. We instead attempted a complete restart of the cluster, hoping that all the nodes would bo
  - DAN-222 (llm) [sem seção] 0.668: To understand the outage, consider the highly abstracted view of the Stackdriver architecture below. Data is posted to the gateway web service. The gateway has a set of queues (shown in red) that buff
  - DAN-222 (causa) [sem seção] 0.453: We do not yet fully understand why the Cassandra cluster failed, but we do know how to isolate and mitigate against similar problems in the future. We are working with the Cassandra developer communit
  - DAN-222 (correcao) [sem seção] 0.397: We are planning changes to the Stackdriver infrastructure to mitigate similar problems in the future. Most critically, we are planning to add a greater degree of separation for the pipelines used for 
  - DAN-222 (correcao) [sem seção] 0.38: At about 11:30 AM attempts to restore the existing Cassandra cluster were abandoned. We began our disaster recovery strategy of building a new Cassandra cluster. By 1:30 PM, a new 36-node Cassandra cl
  - DAN-181 (llm) [**Corrective actions**] 0.612: ### **Corrective actions**  For the duration of the outage, no new data could be ingested. If our users or customers did not buffer this data to disk somewhere to replay it later, it is gone for good.
  - DAN-181 (llm) [**The incident**] 0.59: ## **The incident**  The moment we understood this, we wrote a command to restart our query engine’s cluster without interfering with other critical features (querying and alerting). But right before 
  - DAN-181 (causa) [**How a database dies**] 0.525: ### **How a database dies**  The core of the database failure was a deadlock in MySQL’s internals. There’s no clear path on how we specifically got there, but since this is a concurrency issue, we thi
  - DAN-181 (correcao) [**Contributing factors**] 0.535: ### **Contributing factors**  Preventing a bug by switching to the old infrastructure set up the stage. We suspended deployments during the investigation, which prevented restarts accidentally making 
  - DAN-181 (correcao) [**Conclusion**] 0.499: ## **Conclusion**  While we wish such incidents wouldn’t happen, we know that we’ll have to manage them—no matter how hard we plan for them. One of the most intriguing themes that came up from many of

## q-250 (esperado: DAN-183)

- busca inicial: DAN-183, DAN-195, DAN-134, DAN-096, DAN-148, DAN-101, DAN-133, DAN-080, DAN-094, DAN-129
- justificativa: 
- aprofundar DAN-183: `GKE Dataplane V2 anetd CPU packet drop memcached Postgres timeout root cause fix` — Corresponde exatamente ao cenário atual: migração para nuvem (Google Cloud/GKE), picos de timeout Postgres, erros memcached i/o timeout, ajuste de pool insuficiente, e causa raiz na camada de rede do nó (Dataplane V2/anetD) saturando CPU e dropping pacotes.
  - DAN-183 (llm) [OK, so what’s actually going on?] 0.684: ## OK, so what’s actually going on?  This revelation suggests that this isn't a process-local issue. What we mean by this is the fact that we were having network issues between our Kubernetes node and
  - DAN-183 (llm) [Meanwhile, a few desks away] 0.667: ## Meanwhile, a few desks away  While all this had been going on, another unrelated issue had cropped up. Thanks to an accidental database join, we’d been making thousands of duplicate network calls t
  - DAN-183 (causa) [Meanwhile, a few desks away] 0.461: ## Meanwhile, a few desks away  This was only happening for a tiny handful of requests among hundreds of thousands, with seemingly no other consistent pattern when it came to which users, organization
  - DAN-183 (correcao) [Clouds, caches and connection conundrums] 0.391: ## Clouds, caches and connection conundrums  Ben Wheatley  September 26, 2023  13 min read  We recently moved our infrastructure fully into Google Cloud. Most things went very smoothly, but there was 
  - DAN-183 (correcao) [OK, so what’s actually going on?] 0.364: ## OK, so what’s actually going on?  If you think about it, it all starts to line up pretty much perfectly with what we’d seen and done up until this point:  - We mostly fixed the DB timeouts by fixin

## q-251 (esperado: DAN-183)

- busca inicial: DAN-183, DAN-101, DAN-148, DAN-096, DAN-195, DAN-134, DAN-133, DAN-129, DAN-080, DAN-156
- justificativa: 
- aprofundar DAN-183: `cloud migration Postgres memcached timeouts connection pool root cause fix` — Mesmo cenário: migração para nuvem, picos de Postgres connection timeouts e memcached i/o timeout, tuning do pool ajudou só parcialmente; difere no provedor (GKE) e no agente anetd.
- aprofundar DAN-101: `Go database/sql connection pool exhaustion unnecessary transaction fix root cause` — Bate em timeouts de conexão e tuning insuficiente do pool, mas não bate em migração para nuvem nem erros de memcached.
  - DAN-183 (llm) [/inc spike in connection timeouts] 0.695: ## /inc spike in connection timeouts  The trigger for this incident was a larger-than-normal number of Postgres connection timeouts. This wasn’t something we’d seen with our previous infrastructure, a
  - DAN-183 (llm) [Memcache joins the party] 0.691: ## Memcache joins the party  Postgres wasn’t the only part of our infrastructure having a tough time at this point. In our product, we use a memcached instance to hold transient data and speed up some
  - DAN-183 (causa) [Meanwhile, a few desks away] 0.461: ## Meanwhile, a few desks away  This was only happening for a tiny handful of requests among hundreds of thousands, with seemingly no other consistent pattern when it came to which users, organization
  - DAN-183 (correcao) [Clouds, caches and connection conundrums] 0.391: ## Clouds, caches and connection conundrums  Ben Wheatley  September 26, 2023  13 min read  We recently moved our infrastructure fully into Google Cloud. Most things went very smoothly, but there was 
  - DAN-183 (correcao) [OK, so what’s actually going on?] 0.364: ## OK, so what’s actually going on?  If you think about it, it all starts to line up pretty much perfectly with what we’d seen and done up until this point:  - We mostly fixed the DB timeouts by fixin
  - DAN-101 (llm) [sem seção] 0.687: When our app communicates with our database, it uses a client-side connection pool that is implemented in the`database/sql` Go package. The package uses these pools to limit the number of processes in
  - DAN-101 (llm) [sem seção] 0.664: ``` func trackUsage(ctx context.Context) (end func()) { 	inTransaction, _ := ctx.Value(InTransactionContextKey).(bool) 	startTime := time.Now() 	return func() { 		duration := time.Since(startTime) 		l
  - DAN-101 (causa) [sem seção] 0.433: Earlier this year, we experienced intermittent timeouts in our application while interacting with our database over a period of two weeks.  Despite our best efforts, we couldn’t immediately identify a
  - DAN-101 (correcao) [sem seção] 0.424: At this point, we felt we’d sunk a decent amount of time into investigating this outage, and we’d shipped a good amount of low-hanging fruit, we called it a day and closed the incident.  Within a coup
  - DAN-101 (correcao) [See related articles] 0.421: ## See related articles  ### We gave cloud agents a phone to QA  ### How savepoints quietly throttled our Postgres queue  ### Building Investigations: what it takes to build an AI SRE  ## So good, you

## q-252 (esperado: DAN-186)

- busca inicial: DAN-186, DAN-164, DAN-120, DAN-043, DAN-048, DAN-011, DAN-156, DAN-094, DAN-195, DAN-226
- justificativa: 
- aprofundar DAN-186: `hosted database limit reached migration new database recovery fix` — Bate porque é um banco de dados hospedado que atingiu um limite e causou outage; não bate porque o foco está na migração para novo banco.
- aprofundar DAN-120: `integer limit database read-only outage fix migration` — Bate porque o limite do banco deixou o serviço somente leitura (sem escrita); não bate porque o limite é específico de inteiro.
- aprofundar DAN-195: `postgres transaction ID wraparound outage fix vacuum` — Bate porque é um limite interno do banco (transaction ID) causando outage; não bate porque é wraparound do Postgres, não limite de hospedagem.
  - DAN-186 (llm) [**Full service restoration**] 0.681: # **Full service restoration**  Once we had the new ext4-backed database with full data and indexes synced up to the temporary production database, the final step was to promote the new database to ma
  - DAN-186 (llm) [**Prevention**] 0.666: # **Prevention**  Without knowledge of the pre-April 2014 file size limit, it was difficult to foresee and prevent this issue. As far as we can tell, there’s no information in the RDS console in the f
  - DAN-186 (causa) [**Accountability**] 0.46: # **Accountability**  I take full responsibility for the incident and the downtime. While the information about the 2TB limitation wasn’t directly available to me, it’s my responsibility to understand
  - DAN-186 (correcao) [**Action items**] 0.477: # **Action items**  As part of our retrospective process at Pinterest, we’re defining a better workflow for system-wide Instapaper outages that escalate issues immediately to Pinterest’s Site Reliabil
  - DAN-186 (correcao) [**Reflections**] 0.427: # **Reflections**  This is any web application developer’s worst nightmare. A filesystem-based limitation we weren’t aware of and had no visibility into rendered not only our production database usele
  - DAN-120 (llm) [sem seção] 0.706: Last Thursday, November 9th, Basecamp 3 was in read-only mode for almost five hours starting 7:21am CST and ending 12:11pm CST. That meant users could access existing messages, todo lists, and files, 
  - DAN-120 (llm) [sem seção] 0.572: We pride ourselves at Basecamp on being “boring software” because it just works and it’s always available. Since Basecamp 3 was launched, and up until this outage, we’ve had an uptime record of 99.998
  - DAN-120 (causa) [sem seção] 0.427: Note: If you weren’t using Basecamp at the time, you can see how we kept everyone in the loop using our status.basecamp.com updates and a play-by-play record on our blog. We can’t promise to be perfec
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.787: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.653: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg

## q-253 (esperado: DAN-186)

- busca inicial: DAN-186, DAN-164, DAN-120, DAN-094, DAN-043, DAN-048, DAN-156, DAN-147, DAN-011, DAN-096
- justificativa: 
- aprofundar DAN-186: `hosted database limit reached migration new database fix` — É o mais parecido: banco de dados hospedado (hosted database) atingiu limites e exigiu migração para outro banco; não confirma se o serviço ficou apenas read-only.
- aprofundar DAN-120: `integer limit database read-only outage recovery fix` — Bate porque o banco atingiu um limite (integer limit) e o serviço ficou read-only, impedindo escritas; não confirma se é um banco hospedado (hosted).
- aprofundar DAN-048: `RDS Multi-AZ failover MySQL misconfiguration data loss fix` — É um banco gerenciado na nuvem (RDS) com falha grave, mas o gatilho é hardware e configuração incorreta, não o atingimento de um limite de capacidade.
  - DAN-186 (llm) [**Prevention**] 0.676: # **Prevention**  Without knowledge of the pre-April 2014 file size limit, it was difficult to foresee and prevent this issue. As far as we can tell, there’s no information in the RDS console in the f
  - DAN-186 (llm) [**Root cause**] 0.618: # **Root cause**  In short, the data failure was caused by a 2TB file size limit for RDS instances created before April 2014. On Wednesday, February 9 at 12:30PM PT our “bookmarks” table that stores a
  - DAN-186 (causa) [**Accountability**] 0.46: # **Accountability**  I take full responsibility for the incident and the downtime. While the information about the 2TB limitation wasn’t directly available to me, it’s my responsibility to understand
  - DAN-186 (correcao) [**Action items**] 0.477: # **Action items**  As part of our retrospective process at Pinterest, we’re defining a better workflow for system-wide Instapaper outages that escalate issues immediately to Pinterest’s Site Reliabil
  - DAN-186 (correcao) [**Full service restoration**] 0.454: # **Full service restoration**  Once we had the new ext4-backed database with full data and indexes synced up to the temporary production database, the final step was to promote the new database to ma
  - DAN-120 (llm) [sem seção] 0.687: Last Thursday, November 9th, Basecamp 3 was in read-only mode for almost five hours starting 7:21am CST and ending 12:11pm CST. That meant users could access existing messages, todo lists, and files, 
  - DAN-120 (llm) [sem seção] 0.585: We pride ourselves at Basecamp on being “boring software” because it just works and it’s always available. Since Basecamp 3 was launched, and up until this outage, we’ve had an uptime record of 99.998
  - DAN-120 (causa) [sem seção] 0.427: Note: If you weren’t using Basecamp at the time, you can see how we kept everyone in the loop using our status.basecamp.com updates and a play-by-play record on our blog. We can’t promise to be perfec
  - DAN-048 (llm) [Final thoughts] 0.826: ## Final thoughts  In retrospect, we’re glad that we dug deeper into the incident and how we were able to reach the root of the problem. The incident showed us that we were always vulnerable to data l
  - DAN-048 (llm) [Incorrect configuration variable] 0.816: ## Incorrect configuration variable  We found a MySQL configuration parameter innodb\_flush\_log\_at\_trx\_commit, which is very critical for the seamless process of a failover.  InnoDB data changes a
  - DAN-048 (causa) [How Multi-AZ replication works] 0.492: ## How Multi-AZ replication works  Looking at the process of failover, it seems pretty foolproof; and the replicas should’ve never gone through any duplicate errors and we should’ve never had any data
  - DAN-048 (correcao) [Incorrect configuration variable] 0.339: ## Incorrect configuration variable  Apparently, there is another variable called sync\_binlog which when set to 1, flushes the data to binary logs immediately. As we had set it to 1 (which is correct
  - DAN-048 (correcao) [Data loss] 0.426: ## Data loss  Next day, on our follow-up calls with RDS tech support, we were told that it was not a usual occurrence that the replication crashes in scenarios of multi-AZ master failover, and there m

## q-254 (esperado: DAN-188)

- busca inicial: DAN-188, DAN-080, DAN-195, DAN-102, DAN-164, DAN-112, DAN-109, DAN-147, DAN-048, DAN-101
- justificativa: 
- aprofundar DAN-188: `Postgres metadata lock transaction wraparound global lock fix` — Escolhi porque envolve exatamente servidores PostgreSQL de metadados com operações bloqueadas por lock, incluindo wraparound e lock global, igual ao incidente atual; não menciona serviço de armazenamento diretamente, mas o mecanismo de bloqueio é o mesmo.
- aprofundar DAN-102: `PGAudit Postgres lock critical timeout restart primary removal fix` — Escolhi porque descreve extensão Postgres segurando locks críticos e ignorando timeouts, bloqueando operações do banco, com correção por reinício e remoção, semelhante ao travamento atual; diferenciam-se pela causa ser uma extensão após upgrade, não wraparound.
- aprofundar DAN-195: `Postgres transaction ID wraparound outage root cause fix` — Escolhi porque reporta wraparound de Transaction IDs no Postgres causando outage parcial, que pode explicar a origem do lock nos metadados; não detalha consultas esperando lock por horas, focando mais no XID wraparound.
  - DAN-188 (llm) [Summary of Root Cause] 0.653: ### Summary of Root Cause  In summary:  - All Manta operations touch our sharded, PostgreSQL-backed metadata tier. - During the event, one of the shard databases had all queries on our primary table b
  - DAN-188 (llm) [Subsequent analysis] 0.634: ### Subsequent analysis  #### More background  To fully understand what happened, a little more background on PostgreSQL is required.  PostgreSQL's implementation of Multi-Version Concurrency Control 
  - DAN-188 (causa) [Root cause analysis] 0.545: ## Root cause analysis  For transparency, we've included a lot of detail here about how the incident proceeded. If you're interested in more of a summary, skip to the Summary of Root Cause section bel
  - DAN-188 (correcao) [Closing] 0.517: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working hard to prevent an issue like this from happ
  - DAN-188 (correcao) [The problem] 0.482: ### The problem  We observed the autovacuum scan the full table and all of its indexes, and then do the same thing again. After several hours, it successfully completed and updated the "last\_autovacu
  - DAN-102 (llm) [sem seção] 0.644: On Wednesday, April 9, 2025, between 14:16 and 14:27 UTC, our systems experienced intermittent availability issues. The incident culminated in a 2-minute database outage from 14:25 to 14:27 UTC across
  - DAN-102 (llm) [sem seção] 0.586: Key elements of our infrastructure are designed to handle this scenario, and so, importantly, no on-call alerts or escalations were dropped during this period.  After restoring service, we temporarily
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.832: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.632: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg

## q-255 (esperado: DAN-188)

- busca inicial: DAN-188, DAN-080, DAN-195, DAN-109, DAN-112, DAN-164, DAN-102, DAN-181, DAN-101, DAN-226
- justificativa: 
- aprofundar DAN-188: `PostgreSQL metadata server lock transaction wraparound global lock fix` — Serviço de storage (Manta) com operações bloqueadas por lock no banco de metadados PostgreSQL, igual ao incidente atual; difere por envolver wraparound de transação e query que tentava lock global.
- aprofundar DAN-102: `PGAudit extension hung holding critical locks Postgres migration fix restart` — PostgreSQL com extensão travada segurando locks críticos e bloqueando operações do banco, parecido com queries esperando lock; difere por ser causado por interação PGAudit/migration após upgrade.
- aprofundar DAN-195: `Postgres transaction ID wraparound outage root cause fix vacuum` — Wraparound de transaction ID no PostgreSQL causou interrupção, relacionado à causa raiz do DAN-188; difere por não descrever diretamente lock no banco de metadados de storage.
  - DAN-188 (llm) [Summary of Root Cause] 0.647: ### Summary of Root Cause  In summary:  - All Manta operations touch our sharded, PostgreSQL-backed metadata tier. - During the event, one of the shard databases had all queries on our primary table b
  - DAN-188 (llm) [Subsequent analysis] 0.641: ### Subsequent analysis  #### More background  To fully understand what happened, a little more background on PostgreSQL is required.  PostgreSQL's implementation of Multi-Version Concurrency Control 
  - DAN-188 (causa) [Root cause analysis] 0.545: ## Root cause analysis  For transparency, we've included a lot of detail here about how the incident proceeded. If you're interested in more of a summary, skip to the Summary of Root Cause section bel
  - DAN-188 (correcao) [Closing] 0.517: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working hard to prevent an issue like this from happ
  - DAN-188 (correcao) [The problem] 0.482: ### The problem  We observed the autovacuum scan the full table and all of its indexes, and then do the same thing again. After several hours, it successfully completed and updated the "last\_autovacu
  - DAN-102 (llm) [sem seção] 0.691: On Wednesday, April 9, 2025, between 14:16 and 14:27 UTC, our systems experienced intermittent availability issues. The incident culminated in a 2-minute database outage from 14:25 to 14:27 UTC across
  - DAN-102 (llm) [sem seção] 0.668: Key elements of our infrastructure are designed to handle this scenario, and so, importantly, no on-call alerts or escalations were dropped during this period.  After restoring service, we temporarily
  - DAN-195 (llm) [Background: Postgres Transaction IDs] 0.795: #### Background: Postgres Transaction IDs  In order to understand the underlying issue, we need to explain briefly how transaction concurrency works inside Postgres. At a high level, every write (UPDA
  - DAN-195 (llm) [Wraparound Protection Triggered] 0.667: #### Wraparound Protection Triggered  Mandrill has a set of distinct databases which act as a unified K/V store sharded by key. The hashing algorithm used to balance load to these favored shard4, caus
  - DAN-195 (causa) [What We Learned] 0.466: #### What We Learned  At Mailchimp, we take a blameless approach to post-incident reviews. Our primary objective is to learn as much as we can, not to point fingers at individuals or teams. Incidents 
  - DAN-195 (correcao) [Incident Response] 0.51: #### Incident Response  We’ve been working to update and strengthen our Incident Response protocol over the past year. This was our largest incident in that period, providing a good opportunity for us
  - DAN-195 (correcao) [What We Learned] 0.506: #### What We Learned  - The incident command muscles that we've been building paid off—close coordination of the response was critical to our recovery. - We ultimately landed on the truncation strateg

## q-256 (esperado: DAN-189)

- busca inicial: DAN-189, DAN-103, DAN-066, DAN-146, DAN-067, DAN-064, DAN-070, DAN-106, DAN-210, DAN-191
- justificativa: 
- aprofundar DAN-189: `operator reboot all servers maintenance tool root cause fix` — O operador usou uma ferramenta para reiniciar servidores em manutenção e acabou reiniciando todo o datacenter, exatamente como no incidente atual.
  - DAN-189 (llm) [What Happened?] 0.66: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [What Happened?] 0.567: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (causa) [Next Steps] 0.434: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-257 (esperado: DAN-189)

- busca inicial: DAN-189, DAN-146, DAN-103, DAN-066, DAN-064, DAN-067, DAN-070, DAN-073, DAN-208, DAN-068
- justificativa: 
- aprofundar DAN-189: `reboot all servers lax input validation root cause fix remediation` — É o único incidente que descreve exatamente o mesmo cenário: um operador usou uma ferramenta para reiniciar poucos servidores em manutenção e, por falha de validação de entrada, reiniciou todos os servidores do datacenter de uma vez. Bate perfeitamente com o incidente atual.
  - DAN-189 (llm) [What Happened?] 0.605: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [What Happened?] 0.553: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (causa) [Next Steps] 0.434: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 

## q-258 (esperado: DAN-194)

- busca inicial: DAN-194, DAN-156, DAN-133, DAN-164, DAN-147, DAN-066, DAN-211, DAN-048, DAN-190, DAN-094
- justificativa: 
- aprofundar DAN-194: `MongoDB secondary overloaded troubleshooting change sent traffic to primary root cause fix` — Bate exatamente com o incidente atual: secundários MongoDB sobrecarregados e, durante o diagnóstico, uma mudança enviou todo o tráfego dos secundários para o primário, sobrecarregando-o também. Não há diferença relevante na descrição.
  - DAN-194 (llm) [Website Intermittent Timeouts] 0.654: ## Website Intermittent Timeouts  ## Postmortem  ## Summary  On January 12th at 14:09 UTC, our engineers began responding to alerts for our click / open tracking services and primary MongoDB clusters 
  - DAN-194 (llm) [Summary] 0.62: ## Summary  After review of our MongoDB configurations, we deployed limits on the number of connections our services could establish to our primary MongoDB server. We prepared these changes and began 
  - DAN-194 (causa) [Corrective Actions] 0.357: ## Corrective Actions  - Deployment of Redundant Tracking Infrastructure (Complete) - Our tracking services have previously operated out of a single region. As part of previously planned infrastructur
  - DAN-194 (correcao) [Resolved] 0.444: ## Resolved  This incident has been resolved.  Posted Jan 12, 2017 - 15:10 PST  ## Monitoring  Mailgun engineers have made a series of changes to our system, which have improved the performance and st
  - DAN-194 (correcao) [Identified] 0.327: ## Identified  We’re seeing improved performance and stability from our core API & SMTP services at this time. The engineering team is continuing to work to completely resolve the issue.  Posted Jan 1

## q-259 (esperado: DAN-194)

- busca inicial: DAN-194, DAN-156, DAN-133, DAN-164, DAN-147, DAN-048, DAN-066, DAN-130, DAN-096, DAN-094
- justificativa: 
- aprofundar DAN-194: `secondary overload primary traffic change root cause fix` — Corresponde exatamente: segundos do MongoDB sobrecarregados e, durante troubleshooting, uma mudança enviou todo o tráfego dos segundos para o primário, sobrecarregando-o também. É o único que menciona o erro de roteamento de tráfego causado pelo próprio troubleshooting.
  - DAN-194 (llm) [Website Intermittent Timeouts] 0.526: ## Website Intermittent Timeouts  ## Postmortem  ## Summary  On January 12th at 14:09 UTC, our engineers began responding to alerts for our click / open tracking services and primary MongoDB clusters 
  - DAN-194 (llm) [Corrective Actions] 0.46: ## Corrective Actions  - Deployment of Redundant Tracking Infrastructure (Complete) - Our tracking services have previously operated out of a single region. As part of previously planned infrastructur
  - DAN-194 (causa) [Summary] 0.373: ## Summary  After review of our MongoDB configurations, we deployed limits on the number of connections our services could establish to our primary MongoDB server. We prepared these changes and began 
  - DAN-194 (correcao) [Resolved] 0.444: ## Resolved  This incident has been resolved.  Posted Jan 12, 2017 - 15:10 PST  ## Monitoring  Mailgun engineers have made a series of changes to our system, which have improved the performance and st
  - DAN-194 (correcao) [Identified] 0.327: ## Identified  We’re seeing improved performance and stability from our core API & SMTP services at this time. The engineering team is continuing to work to completely resolve the issue.  Posted Jan 1

## q-260 (esperado: DAN-197)

- busca inicial: DAN-066, DAN-106, DAN-067, DAN-029, DAN-209, DAN-220, DAN-154, DAN-205, DAN-008, DAN-133
- justificativa: 
- aprofundar DAN-066: `Byzantine failure switch misbehavior API outage root cause remediation` — Falha súbita na API sem mudanças do nosso lado, causada por comportamento incorreto de infraestrutura (switch) — bate com falha repentina de provedor externo sem alterações nossas.
- aprofundar DAN-067: `Flexential data center power failure API thundering herd cause fix` — Menciona chamadas de API que estavam falhando e sobrecarga, mas a causa é falha de energia, não chamado de API a provedor de nuvem — semelhança parcial.
- aprofundar DAN-106: `human error networking upgrade EC2 RDS outage cause fix` — Interrupção de provedor de nuvem (Amazon) afetando clientes sem mudanças deles, mas envolve erro humano durante upgrade — causa é uma mudança do provedor, não exatamente sem mudanças.
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.626: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.617: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
  - DAN-067 (llm) [Attempting to Restore Power] 0.736: ### Attempting to Restore Power  While we haven't gotten official confirmation, we have been told by employees that three things hampered getting the generators back online. First, they needed to be p
  - DAN-067 (llm) [Flexential Data Center Power Failure] 0.718: ### Flexential Data Center Power Failure  It is also unusual that Flexential ran both the one remaining utility feed and the generators at the same time. It is not unusual for utilities to ask data ce
  - DAN-067 (causa) [Lessons and Remediation] 0.574: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (correcao) [Disaster Recovery] 0.446: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.699: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.681: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.41: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  The team faced two challenges which delayed getting capacity online. First, when a node fails, the EBS cluster do
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 

## q-261 (esperado: DAN-197)

- busca inicial: DAN-067, DAN-066, DAN-220, DAN-154, DAN-029, DAN-008, DAN-133, DAN-106, DAN-205, DAN-209
- justificativa: 
- aprofundar DAN-066: `Byzantine failure switch misbehavior API availability root cause fix` — Bate por ser falha de infraestrutura que derruba API sem mudança do cliente, mas não é exatamente uma chamada a provedor de nuvem externo.
- aprofundar DAN-106: `human error networking upgrade resource crunch EC2 RDS outage root cause fix` — Bate por ser interrupção de provedor de nuvem (Amazon) sem mudança do cliente, mas foca em EC2/RDS e não em chamadas de API externas.
- aprofundar DAN-067: `power failure thundering herd API calls rate limit recovery fix` — Bate por envolver chamadas de API falhando repentinamente, mas o gatilho é falha de energia em datacenter, não provedor de nuvem.
  - DAN-066 (llm) [2020-11-02 14:43 UTC: Partial Switch Failure] 0.612: ### 2020-11-02 14:43 UTC: Partial Switch Failure  At 14:43, a network switch started misbehaving. Alerts began firing about the switch being unreachable to pings. The device was in a partially operati
  - DAN-066 (llm) [2020-11-02 21:20 UTC Database Replica Rebuilt] 0.599: ### 2020-11-02 21:20 UTC Database Replica Rebuilt  The instant the first database replica rebuilt, it put itself back into service, and performance resumed to normal levels. We re-ramped all of the se
  - DAN-066 (causa) [Redundant Points of Failure] 0.522: ### Redundant Points of Failure  The cascade of failures in this incident was interesting because each system, on its face, had redundancy. Moreover, no system fully failed—each entered a degraded sta
  - DAN-066 (correcao) [Redundant Points of Failure] 0.36: ### Redundant Points of Failure  The first uses of BFT consensus were in safety-critical systems such as aircraft and spacecraft controls. These systems typically have hard real time latency constrain
  - DAN-066 (correcao) [2020-11-02 14:45 UTC: Database system promotes a new primary database] 0.353: ### 2020-11-02 14:45 UTC: Database system promotes a new primary database  Cloudflare’s control plane services use relational databases hosted across multiple clusters within a data center. Each clust
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.692: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  Two factors caused the situation in this EBS cluster to degrade further during the early part of the event. First
  - DAN-106 (llm) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.687: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  RDS multi-AZ deployments provide redundancy by synchronously replicating data between two database replicas in di
  - DAN-106 (causa) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.41: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  The team faced two challenges which delayed getting capacity online. First, when a node fails, the EBS cluster do
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.448: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  In addition to the technical insights and improvements that will result from this event, we also identified impro
  - DAN-106 (correcao) [Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region] 0.388: ### Summary of the Amazon EC2 and Amazon RDS Service Disruption in the US East Region  We will be making a number of changes to prevent a cluster from getting into a re-mirroring storm in the future. 
  - DAN-067 (llm) [Disaster Recovery] 0.719: ### Disaster Recovery  When services were turned up there, we experienced a thundering herd problem where the API calls that had been failing overwhelmed our services. We implemented rate limits to ge
  - DAN-067 (llm) [Lessons and Remediation] 0.607: ### Lessons and Remediation  As I said earlier, I am sorry and embarrassed for this incident and the pain that it caused our customers and our team. We have the right systems and procedures in place t
  - DAN-067 (causa) [Informed Speculation On What Happened Next] 0.51: ### Informed Speculation On What Happened Next  Ground faults with high voltage (12,470 volt) power lines are very bad. Electrical systems are designed to quickly shut down to prevent damage when one 
  - DAN-067 (correcao) [Lessons and Remediation] 0.428: ### Lessons and Remediation  We have a number of questions that we need answered from Flexential. But we also must expect that entire data centers may fail. Google has a process where when there’s a s
  - DAN-067 (correcao) [Disaster Recovery] 0.397: ### Disaster Recovery  At 12:48 UTC, Flexential was able to get the generators restarted. Power returned to portions of the facility. In order to not overwhelm the system, when power is restored to a 

## q-262 (esperado: DAN-200)

- busca inicial: DAN-103, DAN-198, DAN-066, DAN-191, DAN-073, DAN-189, DAN-146, DAN-210, DAN-043, DAN-200
- justificativa: 
- aprofundar DAN-200: `Mars Pathfinder priority inversion VxWorks reset root cause patch fix` — O computador de bordo reiniciava dias após iniciar operação, igual ao incidente atual, embora em uma sonda Mars e não em computador de bordo terrestre.
- aprofundar DAN-198: `Apollo 11 rendezvous radar CPU load computer restart cause fix` — Também envolve reinício espontâneo de computador de bordo, mas desencadeado por carga excessiva de CPU durante pouso lunar, não dias depois de entrar em operação.
  - DAN-200 (llm) [HOW WE FOUND IT] 0.695: ## HOW WE FOUND IT  The software that flies on Mars Pathfinder has several debug features within it that are used in the lab but are not used on the flight spacecraft (not used because some of them pr
  - DAN-200 (llm) [SETTING THE RECORD STRAIGHT] 0.62: ## SETTING THE RECORD STRAIGHT  First, I want to make sure that everyone understands how I feel in regard to Wind River. These folks did a fantastic job for us. They were enthusiastic and supported us
  - DAN-200 (causa) [THE FAILURE] 0.577: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.733: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.696: | | The availability of core sets and VAC areas limited the number of jobs that could be in the queue at any time to eight, of which up to five could require VAC areas. In normal steady-state operatio
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-263 (esperado: DAN-200)

- busca inicial: DAN-198, DAN-191, DAN-103, DAN-189, DAN-200, DAN-073, DAN-146, DAN-106, DAN-069, DAN-066
- justificativa: 
- aprofundar DAN-200: `VxWorks priority inversion system reset remote patch fix` — O incidente envolve resets do computador de bordo dias depois de começar a operar, exatamente como o atual, embora ocorra em uma sonda marciana.
- aprofundar DAN-198: `rendezvous radar excess CPU load computer restart fix` — Também descreve reinícios de computador de nave causados por sobrecarga, mas o gatilho é o radar durante o pouso lunar, não dias após o início da operação.
  - DAN-200 (llm) [THE FAILURE] 0.584: ## THE FAILURE  The failure was identified by the spacecraft as a failure of the bc_dist task to complete its execution before the bc_sched task started. The reaction to this by the spacecraft was to 
  - DAN-200 (llm) [HOW WAS THE PROBLEM CORRECTED] 0.577: ## HOW WAS THE PROBLEM CORRECTED  Once we understood the problem the fix appeared obvious : change the creation flags for the semaphore so as to enable priority inheritance. The Wind River folks, for 
  - DAN-200 (causa) [HUMAN NATURE, DEADLINE PRESSURES] 0.469: ## HUMAN NATURE, DEADLINE PRESSURES  We did see the problem before landing but could not get it to repeat when we tried to track it down. It was not forgotten nor was it deemed unimportant. Yes, we we
  - DAN-200 (correcao) [ANALYSIS AND LESSONS] 0.354: ## ANALYSIS AND LESSONS  Did we (the JPL team) make an error in assuming how the select/pipe mechanism would work ? Yes, probably. But there was no conscious decision to not have the priority inherita
  - DAN-200 (correcao) [HOW WAS THE PROBLEM CORRECTED] 0.348: ## HOW WAS THE PROBLEM CORRECTED  We did end up modifying the global variable to include the priority inheritance option. This corrected the problem. We asked Wind River to analyze the potential impac
  - DAN-198 (llm) [sem seção] 0.587: | The interesting effect of this train of events, during P63, was that the problem fixed itself. The software restart reconstructed only the most recent incarnation of the SERVICER job, and flushed th
  - DAN-198 (llm) [sem seção] 0.562: This phenomenon occurred whenever the RR mode was in SLEW or AUTO, regardless of whether the rendezvous radar itself was powered up. | | The CDU interface counters in the LGC were incremented or decre
  - DAN-198 (causa) [sem seção] 0.429: We leaned closer to the squawk box that connected us to mission control in Houston. | | We heard "Engine on"... several seconds passed... "Engine off". | | Soon we understood what had happened. A smal
  - DAN-198 (correcao) [sem seção] 0.41: A new noun (92) was defined that the crew could select to see the throttle level desired by guidance.  Logic that would have terminated automatic guidance if the throttle were (or appeared to be) swit
  - DAN-198 (correcao) [sem seção] 0.395: | It is evident that without the waypoint, going through this code a second time would cause X to be incremented twice. | | Following a restart, such computations could be reconstructed. For each job,

## q-264 (esperado: DAN-204)

- busca inicial: DAN-175, DAN-215, DAN-204, DAN-203, DAN-124, DAN-131, DAN-058, DAN-136, DAN-141, DAN-107
- justificativa: 
- aprofundar DAN-204: `Redis cache corruption out of sequence requests cross user data billing leak root cause fix` — Este incidente descreve exatamente o sintoma atual: usuários vendo dados de outros usuários, incluindo informações de cobrança, devido a corrupção de filas em cache Redis. É o mais semelhante da lista.
  - DAN-204 (llm) [Technical details] 0.652: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.623: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa

## q-265 (esperado: DAN-204)

- busca inicial: DAN-175, DAN-204, DAN-124, DAN-058, DAN-131, DAN-203, DAN-220, DAN-107, DAN-098, DAN-164
- justificativa: 
- aprofundar DAN-204: `Redis cache corrupted queue cross-user data leak billing root cause fix` — Bate diretamente: usuários veem dados de outros, incluindo billing info, por cache Redis corrompido. Não bate: causa é fila de requisições, não configuração de aplicação.
- aprofundar DAN-058: `backup identifier misconfiguration data leak free tier root cause fix` — Bate parcialmente: vazamento de dados entre clientes por identificador incorreto. Não bate: é backup de banco, não visualização cross-user em tempo real.
- aprofundar DAN-175: `private token leaked data access root cause fix` — Bate parcialmente: vazamento de dados por token exposto. Não bate: é token/API, não usuários comuns vendo dados de outros usuários.
  - DAN-204 (llm) [Technical details] 0.619: ## Technical details  - We use Redis to cache user information in our server so we don’t need to check our database for every request. - We use Redis Cluster to distribute this load over multiple Redi
  - DAN-204 (llm) [Actions we’ve taken] 0.609: ## Actions we’ve taken  As our investigation wraps up, supporting and informing our users is our top priority.  We have taken the following actions to improve our systems:  - Extensively tested our fi
  - DAN-204 (causa) [Technical details] 0.395: ## Technical details  The bug was discovered in the Redis client open-source library, redis-py. As soon as we identified the bug, we reached out to the Redis maintainers with a patch to resolve the is
  - DAN-204 (correcao) [Where we go from here] 0.337: ## Where we go from here  The Redis open-source maintainers have been fantastic collaborators, swiftly addressing the bug and rolling out a patch. Redis, along with other open-source software, plays a
  - DAN-204 (correcao) [sem seção] 0.298: We took ChatGPT offline earlier this week due to a bug in an open-source library which allowed some users to see titles from another active user’s chat history. It’s also possible that the first messa
  - DAN-058 (llm) [What happened?] 0.777: ## What happened?  0.07% of databases under management were incorrectly configured with an empty backup identifier, which caused a data leak. The conservative fix we applied to the leak, lead to the p
  - DAN-058 (llm) [How do we know which databases were affected?] 0.715: ## How do we know which databases were affected?  We were able to determine all databases pointing to an invalid and shared backup ID by querying metadata for databases with the faulty backup ID. We c
  - DAN-058 (causa) [What was the root cause?] 0.424: ## What was the root cause?  Databases on Turso's free tier may scale to zero after one hour of inactivity. They are scaled back to one automatically upon receiving a network request. Usually this is 
  - DAN-058 (correcao) [Lessons learned and Remediation] 0.536: ## Lessons learned and Remediation  While we know the root cause quite well by now, there are still a few things we must do to ensure this never happens again. Some of these things are internal proces
  - DAN-058 (correcao) [Summary] 0.586: ## Summary  We are embarrassed for this incident and the pain that it has caused our customers and our team. We have and will be implementing improved processes to prevent this in the future, but we n
  - DAN-175 (llm) [Incident Summary] 0.568: ## Incident Summary  On April 13, 2022, GitHub notified our security team of a potential security issue they identified on April 12, 2022, and we immediately launched an investigation. Within three ho
  - DAN-175 (llm) [Incident Summary] 0.563: ## Incident Summary  Further investigation determined that the actor accessed and exfiltrated data from the database storing usernames and uniquely hashed and salted passwords for customer accounts. W
  - DAN-175 (causa) [April 2022 Incident Review] 0.327: ## April 2022 Incident Review  Posted By  Bob Wise  - Last Updated: June 14, 2022  We have concluded our investigation and want to provide our customers with an overview of the threat actor’s actions,
  - DAN-175 (correcao) [Incident Summary] 0.451: ## Incident Summary  The diligent response efforts, including enhanced detection, comprehensive mitigation, and detailed investigation effectively disrupted the threat actor’s established infrastructu
  - DAN-175 (correcao) [April 2022 Incident Review] 0.369: ## April 2022 Incident Review  We continue to engage with the GitHub security and engineering teams to raise the bar for security standards. As we believe RFC-8705 based mutual TLS and private key pro

## q-266 (esperado: DAN-205)

- busca inicial: DAN-205, DAN-209, DAN-184, DAN-191, DAN-180, DAN-066, DAN-106, DAN-065, DAN-234, DAN-129
- justificativa: 
- aprofundar DAN-205: `common peering point network instability quorum notification root cause fix` — Corresponde quase exatamente: duas de três implantações com alta latência e perda de conexão, notificações paradas por falha de quorum. Difere por ser de 2013 e envolver um ponto de peering compartilhado.
  - DAN-205 (llm) [The Outage] 0.678: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.587: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig

## q-267 (esperado: DAN-205)

- busca inicial: DAN-205, DAN-209, DAN-184, DAN-148, DAN-066, DAN-116, DAN-107, DAN-191, DAN-109, DAN-234
- justificativa: 
- aprofundar DAN-205: `shared peering point network instability quorum notifications root cause fix` —  bate exatamente com o atual: duas de três implantações com latência alta e perda de conexão simultâneas, falha de notificação e perda de quorum; não bate por ser de 2013 e envolver um ponto de peering compartilhado específico.
  - DAN-205 (llm) [The Outage] 0.699: ## The Outage  **Note:** All times referenced below are in Pacific Time.  - At 7:57am, according to AWS, connectivity issue begins due to a peering point degrading in Northern California - At 8:11am, 
  - DAN-205 (llm) [Outage Post-Mortem – April 13, 2013] 0.618: # Outage Post-Mortem – April 13, 2013  We spend enormous amount of our time on the reliability of PagerDuty and the infrastructure that hosts it. Most of this work is invisible, hidden behind the API 
  - DAN-205 (causa) [Background] 0.487: ## Background  PagerDuty’s infrastructure is hosted in three different datacenters (two in AWS and another in Linode). For the past year, we’ve been rearchitecting our software with the goal of it bei
  - DAN-205 (correcao) [Short term] 0.512: ### Short term  1. During our analysis, we found that we didn’t have adequate logging to debug issues within some of our systems. We have now added more logging and started to aggregate them into a si
  - DAN-205 (correcao) [Long term] 0.426: ### Long term  1. We also found that not all of our engineering staff are up to date with Cassandra and ZooKeeper. We’ll be investing time to train our staff on both of these technologies. 2. Investig

## q-268 (esperado: DAN-207)

- busca inicial: DAN-207, DAN-215, DAN-084, DAN-124, DAN-132, DAN-146, DAN-050, DAN-141, DAN-131, DAN-239
- justificativa: 
- aprofundar DAN-207: `multi-sig wallet security bug root cause fix patch` — Carteira de criptomoeda drenada por bug de segurança em implantação, mas o incidente é um contrato multi-sig específico e não necessariamente código de terceiros.
- aprofundar DAN-215: `employee cryptocurrency theft poor security practices remediation` — Roubo direto de criptomoeda por falhas de segurança, mas envolve funcionário interno e não vulnerabilidade no código da carteira.
- aprofundar DAN-131: `session cookie theft malware production access remediation` — Acesso não autorizado a produção por credenciais roubadas que pode drenar fundos, mas não é falha no código da carteira.
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.744: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (llm) [sem seção] 0.723: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.592: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.527: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.353: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Digital Forensic Investigation Following the preliminary investigation, a digital-forensic investigation was launched to analyze both Infrastructure2 and Infrastr
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo
  - DAN-131 (llm) [What happened?] 0.576: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.528: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi

## q-269 (esperado: DAN-207)

- busca inicial: DAN-207, DAN-215, DAN-132, DAN-175, DAN-124, DAN-084, DAN-160, DAN-141, DAN-016, DAN-219
- justificativa: 
- aprofundar DAN-207: `Parity multi-sig wallet security bug root cause fix drained funds` — É sobre carteira de criptomoeda (multi-sig) com bug de segurança que levou fundos a serem desviados/roubados, exatamente como o incidente atual; difere porque envolve uma mudança de 4000 linhas rotulada como alteração de UI.
- aprofundar DAN-215: `ShapeShift employee cryptocurrency theft root cause security fix` — Também envolve criptomoeda roubada, mas por um funcionário interno em vez de atacantes externos drenando wallets através de código vulnerável, então é menos parecido.
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.81: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (llm) [sem seção] 0.787: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.724: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.687: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.353: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Digital Forensic Investigation Following the preliminary investigation, a digital-forensic investigation was launched to analyze both Infrastructure2 and Infrastr
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo

## q-270 (esperado: DAN-208)

- busca inicial: DAN-208, DAN-079, DAN-151, DAN-066, DAN-106, DAN-144, DAN-191, DAN-222, DAN-205, DAN-220
- justificativa: 
- aprofundar DAN-208: `zookeeper boot failure too much data maintenance window fix` — O resumo diz que Zookeeper não bootou durante janela de manutenção por excesso de dados, exatamente o sintoma do incidente atual; difere no detalhe do excesso de dados, que ainda não é confirmado no atual.
- aprofundar DAN-079: `zookeeper reprovisioning leader election fix` — É sobre ZooKeeper, mas o problema foi eleição de segundo líder durante reprovisionamento, não falha em subir; ainda assim é o único outro incidente com ZooKeeper na lista.
  - DAN-208 (llm) [Wrapping up] 0.722: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (llm) [Read the socket] 0.715: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\
  - DAN-079 (llm) [sem seção] 0.62: In October, we experienced one incident resulting in significant impact and degraded state of availability for issues, pull requests, webhooks, GitHub Actions, and GitHub Pages services.  While reprov

## q-271 (esperado: DAN-208)

- busca inicial: DAN-208, DAN-151, DAN-079, DAN-103, DAN-211, DAN-066, DAN-135, DAN-220, DAN-026, DAN-109
- justificativa: 
- aprofundar DAN-208: `Zookeeper cannot start boot too much data maintenance window root cause fix` — Es el único incidente que coincide exactamente: caída en ventana de mantenimiento programada con Zookeeper incapaz de arrancar/bootear; el resumen ya señala datos excesivos como causa del fallo de arranque.
  - DAN-208 (llm) [Wrapping up] 0.7: # Wrapping up  To sum up, there were several issues which led to such a long  downtime:  1\. We restarted the gateways without waiting for the orchestration  software to be fully started.  2. We had t
  - DAN-208 (llm) [Read the socket] 0.674: # Read the socket  This time, quickly looking at ZooKeeper logs, we found that one node was over the max node size of ZooKeeper. We increased ZooKeeper max buffer size, restarted, and everything came 
  - DAN-208 (causa) [Downtime] 0.502: # Downtime  The maintenance window was only there to upgrade the orchestration  software. Currently, an upgrade of the orchestration software requires  a downtime of the git servers and the UI. (We’re
  - DAN-208 (correcao) [Introduction] 0.361: # Introduction  Here is a reminder of the chronology:  - 19:00 UTC: a maintenance of the region started, only the git servers and the UI were affected. - 19:30 UTC: the sites went down. - 23:30 UTC: t
  - DAN-208 (correcao) [Read the socket] 0.343: # Read the socket  else:  os.read(self.\_read\_pipe, 1)  send\_request(self.\_queue.pop())  And in the client, you have this kind of code:  self.\_queue.append(object)write\_pipe = self.\_connection.\

## q-272 (esperado: DAN-215)

- busca inicial: DAN-215, DAN-207, DAN-084, DAN-050, DAN-131, DAN-015, DAN-029, DAN-203, DAN-175, DAN-124
- justificativa: 
- aprofundar DAN-215: `employee cryptocurrency theft repeated hacks root cause fix security practices` — Bate com roubo de criptomoeda ocorrido mais de vez em poucas semanas (3 hacks em 1 mês); não deixa claro se o alvo foi carteira própria ou exchange.
- aprofundar DAN-207: `multi-sig hack security bug root cause fix cryptocurrency stolen` — Bate com criptomoeda desviada/roubada por falha de segurança; não trata de repetição do incidente em curto espaço de tempo.
- aprofundar DAN-131: `malware laptop session cookie theft root cause fix` — Bate com roubo de acesso via dispositivo e sessão comprometidos; não envolve diretamente criptomoeda nem repetição de roubo de carteira.
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.551: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.503: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.353: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Digital Forensic Investigation Following the preliminary investigation, a digital-forensic investigation was launched to analyze both Infrastructure2 and Infrastr
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo
  - DAN-207 (llm) [sem seção] 0.727: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.71: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-131 (llm) [What happened?] 0.562: ## What happened?  *All dates and times are reported in UTC, unless otherwise noted.*  On December 29, 2022, we were alerted to suspicious GitHub OAuth activity by one of our customers. This notificat
  - DAN-131 (llm) [What happened?] 0.438: ## What happened?  Because the targeted employee had privileges to generate production access tokens as part of the employee’s regular duties, the unauthorized third party was able to access and exfil
  - DAN-131 (causa) [A note on employee responsibility vs. systems safeguards] 0.419: ## A note on employee responsibility vs. systems safeguards  We want to be clear. While one employee’s laptop was exploited through this sophisticated attack, a security incident is a systems failure.
  - DAN-131 (correcao) [sem seção] 0.507: On January 4, 2023, we alerted customers to a security incident. Today, we want to share with you what happened, what we’ve learned, and what our plans are to continuously improve our security posture
  - DAN-131 (correcao) [Closing thoughts] 0.494: ## Closing thoughts  We know there is no convenient time to respond to a security incident on a critical system, and we want to sincerely thank all of our customers who immediately took action followi

## q-273 (esperado: DAN-215)

- busca inicial: DAN-207, DAN-215, DAN-084, DAN-131, DAN-015, DAN-050, DAN-209, DAN-175, DAN-219, DAN-132
- justificativa: 
- aprofundar DAN-207: `multi-sig wallet security bug root cause fix patch` — envolve roubo de criptomoeda de carteira multi-sig, igual ao incidente atual, embora o atual mencione recorrência.
- aprofundar DAN-215: `employee cryptocurrency theft repeated hacks security practices fix` — envolve roubo recorrente de criptomoeda em curto período (3 hacks em 1 mês), assim como o atual (segunda vez em poucas semanas).
  - DAN-207 (llm) [WHAT WAS THE NATURE OF THE BUG?] 0.744: ## WHAT WAS THE NATURE OF THE BUG?  The bug was in a pair of extremely sensitive functions designed to allow the set-up of "multi-sig" wallets in the Parity Wallet software.  The functions should have
  - DAN-207 (llm) [sem seção] 0.723: On Wednesday 19th July, 2017 a bug found in the multi-signature wallet ("multi-sig") code used as part of Parity Wallet software was exploited by parties unknown. As of the time of writing, three wall
  - DAN-207 (causa) [HOW DID THE BUG ESCAPE NOTICE?] 0.36: ## HOW DID THE BUG ESCAPE NOTICE?  In general, we treat security and consensus code extremely seriously at Parity.  All code changes undergo at least one peer review which we manage through a largely 
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.375: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  While there is no fool-proof means of practically ensuring software contains no bugs, Parity Technologies is committed to minimising the ch
  - DAN-207 (correcao) [WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?] 0.32: ## WHAT WILL PARITY DO TO ENSURE THIS DOESN'T HAPPEN AGAIN?  Thirdly, there is wisdom in the idea that the best disinfectant is direct sunlight. Had there been a greater degree of community ownership 
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.575: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Corrective Action Although evidence of the specific attack vector could not be found due to both the destruction of evidence by Rovion and the lack of logging con
  - DAN-215 (llm) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.512: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Following the 2016-03-14 breach (which will be referred to as Breach1 of Infrastructure1), entirely new SSH keys and passwords were created by all team members in
  - DAN-215 (causa) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.355: ## SHAPESHIFT CYBERATTACK POSTMORTEM  PREPARED FOR: SHAPESHIFT AG  Ledger Labs Inc. Michael Perklin, CBP, CISSP, CISA, EnCE, ACE michael@ledgerlabs.io  ShapeShift Cyber-Attack Postmortem On 2016-04-09
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.406: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Production Environment Refresh ShapeShift’s production environment was completely rebuilt using brand new cloud computing accounts. Different operating systems we
  - DAN-215 (correcao) [SHAPESHIFT CYBERATTACK POSTMORTEM] 0.396: ## SHAPESHIFT CYBERATTACK POSTMORTEM  Furthermore, all production servers were configured to send log entries to an off-site logging server to ensure that evidentiary data could not be destroyed follo

## q-274 (esperado: DAN-226)

- busca inicial: DAN-226, DAN-048, DAN-190, DAN-094, DAN-116, DAN-195, DAN-181, DAN-120, DAN-058, DAN-126
- justificativa: 
- aprofundar DAN-226: `SQL Server bugcheck root cause fix read only mode` — O resumo já menciona exatamente o mesmo padrão: SQL Server primário com bugcheck e sites entrando em modo somente leitura; o ambiente (Stack Exchange) pode ser diferente, mas a falha e o componente são idênticos.
  - DAN-226 (llm) [sem seção] 0.586: On January 24, 2017 starting at 17:53 UTC, we experienced system degradation (read only) followed by a site outage. The Stack Exchange network went into read-only mode for approximately 5 minutes befo

## q-275 (esperado: DAN-226)

- busca inicial: DAN-226, DAN-048, DAN-181, DAN-094, DAN-173, DAN-120, DAN-116, DAN-056, DAN-195, DAN-080
- justificativa: 
- aprofundar DAN-226: `SQL Server bugcheck root cause read only mode fix` — Bate exatamente: SQL Server primário com bugcheck e sites em modo read-only, mesma falha do incidente atual.
- aprofundar DAN-120: `database integer limit read only outage root cause fix` — Também envolve modo read-only causado por problema no banco, mas a causa é limite de inteiro, não bugcheck do SQL Server.
- aprofundar DAN-116: `double free database update crash root cause fix` — Envolve crash simultâneo de servidores por bug no banco, mas é double free em impression bus, não SQL Server bugcheck.
  - DAN-226 (llm) [sem seção] 0.584: On January 24, 2017 starting at 17:53 UTC, we experienced system degradation (read only) followed by a site outage. The Stack Exchange network went into read-only mode for approximately 5 minutes befo
  - DAN-120 (llm) [sem seção] 0.705: Last Thursday, November 9th, Basecamp 3 was in read-only mode for almost five hours starting 7:21am CST and ending 12:11pm CST. That meant users could access existing messages, todo lists, and files, 
  - DAN-120 (llm) [sem seção] 0.554: We pride ourselves at Basecamp on being “boring software” because it just works and it’s always available. Since Basecamp 3 was launched, and up until this outage, we’ve had an uptime record of 99.998
  - DAN-120 (causa) [sem seção] 0.427: Note: If you weren’t using Basecamp at the time, you can see how we kept everyone in the loop using our status.basecamp.com updates and a play-by-play record on our blog. We can’t promise to be perfec
  - DAN-116 (llm) [sem seção] 0.739: The problem is essentially a double free. In order to help keep latency as low as possible in our systems, we use what we call “time based memory reclamation” in parts of the system to avoid other mor
  - DAN-116 (llm) [sem seção] 0.618: By 18:47 UTC (2:47PM America/New\_York), the second team had identified the root cause of the crash in the impbus and created and tested a fix. The root cause was an old bug in the impbus, its effect 
  - DAN-116 (causa) [sem seção] 0.484: At 19:11 UTC (3:11PM America/New\_York), we discovered that Mr. Murphy is alive and well. We have never had to do a simultaneous deployment to all 6 data centers. While we originally constructed our d
  - DAN-116 (correcao) [sem seção] 0.481: In terms of our operational processes and deployment systems, we are reviewing our emergency procedures to ensure that we are able to stabilize and restore service in the shortest amount of time. Spec
  - DAN-116 (correcao) [sem seção] 0.452: - we will be changing our current validation systems to allow changes to pass only after the deferred deletion time window passes. In yesterday’s event, the validation systems did expose the problem b

## q-276 (esperado: DAN-235)

- busca inicial: DAN-235, DAN-231, DAN-221, DAN-184, DAN-022, DAN-165, DAN-154, DAN-059, DAN-195, DAN-069
- justificativa: 
- aprofundar DAN-235: `SMS filtering AT&T root cause corrective action` — O incidente descreve exatamente o mesmo sintoma (filtragem de SMS) direcionado a uma grande operadora dos EUA (AT&T), correspondendo ao incidente atual em sintoma e alvo, embora a plataforma seja a Twilio.
  - DAN-235 (llm) [High Filtering On SMS Towards AT&T Network In United States] 0.713: ## High Filtering On SMS Towards AT&T Network In United States  ## Resolved  We are no longer experiencing high filtering on SMS towards AT&T network in the United States for all senders. This inciden
  - DAN-235 (llm) [Investigating] 0.709: ## Investigating  We are experiencing high filtering on SMS towards AT&T network in Unites states. Our engineers are working with our carrier partner to resolve the issue. We expect to provide another
  - DAN-235 (causa) [Update] 0.24: ## Update  We are experiencing high filtering on SMS towards AT&T network in United States. Our engineers are continuing to work with our carrier partner to resolve the issue. We expect to provide ano
  - DAN-235 (correcao) [Monitoring] 0.273: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States. We will continue to monitor to ensure full service recovery. We expect to provide another
  - DAN-235 (correcao) [Monitoring] 0.254: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States for all senders. We will continue monitoring the service to ensure a full recovery. We wil

## q-277 (esperado: DAN-235)

- busca inicial: DAN-235, DAN-231, DAN-221, DAN-184, DAN-022, DAN-165, DAN-065, DAN-195, DAN-005, DAN-006
- justificativa: 
- aprofundar DAN-235: `SMS filtering AT&T root cause fix remediation` — O incidente atual é sobre SMS sendo filtrados para uma grande operadora dos EUA; DAN-235 descreve exatamente alto filtramento de SMS para a rede AT&T nos Estados Unidos, mesmo sintoma e mesmo tipo de componente (operadora móvel dos EUA).
  - DAN-235 (llm) [High Filtering On SMS Towards AT&T Network In United States] 0.704: ## High Filtering On SMS Towards AT&T Network In United States  ## Resolved  We are no longer experiencing high filtering on SMS towards AT&T network in the United States for all senders. This inciden
  - DAN-235 (llm) [Investigating] 0.696: ## Investigating  We are experiencing high filtering on SMS towards AT&T network in Unites states. Our engineers are working with our carrier partner to resolve the issue. We expect to provide another
  - DAN-235 (causa) [Update] 0.24: ## Update  We are experiencing high filtering on SMS towards AT&T network in United States. Our engineers are continuing to work with our carrier partner to resolve the issue. We expect to provide ano
  - DAN-235 (correcao) [Monitoring] 0.273: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States. We will continue to monitor to ensure full service recovery. We expect to provide another
  - DAN-235 (correcao) [Monitoring] 0.254: ## Monitoring  We are observing recovery with high filtering on SMS towards AT&T network in the United States for all senders. We will continue monitoring the service to ensure a full recovery. We wil

## q-278 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-146, DAN-073, DAN-231, DAN-043, DAN-104, DAN-071, DAN-173, DAN-220, DAN-048
- justificativa: 
- aprofundar DAN-236: `steam desktop client deleted local files root cause fix` — O Steam é um cliente desktop que apagou arquivos locais do usuário, exatamente como o incidente atual; diferem o ecossistema (Linux/Steam) e o gatilho específico.
- aprofundar DAN-146: `dropbox scheduled os upgrade machines wiped out root cause fix` — Envolve máquinas de usuários sendo apagadas após uma atualização, mas o resumo é vago e não cita cliente desktop próprio; pode não bater com o componente do incidente atual.
- aprofundar DAN-173: `heroku filesystem corruption bug fix running containers` — Trata de corrupção de filesystem, mas ocorre em contêineres server-side após deploy, não em cliente desktop apagando arquivos locais do usuário.
  - DAN-236 (llm) [Activity] 0.702: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.699: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 
  - DAN-146 (llm) [sem seção] 0.678: On Friday evening our service went down during scheduled maintenance. The service was back up and running about three hours later, with core service fully restored by 4:40 PM PT on Sunday.  For the pa
  - DAN-146 (llm) [sem seção] 0.528: Over the past few years our infrastructure has grown rapidly to support hundreds of millions of users. We routinely upgrade and repurpose our machines. When doing so, we run scripts that remotely veri
  - DAN-173 (llm) [The Fix] 0.79: ## The Fix  Once we identified the problem, we migrated all affected dynos to fresh hosts, with non-corrupted filesystems and with coherent filesystem caches. This work took the majority of the five h
  - DAN-173 (llm) [sem seção] 0.776: As part of our commitment to security and support, we periodically upgrade the stack image, so that we can install updated package versions, address security vulnerabilities, and add new packages to t
  - DAN-173 (causa) [Technical Impact] 0.453: ## Technical Impact  This problem caught us completely by surprise. While we had taken into account that overwriting a mounted image would cause problems, none of us fully understood what those proble
  - DAN-173 (correcao) [Root Causes] 0.478: ## Root Causes  Near the start of December, we upgraded our container tools. This included changing the digest algorithms and filenames used by these safety checks. We also introduced a latent bug: th
  - DAN-173 (correcao) [Technical Impact] 0.417: ## Technical Impact  - Create a disk image with a simple program on it. We used sleep. dd if=/dev/zero of=demo.img bs=1024 count=10240 mkfs -F -t ext4 demo.img sudo mkdir -p /mnt/demo sudo mount -o lo

## q-279 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-146, DAN-073, DAN-164, DAN-043, DAN-104, DAN-220, DAN-126, DAN-173, DAN-058
- justificativa: 
- aprofundar DAN-236: `steam desktop client deleted all local files root cause fix` — O incidente descreve um cliente de desktop (Steam) que apagou todos os arquivos locais do usuário, exatamente como o incidente atual; não envolve servidor ou infraestrutura.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.703: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (llm) [Activity] 0.695: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 

## q-280 (esperado: DAN-237)

- busca inicial: DAN-237, DAN-142, DAN-152, DAN-131, DAN-136, DAN-011, DAN-124, DAN-122, DAN-034, DAN-090
- justificativa: 
- aprofundar DAN-237: `website compromised malicious zip download link fix root cause` — O site foi comprometido e os links de download apontavam para um zip malicioso, igual ao incidente atual, embora seja um site Linux específico.
- aprofundar DAN-152: `npm malicious package published compromised account fix root cause` — Envolve distribuição de pacotes maliciosos após comprometimento de conta, mas via npm e não download direto de site com zip.
- aprofundar DAN-122: `JCenter malicious Maven package impersonation attack fix root cause` — Envolve pacotes maliciosos inseridos em repositório por ataque de personificação, sem relação direta com download de zip de website.
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.678: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  **Elizabeth K. Joseph**     lyz at ubuntu.com  *Mon Nov 17 17:59:36 UTC 2025*  Dear community, As
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.51: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  in a controlled, read-only mode to allow migration to a new static site. To be perfectly clear: t
  - DAN-237 (causa) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.234: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  generator has actually been in the works for some time as our reliance upon the dynamic features 
  - DAN-152 (llm) [Summary] 0.733: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (llm) [Timeline] 0.719: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.72: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.641: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-

## q-281 (esperado: DAN-237)

- busca inicial: DAN-237, DAN-131, DAN-142, DAN-136, DAN-122, DAN-011, DAN-152, DAN-124, DAN-034, DAN-203
- justificativa: 
- aprofundar DAN-237: `website compromise changed download links malicious zip root cause fix` — O site foi comprometido para servir um zip malicioso via links de download, correspondendo exatamente ao incidente atual.
- aprofundar DAN-122: `malicious packages repository impersonation attack removal fix` — Envolve pacotes maliciosos distribuídos em repositório, canal diferente mas impacto semelhante de artefato malicioso.
- aprofundar DAN-152: `compromised maintainer account malicious packages removal fix` — Conta comprometida usada para publicar pacotes maliciosos, método de ataque semelhante mas canal de distribuição diferente.
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.702: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  **Elizabeth K. Joseph**     lyz at ubuntu.com  *Mon Nov 17 17:59:36 UTC 2025*  Dear community, As
  - DAN-237 (llm) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.535: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  in a controlled, read-only mode to allow migration to a new static site. To be perfectly clear: t
  - DAN-237 (causa) [\[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month] 0.234: # \[xubuntu-users\] Public postmortum of the brief Xubuntu.org torrent download compromise last month  generator has actually been in the works for some time as our reliance upon the dynamic features 
  - DAN-122 (llm) [Malicious packages reported in JCenter] 0.616: ## Malicious packages reported in JCenter  ## Postmortem  ## Course of events  - In July 2017, a user impersonating Jake Wharton asked to include a package in JCenter.  - The package was valid from a 
  - DAN-122 (llm) [Remediation] 0.596: ## Remediation  We tackled the issue on two levels:  ## From a technical perspective:  - Once we saw the blog, we immediately banned the fake user from Bintray and removed the malicious packages creat
  - DAN-122 (causa) [From a process and organizational perspective:] 0.243: ## From a process and organizational perspective:  - We have refreshed the inclusion request process with the Support team. This process includes steps to deal with impersonation attempts, which were 
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.328: ## From a process and organizational perspective:  /picasso/picasso/2.5.2/picasso-2.5.2.pom /jakewhaarton/timber/com/squareup/picasso/picasso/2.5.2/picasso-2.5.2.jar.md5 /jakewhaarton/timber/com/squar
  - DAN-122 (correcao) [From a process and organizational perspective:] 0.198: ## From a process and organizational perspective:  -metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/async-http/maven-metadata.xml.md5 /jakewhaarton/timber/org/asynchttpclient/netty-bp/maven-
  - DAN-152 (llm) [Timeline] 0.61: ## Timeline  - **Before the incident**: The attacker presumably found the maintainer’s reused email and password in a third-party breach and used them to log in to the maintainer’s npm account. - **Ea
  - DAN-152 (llm) [Summary] 0.57: ## Summary  On July 12th, 2018, an attacker compromised the npm account of an ESLint maintainer and published malicious versions of the `eslint-scope` and `eslint-config-eslint` packages to the npm re
  - DAN-152 (correcao) [Recommendations] 0.301: ## Recommendations  With the hindsight of this incident, we have a few recommendations for npm package maintainers and users in the future:  - Package maintainers and users should avoid reusing the sa
  - DAN-152 (correcao) [Affected Packages] 0.244: ## Affected Packages  - `eslint-scope@3.7`, a scope analysis library, is a dependency of several popular packages, including some older versions of `eslint` and the latest versions of `babel-eslint` a

## q-282 (esperado: DAN-240)

- busca inicial: DAN-240, DAN-068, DAN-191, DAN-063, DAN-159, DAN-066, DAN-209, DAN-210, DAN-067, DAN-239
- justificativa: 
- aprofundar DAN-240: `primary leased line backup leased line sporadic order failure root cause fix` — O incidente atual tem link principal caído e link de backup instável afetando ordens, igual ao DAN-240; ambos envolvem corretora e bolsa.
  - DAN-240 (llm) [sem seção] 0.658: 13 Apr 2018, 01:48 PM  # Postmortem: Trading and hanging orders on 12th April 2018  Traders,  Yesterday, on the 12th April, one of the NSE leased line connections to our setup went down. This affected
  - DAN-240 (llm) [Postmortem: Trading and hanging orders on 12th April 2018] 0.47: # Postmortem: Trading and hanging orders on 12th April 2018  Once the CTCL was shut off, the orders which were showing any of the pending states were lapsed and reconciled with the exchange. This affe

## q-283 (esperado: DAN-240)

- busca inicial: DAN-240, DAN-209, DAN-191, DAN-068, DAN-239, DAN-077, DAN-205, DAN-067, DAN-106, DAN-159
- justificativa: 
- aprofundar DAN-240: `primary leased line backup sporadic orders failing root cause fix` — É o único incidente com mesmo componente (linha alugada para bolsa), mesmo gatilho (primária caiu, secundária instável) e mesmo impacto (ordens falhando). Os outros são de nuvem, data center ou rede interna, não linha alugada de exchange.
  - DAN-240 (llm) [sem seção] 0.635: 13 Apr 2018, 01:48 PM  # Postmortem: Trading and hanging orders on 12th April 2018  Traders,  Yesterday, on the 12th April, one of the NSE leased line connections to our setup went down. This affected
  - DAN-240 (llm) [Postmortem: Trading and hanging orders on 12th April 2018] 0.469: # Postmortem: Trading and hanging orders on 12th April 2018  Once the CTCL was shut off, the orders which were showing any of the pending states were lapsed and reconciled with the exchange. This affe

## q-284 (esperado: DAN-164)

- busca inicial: DAN-164, DAN-043, DAN-209, DAN-189, DAN-208, DAN-146, DAN-048, DAN-126, DAN-195, DAN-186
- justificativa: 
- aprofundar DAN-164: `tired admin deleted wrong directory data loss root cause fix` — O resumo menciona exatamente um administrador cansado que apagou o diretório errado e perdeu seis horas de dados, idêntico ao incidente atual.
- aprofundar DAN-043: `accidentally deleted production database backup recovery data loss` — Engenheiros excluíram acidentalmente o banco de produção e perderam horas de dados, semelhança na causa humana e no impacto, embora seja um banco gerenciado e não um diretório.
  - DAN-164 (llm) [Root cause analysis] 0.605: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.522: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.707: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.692: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo

## q-285 (esperado: DAN-164)

- busca inicial: DAN-164, DAN-043, DAN-209, DAN-146, DAN-186, DAN-208, DAN-230, DAN-056, DAN-058, DAN-189
- justificativa: 
- aprofundar DAN-164: `tired admin deleted wrong directory six hours data lost root cause fix` — Corresponde exatamente ao incidente atual: administrador cansado apagou o diretório errado e perdeu seis horas de dados, no GitLab.
- aprofundar DAN-043: `accidental production database deletion backup recovery data loss fix` — Semelhança forte: exclusão acidental de banco de produção com perda de várias horas de dados, embora seja banco gerenciado e não um diretório.
- aprofundar DAN-056: `accidental environment variable truncate production database root cause fix` — Semelhança moderada: erro humano causou truncamento acidental do banco de produção, mas sem menção a administrador cansado ou diretório.
  - DAN-164 (llm) [Root cause analysis] 0.632: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.548: ## Timeline  Unfortunately this did not resolve the problem of `pg_basebackup` not starting replication immediately. One of the engineers decided to run it with `strace` to see what it was blocking on
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.724: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.669: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo
  - DAN-056 (llm) [What We Learned] 0.73: ## What We Learned  We have held an internal incident retrospective to learn more about how the data failure occurred, what can be improved on our side to protect against such a failure, and how to be
  - DAN-056 (llm) [Remediation] 0.694: ## Remediation  Steps we have taken to avoid accidental database table truncation:  - Revoked the truncate permission on our databases, effectively making it impossible for tables to be truncated.  - 
  - DAN-056 (causa) [Conclusion] 0.496: ## Conclusion  Here at Travis CI we take security very seriously. The data failure we experienced was unprecedented in both scope and size. Unfortunately, when responding we missed some steps which wo
  - DAN-056 (correcao) [Update] 0.416: ## Update  Database provisioning from the recovery point is still underway. We are doing preparatory work to deal with increased demand when travis-ci.com comes back online. We also continue to invest
  - DAN-056 (correcao) [What happened] 0.404: ## What happened  On Tuesday, 13 March 2018 at 12:04 UTC a database query was accidentally run against our production database which truncated all tables. The query was blocked for around 10 minutes a

## q-286 (esperado: DAN-104)

- busca inicial: DAN-104, DAN-105, DAN-230, DAN-073, DAN-064, DAN-164, DAN-125, DAN-048, DAN-189, DAN-106
- justificativa: 
- aprofundar DAN-104: `S3 typo command removed too many servers root cause fix` — Mesmo componente (S3) e mesma falha humana: comando com digitação errada removeu mais servidores do que o planejado, derrubando armazenamento; difere em data e escala.
- aprofundar DAN-189: `operator rebooted all servers lax input validation root cause fix` — Mesmo padrão de erro de escopo: comando destinado a poucos servidores afetou todos por validação falha; difere no componente (reinício vs remoção S3).
- aprofundar DAN-164: `admin deleted wrong directory database root cause fix` — Mesma categoria de erro humano: exclusão de recurso errado por admin cansado; difere no componente (diretório de banco vs servidores S3).
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.595: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.573: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-189 (llm) [What Happened?] 0.632: ## What Happened?  Due to an operator error, all us-east-1 API systems and customer instances were simultaneously rebooted at 2014-05-27T20:13Z (13:13PDT). Rounded to minutes, the minimum downtime for
  - DAN-189 (llm) [Next Steps] 0.564: ## Next Steps  We will be taking several steps to prevent this failure mode from happening again, and ensuring that other business disaster scenarios are able to recover more quickly.  First, we will 
  - DAN-189 (causa) [What Happened?] 0.499: ## What Happened?  The small number of machines that lagged for the remaining time were subject to a known, transient bug in a network card driver on legacy hardware platforms whereby obtaining a DHCP
  - DAN-189 (correcao) [Closing] 0.539: ## Closing  We want to reiterate our apology for the magnitude of this issue and the impact it caused our customers and their customers. We will be working as diligently as we can, and as expediently 
  - DAN-189 (correcao) [Postmortem for outage of us-east-1] 0.441: ## Postmortem for outage of us-east-1  May 28, 2014 - by The Joyent Team  We would like to share the details on what occurred during the outage on 5/27/2014 in our us-east-1 data center, what we have 
  - DAN-164 (llm) [Root cause analysis] 0.638: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [Timeline] 0.534: ## Timeline  On January 31st an engineer started setting up multiple PostgreSQL servers in our staging environment. The plan was to try out pgpool-II to see if it would reduce the load on our database
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 

## q-287 (esperado: DAN-104)

- busca inicial: DAN-104, DAN-105, DAN-230, DAN-125, DAN-073, DAN-044, DAN-164, DAN-064, DAN-118, DAN-036
- justificativa: 
- aprofundar DAN-104: `typo command removed servers S3 outage root cause fix` — Bate exatamente: comando com erro de digitação removeu mais servidores do que o previsto e derrubou o S3, causando pane em larga escala. Não bate em detalhes de correção específica, que ainda não conhecemos.
- aprofundar DAN-164: `admin deleted wrong directory database outage root cause fix` — Bate parcialmente: erro humano de exclusão/direção errada derrubou serviço, mas não é S3 nem envolve remoção de servidores por comando digitado.
- aprofundar DAN-044: `bad config took down Azure storage root cause fix` — Bate parcialmente: erro de configuração derrubou storage, mas não é comando digitado errado nem remoção de servidores, e é Azure, não S3.
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.676: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.652: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-164 (llm) [Root cause analysis] 0.699: ## Root cause analysis  To analyse the root cause of these problems we'll use a technique called "The 5 Whys". We'll break up the incident into 2 main problems: GitLab.com being down, and it taking a 
  - DAN-164 (llm) [sem seção] 0.588: On January 31st 2017, we experienced a major service outage for one of our products, the online service GitLab.com. The outage was caused by an accidental removal of data from our primary database ser
  - DAN-164 (causa) [Root cause analysis] 0.474: ## Root cause analysis  2. **Why was the staging database needed for restoring GitLab.com?** - Azure disk snapshots were not enabled for the database servers, and the periodic database backups using `
  - DAN-164 (correcao) [Improving recovery procedures] 0.447: ## Improving recovery procedures  We are currently working on fixing and improving our various recovery procedures. Work is split across the following issues:  1. Overview of status of all issues list
  - DAN-164 (correcao) [Improving recovery procedures] 0.396: ## Improving recovery procedures  An ideal environment is one in which you *can* make mistakes but easily and quickly recover from them with minimal to no impact. This in turn requires you to be able 
  - DAN-044 (llm) [Update to Azure Customers:] 0.741: ## Update to Azure Customers:  Incident Information Incident ID 3071402 Incident Title Microsoft Azure Service Incident : Connectivity to multiple Azure Services – Partial Service Interruption Service
  - DAN-044 (llm) [Update to Azure Customers:] 0.73: ## Update to Azure Customers:  The configuration change for the Blob Front-Ends exposed a bug in the Blob Front-Ends, which had been previously performing as expected for the Table Front-Ends. This bu
  - DAN-044 (causa) [Update to Azure Customers:] 0.39: ## Update to Azure Customers:  As a mitigation, we leveraged Twitter and other social media forums. We also provided targeted communication to the Management Portal for affected customers as available
  - DAN-044 (correcao) [sem seção] 0.481: Once we detected this issue, the change was rolled back promptly, but a restart of the storage front ends was required in order to fully undo the update. Once the mitigation steps were deployed, most 
  - DAN-044 (correcao) [Update to Azure Customers:] 0.436: ## Update to Azure Customers:  We will continue to investigate what led to this event and will drive the needed improvements to avoid similar situations in the future. In the meantime, we believe it’s

## q-288 (esperado: DAN-090)

- busca inicial: DAN-090, DAN-025, DAN-216, DAN-086, DAN-023, DAN-136, DAN-024, DAN-032, DAN-005, DAN-137
- justificativa: 
- aprofundar DAN-090: `expired certificate Firefox add-ons root cause fix` — Mesmo componente (complementos Firefox), mesmo gatilho (certificado expirou) e mesma falha (add-ons pararam de funcionar) do incidente atual.
- aprofundar DAN-086: `certificate expiration Azure root cause fix` — Causa raiz semelhante (expiração/rejeição de certificado), mas componente diferente (Azure, não Firefox add-ons).
  - DAN-090 (llm) [Root Cause Analysis] 0.751: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [Incomplete Fixes] 0.581: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (causa) [sem seção] 0.366: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a
  - DAN-086 (llm) [The Leap Day Bug] 0.632: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.628: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-289 (esperado: DAN-090)

- busca inicial: DAN-090, DAN-025, DAN-216, DAN-086, DAN-136, DAN-154, DAN-032, DAN-024, DAN-126, DAN-023
- justificativa: 
- aprofundar DAN-090: `expired certificate Firefox add-ons fix root cause` — corresponde exatamente: certificado expirado fez add-ons do Firefox pararem, mesmo componente e gatilho do incidente atual
- aprofundar DAN-086: `certificate expiration invalid date fix root cause Azure outage` — também envolve expiração de certificado, mas em serviço Azure e com gatilho diferente (ano bissexto), não é Firefox nem add-ons
  - DAN-090 (llm) [Root Cause Analysis] 0.75: ## Root Cause Analysis  The first question that everyone asks is “how did you let this happen?” At a high level, the story seems simple: we let the certificate expire. This seems like a simple failure
  - DAN-090 (llm) [sem seção] 0.583: *Editor’s Note: July 12, 1:52pm pt – Updated Balrog update frequency and added some more background.*  As I mentioned in my previous post, we’ve been conducting a post-mortem on the add-ons outage. So
  - DAN-090 (causa) [Incomplete Fixes] 0.422: ## Incomplete Fixes  Over the weeks following the incident, we released a large number of fixes, including eight versions of the system add-on and six dot releases. In some cases this was necessary be
  - DAN-090 (correcao) [Where to Learn More] 0.374: ## Where to Learn More  If you want to learn more about our findings, I would invite you to read the more detailed reports we produced. And as always, if those don’t answer your questions, feel free t
  - DAN-090 (correcao) [Code Delivery] 0.315: ## Code Delivery  As I mentioned previously, once we had a fix, we decided to deliver it via the Studies system (this is one part of a system we internally call “Normandy”). The Studies system isn’t a
  - DAN-086 (llm) [The Leap Day Bug] 0.672: ## The Leap Day Bug  When the GA creates the transfer certificate, it gives it a one year validity range. It uses midnight UST of the current day as the *valid-from* date and one year from that date a
  - DAN-086 (llm) [The Leap Day Bug in Action] 0.667: ## The Leap Day Bug in Action  The leap day bug immediately triggered at 4:00PM PST, February 28<sup>th</sup> (00:00 UST February 29<sup>th</sup>) when GAs in new VMs tried to generate certificates. S
  - DAN-086 (causa) [Prevention] 0.484: ### Prevention  - **Testing.** The root cause of the initial outage was a software bug due to the incorrect manipulation of date/time values.  We are taking steps that improve our testing to detect ti
  - DAN-086 (correcao) [Improving the Service] 0.519: ## Improving the Service  After an incident occurs, we take the time to analyze the incident and ways we can improve our engineering, operations and communications. To learn as much as we can, we do t
  - DAN-086 (correcao) [Recovery] 0.429: ### Recovery  - **Internal tooling.**  We developed and modified some of our internal tooling to address this incident.  We will continue to invest in our tools to help speed recovery and make recover

## q-290 (esperado: DAN-071)

- busca inicial: DAN-067, DAN-068, DAN-071, DAN-231, DAN-209, DAN-062, DAN-048, DAN-064, DAN-191, DAN-060
- justificativa: 
- aprofundar DAN-071: `lightning strikes datacenter power loss storage disks root cause fix` — Bate exatamente: raios atingiram datacenter, causaram perda de energia e afetaram discos/storage. Difere apenas pelo provedor (Google) e região europeia.
- aprofundar DAN-062: `severe weather power loss AWS Sydney backup generators fix` — Bate parcialmente: clima severo causou perda de energia em datacenter. Não bate em raios específicos nem em impacto direto nos discos.
- aprofundar DAN-068: `breaker coordination power loss data center fix remediation` — Bate parcialmente: falha completa de energia em datacenter. Não bate em raios nem em discos; causa foi configuração incorreta de disjuntores.
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.669: # Google Compute Engine Incident #15056  Some management operations on the affected disks also failed, such as disk snapshot creation. From the start of the incident, the number of affected disks prog
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.609: # Google Compute Engine Incident #15056  However, in a very few cases, recent writes were unrecoverable, leading to permanent data loss on the Persistent Disk. This outage is wholly Google's responsib
  - DAN-071 (causa) [Google Compute Engine Incident #15056] 0.415: # Google Compute Engine Incident #15056  Google Compute Engine Persistent Disk issue in europe-west1-b  Incident began at **2015-08-13 09:25**  and ended at **2015-08-16 09:35**  (all times are **US/P
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.335: # Google Compute Engine Incident #15056  The service has been partially recovered. Meanwhile, affected customers can restore from snapshots as a workaround solution. We will provide another status upd
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.324: # Google Compute Engine Incident #15056  Please also feel free to proactively contact support for more information. We will conduct an internal investigation of this issue and make appropriate improve
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.739: ### Summary of the AWS Service Event in the Sydney Region  If utility power is interrupted, the DRUPS uses this stored energy to continue to provide power to the datacenter while the integrated genera
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.729: ### Summary of the AWS Service Event in the Sydney Region  We’d like to share more detail about the AWS service disruption that occurred this past weekend in the AWS Sydney Region. The service disrupt
  - DAN-062 (causa) [Summary of the AWS Service Event in the Sydney Region] 0.399: ### Summary of the AWS Service Event in the Sydney Region  A latent bug in our instance management software led to a slower than expected recovery of the remaining instances. The team worked over the 
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.388: ### Summary of the AWS Service Event in the Sydney Region  Additionally, we will be taking actions to improve our recovery systems. The first is to fix the latent issue that led to our recovery system
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.359: ### Summary of the AWS Service Event in the Sydney Region  During the initial part of this event, customers experienced errors when trying to launch new instances, or when trying to scale their auto-s
  - DAN-068 (llm) [What happened to the power in the data center?] 0.726: ### What happened to the power in the data center?  Initial assessment of the root cause of Flexential’s CSB failures points to incorrectly set breaker coordination settings within the four CSBs as on
  - DAN-068 (llm) [What happened to the power in the data center?] 0.665: ### What happened to the power in the data center?  On March 26, 2024, at 14:58 UTC, PDX01 experienced a total loss of power to Cloudflare’s physical infrastructure following a reportedly simultaneous
  - DAN-068 (causa) [sem seção] 0.501: Here's a post we never thought we'd need to write: less than five months after one of our major data centers lost power, it happened again to the exact same data center. That sucks and, if you're thin
  - DAN-068 (correcao) [What’s next?] 0.446: ### What’s next?  Our top priority is completing the resilience program for our Analytics platform. Analytics aren’t simply pretty charts in a dashboard. When you want to check the status of attacks, 
  - DAN-068 (correcao) [How did we get here?] 0.43: ### How did we get here?  As mentioned above, the power outage event from last November led us to introduce Code Orange, a process where we shift most or all engineering resources to addressing the is

## q-291 (esperado: DAN-071)

- busca inicial: DAN-071, DAN-068, DAN-067, DAN-062, DAN-060, DAN-061, DAN-064, DAN-231, DAN-191, DAN-070
- justificativa: 
- aprofundar DAN-071: `lightning strikes europe-west1-b power loss persistent disks root cause fix` — bate por raios, datacenter, perda de energia e discos; não bate por ser Google Cloud e não on-premise.
- aprofundar DAN-062: `severe weather power loss AWS Sydney root cause fix` — bate por perda de energia por clima severo em datacenter; não bate por não mencionar raios nem discos.
- aprofundar DAN-070: `datacenter power disruption GitHub servers Redis root cause fix` — bate por interrupção de energia em datacenter principal; não bate por não citar raios nem falha em discos.
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.735: # Google Compute Engine Incident #15056  Some management operations on the affected disks also failed, such as disk snapshot creation. From the start of the incident, the number of affected disks prog
  - DAN-071 (llm) [Google Compute Engine Incident #15056] 0.709: # Google Compute Engine Incident #15056  | |  | SUMMARY: From Thursday 13 August 2015 to Monday 17 August 2015, errors occurred on a small proportion of Google Compute Engine persistent disks in the e
  - DAN-071 (causa) [Google Compute Engine Incident #15056] 0.415: # Google Compute Engine Incident #15056  Google Compute Engine Persistent Disk issue in europe-west1-b  Incident began at **2015-08-13 09:25**  and ended at **2015-08-16 09:35**  (all times are **US/P
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.358: # Google Compute Engine Incident #15056  However, in a very few cases, recent writes were unrecoverable, leading to permanent data loss on the Persistent Disk. This outage is wholly Google's responsib
  - DAN-071 (correcao) [Google Compute Engine Incident #15056] 0.335: # Google Compute Engine Incident #15056  The service has been partially recovered. Meanwhile, affected customers can restore from snapshots as a workaround solution. We will provide another status upd
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.745: ### Summary of the AWS Service Event in the Sydney Region  If utility power is interrupted, the DRUPS uses this stored energy to continue to provide power to the datacenter while the integrated genera
  - DAN-062 (llm) [Summary of the AWS Service Event in the Sydney Region] 0.74: ### Summary of the AWS Service Event in the Sydney Region  We’d like to share more detail about the AWS service disruption that occurred this past weekend in the AWS Sydney Region. The service disrupt
  - DAN-062 (causa) [Summary of the AWS Service Event in the Sydney Region] 0.399: ### Summary of the AWS Service Event in the Sydney Region  A latent bug in our instance management software led to a slower than expected recovery of the remaining instances. The team worked over the 
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.388: ### Summary of the AWS Service Event in the Sydney Region  Additionally, we will be taking actions to improve our recovery systems. The first is to fix the latent issue that led to our recovery system
  - DAN-062 (correcao) [Summary of the AWS Service Event in the Sydney Region] 0.359: ### Summary of the AWS Service Event in the Sydney Region  During the initial part of this event, customers experienced errors when trying to launch new instances, or when trying to scale their auto-s
  - DAN-070 (llm) [The Event] 0.737: ## The Event  By this point, we had a fairly clear picture of what was required to restore service and began working towards that end. We needed to repair our servers that were not booting, and we nee
  - DAN-070 (llm) [The Event] 0.681: ## The Event  At 00:23am UTC on Thursday, January 28th, 2016 (4:23pm PST, Wednesday, January 27th) our primary data center experienced a brief disruption in the systems that supply power to our server
  - DAN-070 (causa) [Future Work] 0.507: ## Future Work  Complex systems are defined by the interaction of many discrete components working together to achieve an end result. Understanding the dependencies for each component in a complex sys
  - DAN-070 (correcao) [Future Work] 0.534: ## Future Work  A number of less technical improvements are also being implemented. Strengthening our cross-team communications would have shaved minutes off the recovery time. Predefining escalation 
  - DAN-070 (correcao) [In Conclusion] 0.461: ## In Conclusion  We realize how important GitHub is to the workflows that enable your projects and businesses to succeed. All of us at GitHub would like to apologize for the impact of this outage. We

## q-292 (esperado: DAN-084)

- busca inicial: DAN-084, DAN-050, DAN-106, DAN-207, DAN-017, DAN-042, DAN-092, DAN-154, DAN-116, DAN-125
- justificativa: 
- aprofundar DAN-084: `conflicting deployed versions root cause fix 460M loss` — O resumo menciona versões conflitantes implantadas e perda de $460M, exatamente como o incidente atual; não há diferença aparente no cenário.
  - DAN-084 (llm) [45 Minutes of Hell] 0.507: ## 45 Minutes of Hell  During the 45-minutes of Hell that Knight experienced they attempted several counter measures to try and stop the erroneous trades. There was no kill-switch (and no documented p
  - DAN-084 (llm) [What Could Possibly Go Wrong? Indeed!] 0.498: ## What Could Possibly Go Wrong? Indeed!  Between July 27, 2012 and July 31, 2012 Knight manually deployed the new software to a limited number of servers per day – eight (8) servers in all. This is w
  - DAN-084 (causa) [sem seção] 0.424: I was speaking at a conference last year on the topics of DevOps, Configuration as Code, and Continuous Delivery and used the following story to demonstrate the importance making deployments fully aut
  - DAN-084 (correcao) [A Lesson to Learn] 0.316: ## A Lesson to Learn  The events of August 1, 2012 should be a lesson to all development and operations teams. It is not enough to build great software and test it; you also have to ensure it is deliv
  - DAN-084 (correcao) [Attack of the Killer Code Zombies] 0.361: ## Attack of the Killer Code Zombies  Its important to understand what the “dead” Power Peg code was meant to do. This functionality was meant to count the shares bought/sold against a parent order as

## q-293 (esperado: DAN-084)

- busca inicial: DAN-084, DAN-050, DAN-207, DAN-106, DAN-042, DAN-017, DAN-116, DAN-068, DAN-125, DAN-191
- justificativa: 
- aprofundar DAN-084: `conflicting deployed versions root cause fix rollback $460M loss` — Corresponde exatamente ao incidente atual: deploy de versões conflitantes do código causando perda de $460 milhões (Knight Capital).
  - DAN-084 (llm) [45 Minutes of Hell] 0.534: ## 45 Minutes of Hell  During the 45-minutes of Hell that Knight experienced they attempted several counter measures to try and stop the erroneous trades. There was no kill-switch (and no documented p
  - DAN-084 (llm) [sem seção] 0.518: I was speaking at a conference last year on the topics of DevOps, Configuration as Code, and Continuous Delivery and used the following story to demonstrate the importance making deployments fully aut
  - DAN-084 (causa) [What Could Possibly Go Wrong? Indeed!] 0.41: ## What Could Possibly Go Wrong? Indeed!  Between July 27, 2012 and July 31, 2012 Knight manually deployed the new software to a limited number of servers per day – eight (8) servers in all. This is w
  - DAN-084 (correcao) [A Lesson to Learn] 0.316: ## A Lesson to Learn  The events of August 1, 2012 should be a lesson to all development and operations teams. It is not enough to build great software and test it; you also have to ensure it is deliv
  - DAN-084 (correcao) [Attack of the Killer Code Zombies] 0.361: ## Attack of the Killer Code Zombies  Its important to understand what the “dead” Power Peg code was meant to do. This functionality was meant to count the shares bought/sold against a parent order as

## q-294 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-059, DAN-073, DAN-104, DAN-146, DAN-054, DAN-231, DAN-220, DAN-191, DAN-043
- justificativa: 
- aprofundar DAN-236: `Steam client deleted all local files root cause fix` — Mesmo produto (Steam) e mesmo sintoma (cliente apagou arquivos do usuário), mas o resumo não detalha a causa técnica nem a correção.
- aprofundar DAN-104: `S3 typo command removed servers root cause fix` — Erro humano em comando de remoção apagou mais do que o pretendido, semelhante à exclusão excessiva, mas em serviço S3, não cliente Steam.
- aprofundar DAN-043: `accidental production database deletion recovery fix` — Exclusão acidental de dados críticos com perda permanente, semelhante à perda de arquivos do usuário, mas escopo diferente (banco vs sistema de arquivos).
  - DAN-236 (llm) [Activity] 0.725: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [doofy commentedon Jan 15, 2015] 0.717: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [jthill commentedon Jan 15, 2015] 0.307: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.586: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We’d like to give you some additional information about the service disruption that occurred in the Northern
  - DAN-104 (llm) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.554: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  We are making several changes as a result of this operational event. While removal of capacity is a key oper
  - DAN-104 (causa) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.312: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  S3 subsystems are designed to support the removal or failure of significant capacity with little or no custo
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.303: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  From the beginning of this event until 11:37AM PST, we were unable to update the individual services’ status
  - DAN-104 (correcao) [Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region] 0.219: ## Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region  One of these subsystems, the index subsystem, manages the metadata and location information of all S3 object
  - DAN-043 (llm) [What have we learned? Why won’t this happen again?] 0.727: ## What have we learned? Why won’t this happen again?  We’ve learned that having a function that deletes your database is too dangerous to have lying around. The problem is, you can never really test 
  - DAN-043 (llm) [sem seção] 0.675: Today at around 10:45pm CET, after a couple of glasses of red wine, we deleted the production database by accident 😨. Over 300.00 scoreboards and their associated data were vaporised in an instant.  T
  - DAN-043 (causa) [Some perspective] 0.425: ## Some perspective  Thankfully nobody’s job is at risk due to this disaster. The founder is not going to fire the developer – because they are one and the same person.  Also, this webapp is just a si
  - DAN-043 (correcao) [What happened?] 0.323: ## What happened?  It’s tempting to blame the disaster on the couple of glasses of red wine. However, the function that wiped the database was written whilst sober. It’s a function that deletes the lo

## q-295 (esperado: DAN-236)

- busca inicial: DAN-236, DAN-059, DAN-073, DAN-076, DAN-146, DAN-142, DAN-050, DAN-054, DAN-043, DAN-104
- justificativa: 
- aprofundar DAN-236: `steam client deleted files root cause fix rm -rf` — Mesmo componente (cliente Steam) e mesma falha (exclusão de todos os arquivos do usuário), embora o relato conhecido seja Linux e o atual possa ser Windows.
- aprofundar DAN-076: `boot.ini deletion installer typo expansion fix` — Envolve instalador de jogo deletando arquivo do sistema, mas não é o Steam nem exclui todos os arquivos do usuário.
- aprofundar DAN-054: `automated cleanup deleted VM images configuration fix` — Envolve exclusão acidental em massa por rotina automatizada, mas não é cliente Steam nem arquivos do usuário final.
  - DAN-236 (llm) [Activity] 0.704: ## Activity  1. I am impressed how calm you stay about this. This is terrible. I just lost my home directory. All i did was start steam.sh with STEAM\_DEBUG=1. I will investigate this and report back.
  - DAN-236 (llm) [jthill commentedon Jan 15, 2015] 0.698: ## jthill commentedon Jan 15, 2015  @minio Not "only if".  `reset_steam`is also invoked by removing your`INITIAL_LAUNCH` ## soren121 commentedon Jan 15, 2015  @minio A script accidentally running  `rm
  - DAN-236 (causa) [Activity] 0.274: ## Activity  but what exactly caused this? i've symlinked \~/.local/share/steam to, so i am a bit afraid to start steam :/ Reacted by Shaun Henderson, Barry Haertel, Agustín Covarrubias and Eddie Anto
  - DAN-236 (correcao) [doofy commentedon Jan 15, 2015] 0.293: ## doofy commentedon Jan 15, 2015  ## Tele42 commentedon Jan 15, 2015  ## keyvin commentedon Jan 15, 2015  ## CamilleScholtz commentedon Jan 15, 2015  This also happened to me a few weeks ago, my enti
  - DAN-236 (correcao) [Activity] 0.28: ## Activity  8. I encountered Steam behaviour like with «--reset» for several times: when I added «--reset» AND when I didn't. So — not «only if», can confirm this, even having not deleted \~/.steam/ 
  - DAN-076 (llm) [About the boot.ini issue] 0.764: # About the boot.ini issue  Initially we had planned to use our third-party patching technology to create the graphics content upgrade file; however, we realized late in the development cycle that whi
  - DAN-076 (llm) [About the boot.ini issue] 0.726: # About the boot.ini issue  The assumption was that by setting *SetOutPath "$INSTDIR"* then all commands that followed would use that working directory.  The *File* commands use the output path that h
  - DAN-076 (causa) [About the boot.ini issue] 0.38: # About the boot.ini issue  *Why wasn't this caught in a code review?* The installer scripting language is not easy to read. We had been working very hard for many weeks prior to release, evenings and
  - DAN-076 (correcao) [About the boot.ini issue] 0.357: # About the boot.ini issue  My name is Dr. Erlendur S. Thorsteinsson and I have been directing the EVE Online Software Group for the better part of this year. From my previous work experiences in the 
  - DAN-054 (llm) [What happened?] 0.754: ## What happened?  In addition, our cleanup service had been briefly disabled to troubleshooting a potential race condition. Then we turned the automated cleanup back on. The service had a **default h
  - DAN-054 (llm) [What are we doing about it?] 0.743: ## What are we doing about it?  Counter measures we have already in place:  - **Reproducible image provisioning process.** This allows us to rebuild an exact image easily if it should be deleted. Whil
  - DAN-054 (causa) [sem seção] 0.444: On August 9, we had a major incident on our Google Compute Engine setup. This was something more than just an outage. Our system wasn’t just down for an extended period of time, we permanently lost ou
  - DAN-054 (correcao) [What was the impact for our customers?] 0.355: ## What was the impact for our customers?  A 90 minute, unscheduled outage is something we try our best to avoid. From large enterprises to hobby, side projects, proprietary and open source projects, 
  - DAN-054 (correcao) [What happened?] 0.256: ## What happened?  When you use the hosted version of Travis CI, whether it is travis-ci.com or travis-ci.org, your build jobs are running on one of three platforms:  - **A docker container inside an 
