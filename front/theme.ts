
import type { CustomThemeConfig } from '@skeletonlabs/tw-plugin';

export const appTheme: CustomThemeConfig = {
    name: 'app-theme',
    properties: {
		// =~= Theme Properties =~=
		"--theme-font-family-base": `"Inter", sans-serif`,
		"--theme-font-family-heading": `"Inter", sans-serif`,
		"--theme-font-color-base": "255 255 255",
		"--theme-font-color-dark": "255 255 255",
		"--theme-rounded-base": "8px",
		"--theme-rounded-container": "8px",
		"--theme-border-base": "1px",
		// =~= Theme On-X Colors =~=
		"--on-primary": "255 255 255",
		"--on-secondary": "0 0 0",
		"--on-tertiary": "0 0 0",
		"--on-success": "0 0 0",
		"--on-warning": "0 0 0",
		"--on-error": "0 0 0",
		"--on-surface": "255 255 255",
		// =~= Theme Colors  =~=
		// primary | #0766AD 
		"--color-primary-50": "218 232 243", // #dae8f3
		"--color-primary-100": "205 224 239", // #cde0ef
		"--color-primary-200": "193 217 235", // #c1d9eb
		"--color-primary-300": "156 194 222", // #9cc2de
		"--color-primary-400": "81 148 198", // #5194c6
		"--color-primary-500": "7 102 173", // #0766AD
		"--color-primary-600": "6 92 156", // #065c9c
		"--color-primary-700": "5 77 130", // #054d82
		"--color-primary-800": "4 61 104", // #043d68
		"--color-primary-900": "3 50 85", // #033255
		// secondary | #29ADB2 
		"--color-secondary-50": "223 243 243", // #dff3f3
		"--color-secondary-100": "212 239 240", // #d4eff0
		"--color-secondary-200": "202 235 236", // #caebec
		"--color-secondary-300": "169 222 224", // #a9dee0
		"--color-secondary-400": "105 198 201", // #69c6c9
		"--color-secondary-500": "41 173 178", // #29ADB2
		"--color-secondary-600": "37 156 160", // #259ca0
		"--color-secondary-700": "31 130 134", // #1f8286
		"--color-secondary-800": "25 104 107", // #19686b
		"--color-secondary-900": "20 85 87", // #145557
		// tertiary | #C5E898 
		"--color-tertiary-50": "246 252 240", // #f6fcf0
		"--color-tertiary-100": "243 250 234", // #f3faea
		"--color-tertiary-200": "241 249 229", // #f1f9e5
		"--color-tertiary-300": "232 246 214", // #e8f6d6
		"--color-tertiary-400": "214 239 183", // #d6efb7
		"--color-tertiary-500": "197 232 152", // #C5E898
		"--color-tertiary-600": "177 209 137", // #b1d189
		"--color-tertiary-700": "148 174 114", // #94ae72
		"--color-tertiary-800": "118 139 91", // #768b5b
		"--color-tertiary-900": "97 114 74", // #61724a
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