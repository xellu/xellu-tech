
import type { CustomThemeConfig } from '@skeletonlabs/tw-plugin';

export const appTheme: CustomThemeConfig = {
    name: 'app-theme',
	properties: {
		// =~= Theme Properties =~=
		"--theme-font-family-base": `"Inter", sans-serif`,
		"--theme-font-family-heading": `"Plus Jakarta Sans", serif`,
		"--theme-font-color-base": "0 0 0",
		"--theme-font-color-dark": "255 255 255",
		"--theme-rounded-base": "8px",
		"--theme-rounded-container": "8px",
		"--theme-border-base": "1px",
		// =~= Theme On-X Colors =~=
		"--on-primary": "0 0 0",
		"--on-secondary": "255 255 255",
		"--on-tertiary": "0 0 0",
		"--on-success": "0 0 0",
		"--on-warning": "0 0 0",
		"--on-error": "0 0 0",
		"--on-surface": "255 255 255",
		// =~= Theme Colors  =~=
		// primary | #e63440 
		"--color-primary-50": "251 225 226", // #fbe1e2
		"--color-primary-100": "250 214 217", // #fad6d9
		"--color-primary-200": "249 204 207", // #f9cccf
		"--color-primary-300": "245 174 179", // #f5aeb3
		"--color-primary-400": "238 113 121", // #ee7179
		"--color-primary-500": "230 52 64", // #e63440
		"--color-primary-600": "207 47 58", // #cf2f3a
		"--color-primary-700": "173 39 48", // #ad2730
		"--color-primary-800": "138 31 38", // #8a1f26
		"--color-primary-900": "113 25 31", // #71191f
		// secondary | #8a1149 
		"--color-secondary-50": "237 219 228", // #eddbe4
		"--color-secondary-100": "232 207 219", // #e8cfdb
		"--color-secondary-200": "226 196 210", // #e2c4d2
		"--color-secondary-300": "208 160 182", // #d0a0b6
		"--color-secondary-400": "173 88 128", // #ad5880
		"--color-secondary-500": "138 17 73", // #8a1149
		"--color-secondary-600": "124 15 66", // #7c0f42
		"--color-secondary-700": "104 13 55", // #680d37
		"--color-secondary-800": "83 10 44", // #530a2c
		"--color-secondary-900": "68 8 36", // #440824
		// tertiary | #988df1 
		"--color-tertiary-50": "240 238 253", // #f0eefd
		"--color-tertiary-100": "234 232 252", // #eae8fc
		"--color-tertiary-200": "229 227 252", // #e5e3fc
		"--color-tertiary-300": "214 209 249", // #d6d1f9
		"--color-tertiary-400": "183 175 245", // #b7aff5
		"--color-tertiary-500": "152 141 241", // #988df1
		"--color-tertiary-600": "137 127 217", // #897fd9
		"--color-tertiary-700": "114 106 181", // #726ab5
		"--color-tertiary-800": "91 85 145", // #5b5591
		"--color-tertiary-900": "74 69 118", // #4a4576
		// success | #01f349 
		"--color-success-50": "217 253 228", // #d9fde4
		"--color-success-100": "204 253 219", // #ccfddb
		"--color-success-200": "192 252 210", // #c0fcd2
		"--color-success-300": "153 250 182", // #99fab6
		"--color-success-400": "77 247 128", // #4df780
		"--color-success-500": "1 243 73", // #01f349
		"--color-success-600": "1 219 66", // #01db42
		"--color-success-700": "1 182 55", // #01b637
		"--color-success-800": "1 146 44", // #01922c
		"--color-success-900": "0 119 36", // #007724
		// warning | #ffe23e 
		"--color-warning-50": "255 251 226", // #fffbe2
		"--color-warning-100": "255 249 216", // #fff9d8
		"--color-warning-200": "255 248 207", // #fff8cf
		"--color-warning-300": "255 243 178", // #fff3b2
		"--color-warning-400": "255 235 120", // #ffeb78
		"--color-warning-500": "255 226 62", // #ffe23e
		"--color-warning-600": "230 203 56", // #e6cb38
		"--color-warning-700": "191 170 47", // #bfaa2f
		"--color-warning-800": "153 136 37", // #998825
		"--color-warning-900": "125 111 30", // #7d6f1e
		// error | #ff442f 
		"--color-error-50": "255 227 224", // #ffe3e0
		"--color-error-100": "255 218 213", // #ffdad5
		"--color-error-200": "255 208 203", // #ffd0cb
		"--color-error-300": "255 180 172", // #ffb4ac
		"--color-error-400": "255 124 109", // #ff7c6d
		"--color-error-500": "255 68 47", // #ff442f
		"--color-error-600": "230 61 42", // #e63d2a
		"--color-error-700": "191 51 35", // #bf3323
		"--color-error-800": "153 41 28", // #99291c
		"--color-error-900": "125 33 23", // #7d2117
		// surface | #060e1a 
		"--color-surface-50": "218 219 221", // #dadbdd
		"--color-surface-100": "205 207 209", // #cdcfd1
		"--color-surface-200": "193 195 198", // #c1c3c6
		"--color-surface-300": "155 159 163", // #9b9fa3
		"--color-surface-400": "81 86 95", // #51565f
		"--color-surface-500": "6 14 26", // #060e1a
		"--color-surface-600": "5 13 23", // #050d17
		"--color-surface-700": "5 11 20", // #050b14
		"--color-surface-800": "4 8 16", // #040810
		"--color-surface-900": "3 7 13", // #03070d
		
	}
}