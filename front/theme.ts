
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
		"--on-primary": "0 0 0",
		"--on-secondary": "0 0 0",
		"--on-tertiary": "0 0 0",
		"--on-success": "0 0 0",
		"--on-warning": "0 0 0",
		"--on-error": "0 0 0",
		"--on-surface": "255 255 255",
		// =~= Theme Colors  =~=
		// primary | #ca9ee6 
		"--color-primary-50": "247 240 251", // #f7f0fb
		"--color-primary-100": "244 236 250", // #f4ecfa
		"--color-primary-200": "242 231 249", // #f2e7f9
		"--color-primary-300": "234 216 245", // #ead8f5
		"--color-primary-400": "218 187 238", // #dabbee
		"--color-primary-500": "202 158 230", // #ca9ee6
		"--color-primary-600": "182 142 207", // #b68ecf
		"--color-primary-700": "152 119 173", // #9877ad
		"--color-primary-800": "121 95 138", // #795f8a
		"--color-primary-900": "99 77 113", // #634d71
		// secondary | #8caaee 
		"--color-secondary-50": "238 242 252", // #eef2fc
		"--color-secondary-100": "232 238 252", // #e8eefc
		"--color-secondary-200": "226 234 251", // #e2eafb
		"--color-secondary-300": "209 221 248", // #d1ddf8
		"--color-secondary-400": "175 196 243", // #afc4f3
		"--color-secondary-500": "140 170 238", // #8caaee
		"--color-secondary-600": "126 153 214", // #7e99d6
		"--color-secondary-700": "105 128 179", // #6980b3
		"--color-secondary-800": "84 102 143", // #54668f
		"--color-secondary-900": "69 83 117", // #455375
		// tertiary | #f4b8e4 
		"--color-tertiary-50": "253 244 251", // #fdf4fb
		"--color-tertiary-100": "253 241 250", // #fdf1fa
		"--color-tertiary-200": "252 237 248", // #fcedf8
		"--color-tertiary-300": "251 227 244", // #fbe3f4
		"--color-tertiary-400": "247 205 236", // #f7cdec
		"--color-tertiary-500": "244 184 228", // #f4b8e4
		"--color-tertiary-600": "220 166 205", // #dca6cd
		"--color-tertiary-700": "183 138 171", // #b78aab
		"--color-tertiary-800": "146 110 137", // #926e89
		"--color-tertiary-900": "120 90 112", // #785a70
		// success | #a6d189 
		"--color-success-50": "242 248 237", // #f2f8ed
		"--color-success-100": "237 246 231", // #edf6e7
		"--color-success-200": "233 244 226", // #e9f4e2
		"--color-success-300": "219 237 208", // #dbedd0
		"--color-success-400": "193 223 172", // #c1dfac
		"--color-success-500": "166 209 137", // #a6d189
		"--color-success-600": "149 188 123", // #95bc7b
		"--color-success-700": "125 157 103", // #7d9d67
		"--color-success-800": "100 125 82", // #647d52
		"--color-success-900": "81 102 67", // #516643
		// warning | #e5c890 
		"--color-warning-50": "251 247 238", // #fbf7ee
		"--color-warning-100": "250 244 233", // #faf4e9
		"--color-warning-200": "249 241 227", // #f9f1e3
		"--color-warning-300": "245 233 211", // #f5e9d3
		"--color-warning-400": "237 217 177", // #edd9b1
		"--color-warning-500": "229 200 144", // #e5c890
		"--color-warning-600": "206 180 130", // #ceb482
		"--color-warning-700": "172 150 108", // #ac966c
		"--color-warning-800": "137 120 86", // #897856
		"--color-warning-900": "112 98 71", // #706247
		// error | #e78284 
		"--color-error-50": "251 236 237", // #fbeced
		"--color-error-100": "250 230 230", // #fae6e6
		"--color-error-200": "249 224 224", // #f9e0e0
		"--color-error-300": "245 205 206", // #f5cdce
		"--color-error-400": "238 168 169", // #eea8a9
		"--color-error-500": "231 130 132", // #e78284
		"--color-error-600": "208 117 119", // #d07577
		"--color-error-700": "173 98 99", // #ad6263
		"--color-error-800": "139 78 79", // #8b4e4f
		"--color-error-900": "113 64 65", // #714041
		// surface | #1e1e2e 
		"--color-surface-50": "221 221 224", // #dddde0
		"--color-surface-100": "210 210 213", // #d2d2d5
		"--color-surface-200": "199 199 203", // #c7c7cb
		"--color-surface-300": "165 165 171", // #a5a5ab
		"--color-surface-400": "98 98 109", // #62626d
		"--color-surface-500": "30 30 46", // #1e1e2e
		"--color-surface-600": "27 27 41", // #1b1b29
		"--color-surface-700": "23 23 35", // #171723
		"--color-surface-800": "18 18 28", // #12121c
		"--color-surface-900": "15 15 23", // #0f0f17
		
	}
}