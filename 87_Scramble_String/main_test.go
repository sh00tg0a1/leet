package main

import "testing"

func Test_isScramble(t *testing.T) {
	type args struct {
		s1 string
		s2 string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "3",
			args: args{
				s1: "abc",
				s2: "cba",
			},
			want: true,
		},
		{
			name: "4Y",
			args: args{
				s1: "abcd",
				s2: "bcad",
			},
			want: true,
		},
		{
			name: "4N",
			args: args{
				s1: "abcd",
				s2: "cadb",
			},
			want: false,
		},
		{
			name: "5N",
			args: args{
				s1: "abcde",
				s2: "caebd",
			},
			want: false,
		},
		{
			name: "5Y",
			args: args{
				s1: "great",
				s2: "rgeat",
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isScramble(tt.args.s1, tt.args.s2); got != tt.want {
				t.Errorf("isScramble() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isScramble2(t *testing.T) {
	type args struct {
		s1 string
		s2 string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "hard",
			args: args{
				s1: "abcdd",
				s2: "dbdac",
			},
			want: false,
		},
		{
			name: "very hard",
			args: args{
				s1: "abcdbdacbdac",
				s2: "bdacabcdbdac",
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isScramble(tt.args.s1, tt.args.s2); got != tt.want {
				t.Errorf("isScramble() = %v, want %v", got, tt.want)
			}
		})
	}
}
